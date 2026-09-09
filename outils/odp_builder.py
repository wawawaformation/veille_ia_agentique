#!/usr/bin/env python3
"""Utilitaires partagés pour générer des présentations ODP (LibreOffice Impress)
à partir de python-pptx, pour toutes les veilles du dépôt.

Pourquoi ce module existe : chaque veille a besoin d'un ODP support de
présentation live (cf. CLAUDE.md racine, section "Format des restitutions").
Plutôt que de dupliquer la construction pptx + conversion dans chaque
`fonds/<veille>/working/`, ce module centralise les fonctions génériques ;
chaque veille garde juste son propre script de CONTENU (titres, bullets,
images, notes propres à ses slides) qui importe ce module.

Usage type dans une veille (working/build_odp.py de cette veille) :

    import sys
    sys.path.insert(0, "/projets/veille/outils")
    from odp_builder import OdpBuilder

    b = OdpBuilder()  # 16:9 par défaut, fond blanc

    s = b.add_slide()
    b.add_title(s, "Mon titre de slide")
    b.add_bullets(s, ["Point 1", "Point 2"], left=Inches(0.8), top=Inches(1.8),
                  width=Inches(10), height=Inches(3))
    b.add_image_fit(s, "/chemin/vers/photo.jpg", left=Inches(7), top=Inches(1.5),
                     max_w=Inches(5), max_h=Inches(4.5))
    b.add_notes(s, duree="30s", fin="1:00",
                idees=["Idée principale 1", "Idée principale 2"],
                mots_cles=["mot1", "mot2"])

    b.save_and_convert_to_odp("/chemin/vers/final/ma_veille.odp")

Dépendances (venv recommandé, ne PAS installer au niveau système — piège
`externally-managed-environment` sur cette machine) :

    python3 -m venv /tmp/venv_odp && source /tmp/venv_odp/bin/activate
    pip install python-pptx Pillow

Piège déjà documenté dans le CLAUDE.md racine du dépôt : "Un PPTX n'est pas un
ODP. Convertir réellement (soffice --headless --convert-to odp), pas
seulement renommer l'extension." — `save_and_convert_to_odp()` applique
toujours une vraie conversion via `soffice`, jamais un renommage.
"""

import os
import shutil
import subprocess
import tempfile

from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR

# Palette par défaut — cohérente avec les schémas drawio produits par le skill
# schemas-drawio (voir ~/.claude/skills/schemas-drawio/), à réutiliser telle
# quelle pour que les slides et les schémas partagent le même code couleur.
DARK = RGBColor(0x33, 0x33, 0x33)
GREY = RGBColor(0x66, 0x66, 0x66)
ACCENT = RGBColor(0xD7, 0x9B, 0x00)
WHITE = RGBColor(0xFF, 0xFF, 0xFF)
BG_OFFWHITE = RGBColor(0xFA, 0xF9, 0xF6)  # fond de slide par défaut : jamais du blanc pur
GREEN = RGBColor(0x82, 0xB3, 0x66)
BLUE = RGBColor(0x6C, 0x8E, 0xBF)
RED = RGBColor(0xB8, 0x54, 0x50)


class OdpBuilder:
    def __init__(self, widescreen=True):
        self.prs = Presentation()
        if widescreen:
            self.prs.slide_width = Inches(13.333)
            self.prs.slide_height = Inches(7.5)
        self.blank_layout = self.prs.slide_layouts[6]
        self.SW = self.prs.slide_width
        self.SH = self.prs.slide_height

    # ------------------------------------------------------------------
    def add_slide(self, bg_color=BG_OFFWHITE):
        """bg_color=None pour laisser le fond par défaut du thème (pas de remplissage forcé)."""
        slide = self.prs.slides.add_slide(self.blank_layout)
        if bg_color is not None:
            bg = slide.background
            bg.fill.solid()
            bg.fill.fore_color.rgb = bg_color
        return slide

    def add_title(self, slide, text, size=32, top=Inches(0.4), color=DARK):
        box = slide.shapes.add_textbox(Inches(0.5), top, self.SW - Inches(1.0), Inches(1.0))
        tf = box.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.text = text
        p.font.size = Pt(size)
        p.font.bold = True
        p.font.color.rgb = color
        p.font.name = "Arial"
        return box

    def add_bullets(self, slide, bullets, left, top, width, height, size=18, color=DARK):
        box = slide.shapes.add_textbox(left, top, width, height)
        tf = box.text_frame
        tf.word_wrap = True
        for i, b in enumerate(bullets):
            p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
            p.text = b
            p.font.size = Pt(size)
            p.font.color.rgb = color
            p.font.name = "Arial"
            p.space_after = Pt(10)
        return box

    def add_image_fit(self, slide, path, left, top, max_w, max_h):
        """Insère une image en la centrant dans la zone (left,top,max_w,max_h)
        sans la déformer. Affiche un placeholder texte si le fichier n'existe pas
        (utile pour une capture d'écran pas encore prise)."""
        if not os.path.exists(path):
            box = slide.shapes.add_textbox(left, top, max_w, max_h)
            tf = box.text_frame
            tf.word_wrap = True
            p = tf.paragraphs[0]
            p.text = f"[ image manquante : {os.path.basename(path)} ]"
            p.font.size = Pt(14)
            p.font.italic = True
            p.font.color.rgb = GREY
            tf.vertical_anchor = MSO_ANCHOR.MIDDLE
            box.line.color.rgb = GREY
            box.line.width = Pt(1)
            return None
        from PIL import Image
        with Image.open(path) as im:
            iw, ih = im.size
        ratio = min(max_w / iw, max_h / ih)
        w, h = int(iw * ratio), int(ih * ratio)
        l = left + (max_w - w) // 2
        t = top + (max_h - h) // 2
        return slide.shapes.add_picture(path, l, t, width=w, height=h)

    def add_notes(self, slide, duree, fin, sur_slide, idees, mots_cles):
        """duree: str ex '45s'. fin: str ex '1:20' (timing de fin de la slide).
        sur_slide: phrase courte décrivant ce qui est déjà affiché à l'écran
        (bullets/images/tableau), pour se repérer sans redécouvrir la slide.
        idees: liste de phrases courtes (idées principales à dire à l'oral).
        mots_cles: liste de mots isolés (pense-bête ultra-rapide)."""
        notes = slide.notes_slide
        tf = notes.notes_text_frame
        tf.text = f"Durée : {duree}"
        p2 = tf.add_paragraph()
        p2.text = f"Timing de fin de la slide : {fin}"
        p3 = tf.add_paragraph()
        p3.text = "---"
        p3b = tf.add_paragraph()
        p3b.text = f"Sur la slide : {sur_slide}"
        p3c = tf.add_paragraph()
        p3c.text = "---"
        for idee in idees:
            p = tf.add_paragraph()
            p.text = f"• {idee}"
        p4 = tf.add_paragraph()
        p4.text = "---"
        p5 = tf.add_paragraph()
        p5.text = "Mots-clés : " + ", ".join(mots_cles)

    def add_timing_footer(self, slide, timing, duree):
        box = slide.shapes.add_textbox(self.SW - Inches(2.2), self.SH - Inches(0.4), Inches(2.0), Inches(0.3))
        tf = box.text_frame
        p = tf.paragraphs[0]
        p.text = f"{timing} · {duree}"
        p.font.size = Pt(10)
        p.font.color.rgb = GREY
        p.alignment = PP_ALIGN.RIGHT

    def add_table(self, slide, rows_data, headers, left, top, width, height, font_size=14):
        """rows_data: liste de tuples/listes (une ligne = une entrée, sans les headers)."""
        n_rows = len(rows_data) + 1
        n_cols = len(headers)
        tbl_shape = slide.shapes.add_table(n_rows, n_cols, left, top, width, height)
        tbl = tbl_shape.table
        for c, h in enumerate(headers):
            tbl.cell(0, c).text = h
        for r, row in enumerate(rows_data, start=1):
            for c, val in enumerate(row):
                tbl.cell(r, c).text = str(val)
        for r in range(n_rows):
            for c in range(n_cols):
                for p in tbl.cell(r, c).text_frame.paragraphs:
                    p.font.size = Pt(font_size)
                    p.font.name = "Arial"
        return tbl_shape

    # ------------------------------------------------------------------
    def save_and_convert_to_odp(self, output_path, keep_pptx=False):
        """Sauvegarde en .pptx temporaire puis convertit RÉELLEMENT en .odp via
        soffice --headless --convert-to odp (filtre impress8), jamais un simple
        renommage. output_path doit se terminer par .odp."""
        assert output_path.endswith(".odp"), "output_path doit se terminer par .odp"
        out_dir = os.path.dirname(os.path.abspath(output_path))
        os.makedirs(out_dir, exist_ok=True)

        with tempfile.TemporaryDirectory() as tmp:
            pptx_path = os.path.join(tmp, "presentation.pptx")
            self.prs.save(pptx_path)

            result = subprocess.run(
                ["soffice", "--headless", "--convert-to", "odp", "--outdir", tmp, pptx_path],
                capture_output=True, text=True, timeout=120,
            )
            if result.returncode != 0:
                raise RuntimeError(f"Échec conversion soffice :\n{result.stdout}\n{result.stderr}")

            generated_odp = os.path.join(tmp, "presentation.odp")
            if not os.path.exists(generated_odp):
                raise RuntimeError(f"soffice n'a pas produit de .odp. stdout={result.stdout} stderr={result.stderr}")

            shutil.move(generated_odp, output_path)

            if keep_pptx:
                kept_path = output_path[:-4] + ".pptx"
                shutil.copy(pptx_path, kept_path)

        n_slides = len(self.prs.slides._sldIdLst)
        print(f"OK : {n_slides} slides converties → {output_path}")
        return output_path
