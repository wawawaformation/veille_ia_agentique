import argparse
import base64
import json
import os
import re
from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI


# ============================================================
# CONFIG
# ============================================================

load_dotenv(override=True)

OLLAMA_API_KEY = os.environ["OLLAMA_API_KEY"]

MODEL = "glm-5.3-flash"

parser = argparse.ArgumentParser(
    description="Transcrit une image avec GLM-5.3-Flash via Ollama Cloud."
)

parser.add_argument(
    "image",
    type=Path,
    help="Fichier image à transcrire.",
)

parser.add_argument(
    "--output",
    type=Path,
    default=Path("output"),
    help="Dossier de sortie des fichiers Markdown (défaut : output).",
)

parser.add_argument(
    "--logs",
    type=Path,
    default=Path("logs"),
    help="Dossier de sortie des logs JSON (défaut : logs).",
)

args = parser.parse_args()

IMAGE_PATH = args.image
OUTPUT_DIR = args.output
LOG_DIR = args.logs

if not IMAGE_PATH.is_file():
    parser.error(f"Fichier image introuvable : {IMAGE_PATH}")

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
LOG_DIR.mkdir(parents=True, exist_ok=True)


# ============================================================
# OUTILS
# ============================================================

def image_to_data_url(path: Path) -> str:
    image_bytes = path.read_bytes()
    image_b64 = base64.b64encode(image_bytes).decode("utf-8")

    return f"data:image/png;base64,{image_b64}"


def extract_document_metadata(reasoning: str) -> dict:
    """
    Extrait les métadonnées documentaires depuis le reasoning GLM.

    Exemples observés :

    Header: "Le Capital" (italic, centered...)
    Page number: 3, at the bottom center.

    ou :

    The page header is "Le Capital"
    Page number is 3 at the bottom.
    """

    metadata = {
        "title": None,
        "header": None,
        "page": None,
        "page_number_position": None,
    }

    # --------------------------------------------------------
    # HEADER
    # --------------------------------------------------------

    header_patterns = [
        r'header\s*:\s*["“](.+?)["”]',
        r'(?:the\s+)?page\s+header\s+is\s+["“](.+?)["”]',
    ]

    for pattern in header_patterns:
        match = re.search(
            pattern,
            reasoning,
            flags=re.IGNORECASE,
        )

        if match:
            header = match.group(1).strip()

            metadata["header"] = header
            metadata["title"] = header

            break


    # --------------------------------------------------------
    # NUMÉRO DE PAGE
    # --------------------------------------------------------

    page_patterns = [
        r'page\s+number\s*:\s*(\d+)',
        r'page\s+number\s+is\s+(\d+)',
    ]

    for pattern in page_patterns:
        match = re.search(
            pattern,
            reasoning,
            flags=re.IGNORECASE,
        )

        if match:
            metadata["page"] = int(match.group(1))
            break


    # --------------------------------------------------------
    # POSITION DU NUMÉRO
    # --------------------------------------------------------

    lower = reasoning.lower()

    if "page number" in lower:

        if "bottom center" in lower:
            metadata["page_number_position"] = "bottom_center"

        elif "bottom right" in lower:
            metadata["page_number_position"] = "bottom_right"

        elif "bottom left" in lower:
            metadata["page_number_position"] = "bottom_left"

        elif "bottom" in lower:
            metadata["page_number_position"] = "bottom"

        elif "top center" in lower:
            metadata["page_number_position"] = "top_center"

        elif "top right" in lower:
            metadata["page_number_position"] = "top_right"

        elif "top left" in lower:
            metadata["page_number_position"] = "top_left"

        elif "top" in lower:
            metadata["page_number_position"] = "top"


    return metadata


def extract_quality_signals(reasoning: str) -> dict:
    """
    Extraction très simple de signaux présents dans le reasoning.

    Ce n'est pas encore le vrai contrôle qualité LLM.
    """

    r = reasoning.lower()

    return {
        "dehyphenation_applied": any(
            marker in r
            for marker in (
                "hyphenated",
                "hyphenation",
                "joined",
                "should be joined",
                "split across lines",
                "end-of-line",
                "line break",
            )
        ),

        "uncertain_reading": any(
            marker in r
            for marker in (
                "unclear",
                "uncertain",
                "difficult to read",
                "hard to read",
                "not sure",
                "ambiguous",
                "possibly",
                "may be",
            )
        ),

        "omission_suspected": any(
            marker in r
            for marker in (
                "omit",
                "omitted",
                "missing text",
                "cannot read",
                "can't read",
                "illegible",
                "unreadable",
            )
        ),

        "reconstruction_detected": any(
            marker in r
            for marker in (
                "joined",
                "reconstruct",
                "split across lines",
                "hyphenated",
                "hyphenation",
            )
        ),
    }


def clean_content(
    content: str,
    document_metadata: dict,
) -> str:
    """
    Nettoie le contenu OCR pour retirer les éléments documentaires
    déjà transférés dans le front matter.

    Actuellement :
    - header/titre au début,
    - règle Markdown éventuelle,
    - numéro de page en fin,
    - règle Markdown éventuelle avant le numéro.
    """

    lines = content.strip().splitlines()

    header = document_metadata.get("header")
    page = document_metadata.get("page")


    # --------------------------------------------------------
    # RETIRE LE HEADER
    # --------------------------------------------------------

    if header and lines:

        first = lines[0].strip()

        # Exemples supportés :
        #
        # # Le Capital
        # ## Le Capital
        # *Le Capital*
        # **Le Capital**
        # Le Capital

        candidate = re.sub(
            r"^#{1,6}\s*",
            "",
            first,
        )

        candidate = candidate.strip("*_ ").strip()

        if candidate == header:

            lines.pop(0)

            # lignes vides après header
            while lines and not lines[0].strip():
                lines.pop(0)

            # règle Markdown éventuelle
            if lines and lines[0].strip() == "---":
                lines.pop(0)

            # nouvelles lignes vides
            while lines and not lines[0].strip():
                lines.pop(0)


    # --------------------------------------------------------
    # RETIRE LE NUMÉRO DE PAGE
    # --------------------------------------------------------

    if page is not None:

        # supprime lignes vides finales
        while lines and not lines[-1].strip():
            lines.pop()

        # numéro final
        if lines and lines[-1].strip() == str(page):
            lines.pop()

        # supprime lignes vides
        while lines and not lines[-1].strip():
            lines.pop()

        # règle Markdown éventuelle juste avant le numéro
        if lines and lines[-1].strip() == "---":
            lines.pop()

        # supprime encore les lignes vides finales
        while lines and not lines[-1].strip():
            lines.pop()


    return "\n".join(lines).strip()


def yaml_value(value):
    """
    Petit sérialiseur YAML suffisant pour ce prototype.
    """

    if value is None:
        return "null"

    if isinstance(value, bool):
        return "true" if value else "false"

    if isinstance(value, (int, float)):
        return str(value)

    escaped = (
        str(value)
        .replace("\\", "\\\\")
        .replace('"', '\\"')
    )

    return f'"{escaped}"'


def build_front_matter(
    document: dict,
    source: dict,
    ocr: dict,
    analysis: dict,
    quality: dict,
) -> str:

    lines = [
        "---",

        "document:",
        f"  title: {yaml_value(document.get('title'))}",
        f"  page: {yaml_value(document.get('page'))}",
        f"  header: {yaml_value(document.get('header'))}",
        (
            "  page_number_position: "
            f"{yaml_value(document.get('page_number_position'))}"
        ),

        "",

        "source:",
        f"  file: {yaml_value(source.get('file'))}",
        f"  format: {yaml_value(source.get('format'))}",

        "",

        "ocr:",
        f"  provider: {yaml_value(ocr.get('provider'))}",
        f"  model: {yaml_value(ocr.get('model'))}",
        f"  prompt_tokens: {yaml_value(ocr.get('prompt_tokens'))}",
        (
            "  completion_tokens: "
            f"{yaml_value(ocr.get('completion_tokens'))}"
        ),
        f"  total_tokens: {yaml_value(ocr.get('total_tokens'))}",
        f"  finish_reason: {yaml_value(ocr.get('finish_reason'))}",

        "",

        "analysis:",
        (
            "  dehyphenation_applied: "
            f"{yaml_value(analysis.get('dehyphenation_applied'))}"
        ),
        (
            "  uncertain_reading: "
            f"{yaml_value(analysis.get('uncertain_reading'))}"
        ),
        (
            "  omission_suspected: "
            f"{yaml_value(analysis.get('omission_suspected'))}"
        ),
        (
            "  reconstruction_detected: "
            f"{yaml_value(analysis.get('reconstruction_detected'))}"
        ),

        "",

        "quality:",
        f"  status: {yaml_value(quality.get('status'))}",
        f"  controller: {yaml_value(quality.get('controller'))}",
        f"  fallback_used: {yaml_value(quality.get('fallback_used'))}",

        "---",
    ]

    return "\n".join(lines)


# ============================================================
# CLIENT OLLAMA CLOUD
# ============================================================

client = OpenAI(
    base_url="https://ollama.com/v1",
    api_key=OLLAMA_API_KEY,
)


# ============================================================
# IMAGE
# ============================================================

data_url = image_to_data_url(IMAGE_PATH)


# ============================================================
# PROMPT OCR
# ============================================================

prompt = """
Tu transcris cette page scannée en Markdown propre.

Respecte strictement le texte principal visible et son ordre de lecture.

Pendant ton analyse, identifie notamment :
- le titre courant ou l'en-tête ;
- le numéro de page ;
- la position du numéro de page ;
- les éventuelles césures de fin de ligne ;
- les zones ambiguës, illisibles ou parasites.

Ces éléments servent uniquement à ton analyse interne.

Dans la réponse finale :
- retourne uniquement le texte principal transcrit ;
- n'ajoute aucun commentaire ;
- n'ajoute aucune section "Transcription" ;
- n'ajoute aucune section de métadonnées ;
- n'inclus pas l'en-tête courant ;
- n'inclus pas le numéro de page ;
- rétablis les mots coupés artificiellement en fin de ligne ;
- ne résume pas ;
- n'invente pas ;
- ne complète pas ce qui n'est pas lisible.
""".strip()


# ============================================================
# APPEL GLM
# ============================================================

response = client.chat.completions.create(
    model=MODEL,
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": prompt,
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": data_url,
                    },
                },
            ],
        }
    ],
)


# ============================================================
# RÉCUPÉRATION
# ============================================================

choice = response.choices[0]
message = choice.message

message_dict = message.model_dump()

content = message.content or ""

reasoning = (
    message_dict.get("reasoning")
    or ""
)

usage = response.usage


# ============================================================
# EXTRACTION MÉTADONNÉES
# ============================================================

document_metadata = extract_document_metadata(
    reasoning
)

analysis_metadata = extract_quality_signals(
    reasoning
)


# ============================================================
# NETTOYAGE DU CONTENU
# ============================================================

clean_markdown = clean_content(
    content,
    document_metadata,
)


# ============================================================
# MÉTADONNÉES TECHNIQUES
# ============================================================

source_metadata = {
    "file": IMAGE_PATH.name,
    "format": IMAGE_PATH.suffix.lstrip(".").lower(),
}


ocr_metadata = {
    "provider": "ollama",
    "model": MODEL,

    "prompt_tokens": (
        usage.prompt_tokens
        if usage
        else None
    ),

    "completion_tokens": (
        usage.completion_tokens
        if usage
        else None
    ),

    "total_tokens": (
        usage.total_tokens
        if usage
        else None
    ),

    "finish_reason": choice.finish_reason,
}


# Pas encore de vrai contrôleur qualité

quality_metadata = {
    "status": "pending",
    "controller": None,
    "fallback_used": False,
}


# ============================================================
# FRONT MATTER
# ============================================================

front_matter = build_front_matter(
    document=document_metadata,
    source=source_metadata,
    ocr=ocr_metadata,
    analysis=analysis_metadata,
    quality=quality_metadata,
)


final_markdown = (
    front_matter
    + "\n\n"
    + clean_markdown
    + "\n"
)


# ============================================================
# NOM DE SORTIE
# ============================================================

page_number = document_metadata.get("page")

if page_number is not None:

    stem = f"page_{page_number:03d}"

else:

    stem = IMAGE_PATH.stem


md_path = OUTPUT_DIR / f"{stem}.md"
json_path = LOG_DIR / f"{stem}.json"


# ============================================================
# SAUVEGARDE MARKDOWN
# ============================================================

md_path.write_text(
    final_markdown,
    encoding="utf-8",
)


# ============================================================
# LOG COMPLET
# ============================================================

log = {
    "source": source_metadata,

    "document": document_metadata,

    "ocr": ocr_metadata,

    "analysis": analysis_metadata,

    "quality": quality_metadata,

    "content_raw": content,

    "content_clean": clean_markdown,

    "reasoning_raw": reasoning,

    "response": response.model_dump(),
}


json_path.write_text(
    json.dumps(
        log,
        ensure_ascii=False,
        indent=2,
    ),
    encoding="utf-8",
)


# ============================================================
# AFFICHAGE
# ============================================================

print()

print("=" * 80)
print("DOCUMENT")
print("=" * 80)

print(
    json.dumps(
        document_metadata,
        indent=2,
        ensure_ascii=False,
    )
)


print()

print("=" * 80)
print("SIGNAUX EXTRAITS DU REASONING")
print("=" * 80)

print(
    json.dumps(
        analysis_metadata,
        indent=2,
        ensure_ascii=False,
    )
)


print()

print("=" * 80)
print("MARKDOWN FINAL")
print("=" * 80)

print(final_markdown)


print()

print("=" * 80)
print("FICHIERS")
print("=" * 80)

print(f"Markdown : {md_path}")
print(f"Log JSON : {json_path}")