#!/usr/bin/env python3
"""Génère l'ODP de la présentation à partir de plan_slides.md (contenu codé en
dur, pas de parsing automatique). Utilise le module partagé
`/projets/veille/outils/odp_builder.py` — voir ce fichier pour les fonctions
génériques réutilisées par toutes les veilles.

Pour régénérer après modification (ex : ajout de la capture d'écran Ollama slide 19) :

    python3 -m venv /tmp/venv_odp && source /tmp/venv_odp/bin/activate
    pip install python-pptx Pillow
    python3 build_odp.py
"""

import sys
from pptx.util import Inches, Pt

sys.path.insert(0, "/projets/veille/outils")
from odp_builder import OdpBuilder, DARK, GREY, ACCENT

BASE = "/projets/veille/fonds/mistral_est_il_vraiment_opensource/working/images"
PHOTOS = f"{BASE}/photos"
FINAL_OUT = "/projets/veille/fonds/mistral_est_il_vraiment_opensource/final/mistral_est_il_vraiment_opensource.odp"

b = OdpBuilder()

# ============================================================
# SLIDE 1 : Titre
# ============================================================
s = b.add_slide()
b.add_image_fit(s, f"{PHOTOS}/slide1.jpg", Inches(0), Inches(0), b.SW, Inches(5.6))
box = s.shapes.add_textbox(Inches(0.5), Inches(5.7), b.SW - Inches(1.0), Inches(1.6))
tf = box.text_frame
tf.word_wrap = True
p = tf.paragraphs[0]
p.text = "Mistral est-il vraiment open source ?"
p.font.size = Pt(34)
p.font.bold = True
p.font.color.rgb = DARK
p.font.name = "Arial"
from pptx.enum.text import PP_ALIGN
p.alignment = PP_ALIGN.CENTER
p2 = tf.add_paragraph()
p2.text = "Décortiquer le continuum d'ouverture en IA"
p2.font.size = Pt(18)
p2.font.color.rgb = GREY
p2.font.name = "Arial"
p2.alignment = PP_ALIGN.CENTER
b.add_notes(s, "0s", "0:00", "Photo chat + Pinocchio en fond, titre et sous-titre en dessous", ["Slide de garde", "Oral démarre direct sur l'agenda"], ["titre", "Pinocchio", "mensonge"])

# ============================================================
# SLIDE 2 : Agenda
# ============================================================
s = b.add_slide()
b.add_title(s, "Agenda")
b.add_bullets(s, [
    "📚 Bloc 1 : Logiciel libre et standards ouverts",
    "🤖 Bloc 2 : Le continuum d'ouverture en IA",
    "⚖️ Bloc 3 : Réglementaire + frugalité",
    "🔧 Bloc 4 : Ollama, conclusion et twist final",
], Inches(0.8), Inches(1.8), Inches(8), Inches(4), size=24)
b.add_notes(s, "15s", "0:15", "Titre « Agenda » + 4 bullets avec emoji (un par bloc)", ["4 blocs à annoncer", "Emojis suffisent, pas de détail à lire"], ["agenda", "4 blocs", "sommaire"])

# ============================================================
# SLIDE 3 : Intro Bloc 1
# ============================================================
s = b.add_slide()
b.add_title(s, "Bloc 1 — Logiciel libre et standards ouverts")
b.add_bullets(s, [
    "Pour comprendre « open source » en IA, il faut d'abord comprendre le logiciel libre traditionnel",
    "Trois concepts clés : libertés, standards, interopérabilité",
], Inches(0.8), Inches(1.8), Inches(10), Inches(3), size=22)
b.add_notes(s, "20s", "0:35", "Titre du bloc 1 + 2 bullets (comprendre le logiciel libre d'abord, 3 concepts clés)", ["Transition orale", "Comprimée : dire vite sans perdre l'auditoire"], ["transition", "logiciel libre"])

# ============================================================
# SLIDE 4 : Les 4 libertés
# ============================================================
s = b.add_slide()
b.add_title(s, "Les 4 libertés (FSF, Richard Stallman)")
b.add_bullets(s, [
    "Liberté 0 : Utiliser",
    "Liberté 1 : Étudier et modifier",
    "Liberté 2 : Redistribuer",
    "Liberté 3 : Redistribuer modifiée",
], Inches(0.6), Inches(1.6), Inches(6.5), Inches(3.5), size=22)
b.add_image_fit(s, f"{PHOTOS}/slide4_recette.jpg", Inches(7.3), Inches(1.6), Inches(5.4), Inches(4.5))
b.add_notes(s, "45s", "1:20", "4 bullets (les 4 libertés) à gauche, photo d'un carnet de recette à droite", ["Analogie : recette de cuisine", "Modifier + partager, pas juste utiliser"], ["4 libertés", "FSF", "Stallman", "recette"])

# ============================================================
# SLIDE 5 : Standards ouverts (USB patchwork)
# ============================================================
s = b.add_slide()
b.add_title(s, "Standards ouverts ≠ Logiciel libre")
b.add_bullets(s, [
    "Un standard ouvert = une spécification commune que tout le monde peut respecter",
    "USB, TCP/IP, HTTP, HTML",
], Inches(0.6), Inches(1.4), Inches(11.5), Inches(1.3), size=20)
b.add_image_fit(s, f"{PHOTOS}/slide5_usb_patchwork.jpg", Inches(2.5), Inches(2.7), Inches(8.3), Inches(4.4))
b.add_notes(s, "30s", "1:50", "2 bullets (définition standard ouvert + exemples) en haut, patchwork USB (sigle, souris, manettes, disque dur) en dessous", ["Analogie USB : même standard, matériel différent", "Liberté d'interagir/changer de prestataire, pas de modifier le code"], ["USB", "standard ouvert", "interopérabilité"])

# ============================================================
# SLIDE 6 : Transition vers IA
# ============================================================
s = b.add_slide()
b.add_title(s, "Maintenant, appliquons ça à l'IA…")
b.add_bullets(s, [
    "Maintenant qu'on a ces concepts clés…",
    "La question : « Comment appliquer ça à l'IA ? »",
    "Parce qu'un modèle d'IA n'est pas qu'un programme",
], Inches(0.8), Inches(1.8), Inches(10), Inches(3), size=22)
b.add_notes(s, "20s", "2:10", "Titre + 3 bullets (transition logiciel → IA)", ["Transition vers IA", "Comprimée"], ["transition", "IA"])

# ============================================================
# SLIDE 7 : Pourquoi IA complique la notion
# ============================================================
s = b.add_slide()
b.add_title(s, "Un modèle d'IA ≠ Un programme classique")
b.add_bullets(s, [
    "Logiciel : le code source explique tout",
    "IA : son comportement vient de 3 composantes indépendantes",
    "→ Poids (paramètres appris)",
    "→ Recette d'entraînement (code + hyperparamètres)",
    "→ Données (le matériau brut)",
], Inches(0.6), Inches(1.4), Inches(11.5), Inches(2.2), size=18)
b.add_image_fit(s, f"{BASE}/slide7_code_vs_composantes_preview.png", Inches(1.5), Inches(3.6), Inches(10.3), Inches(3.5))
b.add_notes(s, "40s", "2:50", "5 bullets (logiciel vs IA, 3 composantes) en haut, schéma code Python vs 3 boîtes en dessous", ["Pivot conceptuel du bloc 2", "Code Python (1 truc) vs 3 boîtes (poids/recette/données)"], ["3 composantes", "pivot", "code source"])

# ============================================================
# SLIDE 8 : Analogie gâteau
# ============================================================
s = b.add_slide()
b.add_title(s, "Comment fabrique-t-on un modèle ? (analogie du gâteau)")
b.add_image_fit(s, f"{PHOTOS}/slide8_ingredients.jpg", Inches(0.4), Inches(1.6), Inches(3.6), Inches(3.6))
b.add_image_fit(s, f"{PHOTOS}/slide8_gateau_fini.jpg", Inches(4.2), Inches(1.6), Inches(3.6), Inches(3.6))
b.add_image_fit(s, f"{BASE}/slide8_gateau_composantes_preview.png", Inches(8.0), Inches(1.6), Inches(4.9), Inches(3.6))
b.add_notes(s, "40s", "3:30", "Titre + 3 images côte à côte : ingrédients, gâteau fini, schéma labellisé Poids/Recette/Données", ["Gâteau fini = tu peux manger mais pas reproduire", "Poids=gâteau / Recette=processus / Données=ingrédients"], ["poids", "recette", "données", "gâteau"])

# ============================================================
# SLIDE 9 : OSAID distinction
# ============================================================
s = b.add_slide()
b.add_title(s, "Open weight vs Open source : la distinction critique")
b.add_table(s,
    headers=["", "Open weight", "Open source"],
    rows_data=[
        ("Poids", "✓ Public", "✓ Public"),
        ("Recette + données", "✗ Fermé", "✓ Public"),
        ("Libertés FSF", "Liberté 0 seule", "Libertés 0-3 ✓✓✓"),
    ],
    left=Inches(0.6), top=Inches(1.5), width=Inches(6.5), height=Inches(2.2),
)
b.add_image_fit(s, f"{PHOTOS}/slide9_gateau_emballe.jpg", Inches(7.4), Inches(1.5), Inches(2.7), Inches(3.5))
b.add_image_fit(s, f"{PHOTOS}/slide8_gateau_fini.jpg", Inches(10.3), Inches(1.5), Inches(2.7), Inches(3.5))
b.add_bullets(s, [
    "« Filtre d'amour » : open weight te fait confiance au vendeur. Open source te permet d'auditer toi-même.",
], Inches(0.6), Inches(4.0), Inches(6.5), Inches(1.5), size=16, color=ACCENT)
b.add_notes(s, "35s", "4:05", "Tableau 2×3 (poids/recette+données/libertés) à gauche, photos brioche + gâteau à droite, phrase filtre d'amour en bas", ["Open weight = confiance aveugle (gâteau emballé)", "Open source = confiance vérifiée (tout visible)", "Filtre d'amour"], ["open weight", "open source", "filtre d'amour"])

# ============================================================
# SLIDE 10 : Continuum 4 catégories
# ============================================================
s = b.add_slide()
b.add_title(s, "Le continuum en 4 catégories")
b.add_image_fit(s, f"{BASE}/slide10_continuum_gradient_preview.png", Inches(0.6), Inches(1.5), Inches(12.1), Inches(4.8))
b.add_notes(s, "40s", "4:45", "Titre + schéma gradient 4 catégories pleine largeur (Mistral positionné, exemples : GPT/Claude/Gemini, Llama/Mistral/DeepSeek, gpt-oss/Gemma/Qwen, OLMo/Apertus/Luciole)", ["4 catégories : Fermé/API, Open weight, Open weight++, Open source", "Mistral = open weight", "27 modèles en annexe"], ["continuum", "4 catégories", "Mistral", "gpt-oss", "Apertus"])

# ============================================================
# SLIDE 11 : Biais invisibles
# ============================================================
s = b.add_slide()
b.add_title(s, "Pourquoi la distinction importe vraiment", size=28)
b.add_bullets(s, [
    "Exemple 1 : Les données cachées",
    "Imagine un modèle entraîné sur des données contaminées par la propagande d'un dictateur",
    "Open weight seul : tu goûtes le gâteau, c'est bizarre, mais tu ne sais pas d'où ça vient",
    "Open source : tu vois la recette et les ingrédients, tu repères la source contaminée",
], Inches(0.6), Inches(1.5), Inches(6.5), Inches(4), size=17)
b.add_image_fit(s, f"{PHOTOS}/slide11_eau_trouble.jpg", Inches(7.3), Inches(1.5), Inches(2.6), Inches(4.5))
b.add_image_fit(s, f"{PHOTOS}/slide11_eau_claire.jpg", Inches(10.0), Inches(1.5), Inches(2.6), Inches(4.5))
b.add_notes(s, "35s", "5:20", "4 bullets (exemple biais) à gauche, photos eau trouble + eau claire à droite", ["Eau contaminée invisible = biais caché", "Indépendance de penser dépend de la transparence"], ["biais", "données", "eau contaminée", "filtre d'amour"])

# ============================================================
# SLIDE 12 : Cas Lucie
# ============================================================
s = b.add_slide()
b.add_title(s, "Erreurs méthodologiques révélées (cas Lucie)", size=28)
b.add_bullets(s, [
    "OpenLLM France, janvier 2025",
    "Lucie lancée en version inachevée, non censurée",
    "Communauté a vu les erreurs et dénoncé",
    "Forcé de corriger",
    "Si Lucie était fermée : personne n'aurait jamais su",
], Inches(0.6), Inches(1.5), Inches(6.8), Inches(4.2), size=17)
b.add_image_fit(s, f"{PHOTOS}/slide12_ferme.jpg", Inches(7.6), Inches(1.5), Inches(5.1), Inches(4.5))
b.add_notes(s, "20s", "5:40", "5 bullets (cas Lucie) à gauche, photo panneau CLOSED à droite", ["Cas Lucie (OpenLLM France, janvier 2025)", "Restaurant qui ferme pour refaire la cuisine", "Ouverture = correction communautaire"], ["Lucie", "OpenLLM France", "correction communautaire"])

# ============================================================
# SLIDE 13 : Transition Bloc 3
# ============================================================
s = b.add_slide()
b.add_title(s, "Comment les gouvernements définissent-ils « open source » ?")
b.add_bullets(s, [
    "L'UE a répondu avec l'AI Act.",
    "Et la réponse n'est pas celle qu'on attendrait…",
], Inches(0.8), Inches(2.2), Inches(10), Inches(2), size=22)
b.add_notes(s, "15s", "5:55", "Titre + 2 bullets (question réglementaire, AI Act)", ["Transition vers réglementaire (AI Act)", "Comprimée"], ["transition", "AI Act"])

# ============================================================
# SLIDE 14 : 3 définitions
# ============================================================
s = b.add_slide()
b.add_title(s, "Attention : 3 définitions différentes du mot « open source »", size=26)
b.add_table(s,
    headers=["Contexte", "Définition", "Exigence sur les données"],
    rows_data=[
        ("Marketing", "Poids publiés, transparent-ish", "Rien"),
        ("AI Act (légal)", "Licence libre + architecture publique + non monétisé", "Un résumé du contenu (art. 53(1)(d))"),
        ("OSAID (OSI)", "Utiliser / étudier / modifier / redistribuer", "Infos suffisantes pour reconstruire"),
    ],
    left=Inches(0.5), top=Inches(1.5), width=Inches(6.0), height=Inches(2.6), font_size=13,
)
b.add_image_fit(s, f"{BASE}/slide14_venn_definitions_preview.png", Inches(6.8), Inches(1.4), Inches(6.1), Inches(4.8))
b.add_notes(s, "25s", "6:20", "Tableau 3 définitions à gauche, schéma Venn à droite", ["3 définitions : Marketing, AI Act, OSAID", "AI Act plus LÉGER que OSAID : un résumé des données suffit, pas les données", "Aucune ne recouvre les autres", "Commenter surtout le Venn, tableau en lecture silencieuse"], ["3 définitions", "Venn", "OSAID", "résumé ≠ données"])

# ============================================================
# SLIDE 15 : AI Act seuil
# ============================================================
s = b.add_slide()
b.add_title(s, "L'Union européenne exempte les modèles « open source »", size=26)
b.add_bullets(s, [
    "Article 2(12) : exemption pour open source (risque systémique allégé)",
    "Mais : seuil à 10²⁵ FLOPs (article 51(2))",
    "Paradoxe : Llama-3 405B ≈ 3,8 × 10²⁵ FLOPs → au-dessus du seuil",
], Inches(0.6), Inches(1.5), Inches(11.5), Inches(1.8), size=18)
b.add_image_fit(s, f"{BASE}/slide15_seuil_flops_preview.png", Inches(0.6), Inches(3.3), Inches(11.5), Inches(3.3))
b.add_notes(s, "40s", "7:00", "3 bullets (exemption, seuil, paradoxe Llama) en haut, schéma jauge FLOPs en dessous", ["Exemption AI Act pour open source", "Seuil 10²⁵ FLOPs", "Llama-3 405B dépasse le seuil"], ["AI Act", "seuil FLOPs", "Llama-3"])

# ============================================================
# SLIDE 16 : Frugalité piscine
# ============================================================
s = b.add_slide()
b.add_title(s, "La fausse bonne idée : local = plus écolo ?", size=28)
b.add_bullets(s, [
    "Intuition : faire tourner un modèle chez moi, c'est plus écolo qu'une API cloud",
    "Réalité : c'est plus compliqué",
], Inches(0.6), Inches(1.4), Inches(11.5), Inches(1.3), size=18)
b.add_image_fit(s, f"{PHOTOS}/slide16_piscine_privee.jpg", Inches(1.0), Inches(2.8), Inches(5.3), Inches(4.2))
b.add_image_fit(s, f"{PHOTOS}/slide16_piscine_publique.jpg", Inches(6.6), Inches(2.8), Inches(5.3), Inches(4.2))
b.add_notes(s, "25s", "7:25", "2 bullets (intuition/réalité) en haut, photos piscine privée + publique en dessous", ["Analogie piscine privée vs communautaire", "Paradoxe de Jevons"], ["frugalité", "piscine", "Jevons"])

# ============================================================
# SLIDE 17 : Seuil GPU 85%
# ============================================================
s = b.add_slide()
b.add_title(s, "Quand est-ce que local devient compétitif ?", size=28)
b.add_image_fit(s, f"{BASE}/slide17_seuil_gpu_preview.png", Inches(0.8), Inches(1.6), Inches(11.7), Inches(4.5))
b.add_notes(s, "20s", "7:45", "Titre + schéma jauge 85% GPU pleine largeur", ["Seuil 85% utilisation GPU", "Vérifier les chiffres, pas supposer"], ["85%", "GPU", "cloud", "local"])

# ============================================================
# SLIDE 18 : Conclusion Bloc 3
# ============================================================
s = b.add_slide()
b.add_title(s, "Pragmatisme")
b.add_bullets(s, [
    "Local pas forcément mieux",
    "API cloud pas forcément pire",
    "L'intérêt de open weight : tu peux décider au cas par cas",
], Inches(0.8), Inches(2.0), Inches(10), Inches(3), size=22)
b.add_notes(s, "10s", "7:55", "Titre « Pragmatisme » + 3 bullets", ["Quasi fusionnée avec S17, enchaîner sans pause", "Local pas forcément mieux, cloud pas forcément pire"], ["pragmatisme", "fusion S17"])

# ============================================================
# SLIDE 19 : Ollama
# ============================================================
s = b.add_slide()
b.add_title(s, "Ollama : comment ça fonctionne ?", size=28)
b.add_bullets(s, [
    "Plateforme MIT (code ouvert)",
    "Catalogue exclusivement open weight + open source (zéro fermé/API)",
    "3 modes : Local (CLI gratuit) / API (gratuit, limité) / Cloud Pro (20$/mois)",
    "Exemples : Llama, OLMo, Gemma, Llama Vision",
], Inches(0.6), Inches(1.5), Inches(6.8), Inches(4), size=17)
b.add_image_fit(s, f"{PHOTOS}/slide19_ollama_screenshot.png", Inches(7.6), Inches(1.5), Inches(5.1), Inches(4.5))
b.add_notes(s, "20s", "8:15", "4 bullets (plateforme, catalogue, modes, exemples) à gauche, capture d'écran (ou placeholder) à droite", ["Monétisation = infrastructure cloud, pas les modèles", "CAPTURE D'ÉCRAN MANQUANTE à insérer"], ["Ollama", "MIT", "catalogue"])

# ============================================================
# SLIDE 20 : Conclusion générale
# ============================================================
s = b.add_slide()
b.add_title(s, "Mistral est-il vraiment open source ?")
b.add_bullets(s, [
    "Non. Mistral est open weight.",
    "Pour être open source, il faudrait aussi publier les données et la recette d'entraînement.",
    "« Open source » n'est pas une case qu'on coche : c'est un continuum, et c'est un choix.",
], Inches(0.6), Inches(1.5), Inches(11.5), Inches(2), size=19)
b.add_image_fit(s, f"{BASE}/slide10_continuum_gradient_preview.png", Inches(0.6), Inches(3.6), Inches(12.1), Inches(3.5))
b.add_notes(s, "20s", "8:35", "3 bullets (réponse + implication) en haut, schéma continuum (réutilisé) en dessous", ["Réponse directe : Mistral = open weight, pas open source", "Aller vite, le twist S21 porte l'impact"], ["conclusion", "open weight", "continuum"])

# ============================================================
# SLIDE 21 : Twist final
# ============================================================
s = b.add_slide()
b.add_title(s, "Mais attends…", size=36)
b.add_image_fit(s, f"{BASE}/slide21_carte_rgpd_preview.png", Inches(0.6), Inches(1.5), Inches(12.1), Inches(5.5))
b.add_notes(s, "40s", "9:15", "Titre « Mais attends… » + schéma 2 colonnes (Ollama USA vs Infomaniak Suisse) pleine largeur", ["Ollama Cloud = infra USA, transfert hors UE (RGPD art. 44)", "Infomaniak (Suisse) = RGPD ok mais catalogue restreint (8 modèles, dont Apertus)", "Large choix OU souveraineté, rarement les deux", "TON : léger, ironique — « Eh merde… »", "Ne pas précipiter, slide dense"], ["twist", "RGPD", "Infomaniak", "dilemme"])

# ============================================================
# SLIDE 22 : Questions
# ============================================================
s = b.add_slide()
b.add_title(s, "Questions ?", size=40)
b.add_notes(s, "15s", "9:30", "Titre « Questions ? » seul", ["Fin de présentation"], ["questions", "fin"])

# ============================================================
b.save_and_convert_to_odp(FINAL_OUT)
