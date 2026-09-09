# Veille — Mistral est-il vraiment open source ?

Veille sur la distinction open weight / open source / standards ouverts en IA
générative. Point de départ : une vidéo YouTube d'Anaïs distinguant poids,
code d'entraînement et données. Angle titre : le vocabulaire « open source »
est souvent employé à tort (Llama, Mistral, DeepSeek qualifiés d'« open
source » alors qu'ils ne satisfont pas les critères stricts).

## État actuel (2026-09-09) — veille terminée

Les trois livrables sont finalisés dans `final/` : ODP (support live),
`script_oral.pdf` (aide-mémoire personnel de présentation) et
`mistral_est_il_vraiment_opensource.pdf` (document de partage pour
lecture asynchrone). Présentation orale prévue le 2026-09-10 (10 min
cible, 9:30 réel calculé — 30s de marge). Dossier renommé
`mistral_est_il_vraiment_opensource_2026-09-09` le 2026-09-09, conforme à
la convention `nom_AAAA-MM-JJ` du `CLAUDE.md` racine.

Le contenu s'est restructuré en **4 blocs de présentation distincts**
(`presentation_bloc_1_logiciel_libre.md` à `presentation_bloc_4_ollama.md`)
plus un **plan de slides détaillé** (`plan_slides.md`, 22 slides, timing et
visuel précisés pour chacune) — c'est ce plan qui fait foi sur la structure
finale, pas la « Fiche de veille » originelle ci-dessous qui reste le
document source mais n'est plus la structure de présentation.

## Contenu

- `working/plan_slides.md` — **document de référence pour la présentation** :
  22 slides détaillées (texte, analogie, visuel, timing), 4 blocs + intro +
  fermeture, timing réel recalculé le 2026-09-08 (9:30, 30s de marge sous
  la cible de 10:00)
- `working/presentation_bloc_1_logiciel_libre.md` à
  `working/presentation_bloc_4_ollama.md` — le texte de présentation par bloc
  (bloc 4 contient aussi la conclusion générale et le twist RGPD/Infomaniak,
  pas seulement Ollama)
- `working/analogies_metaphores.md` — analogies orales par bloc (recette,
  USB, gâteau, eau contaminée, restaurant fermé, piscine)
- `working/bibliographie.md` — sources vérifiées (URLs récupérées réellement,
  y compris un appel API direct à Infomaniak par David le 2026-09-08)
- `working/images/` — 7 schémas `.drawio` (contrôlés visuellement via export
  PNG + `drawio` CLI) et `working/images/photos/` — 9 photos Unsplash +
  1 patchwork composite (USB) + 1 clipart SVG fait maison (disque dur) +
  1 image générée par IA (slide 1, chat + Pinocchio), crédits détaillés dans
  `photos/credits.md`. Il manque encore une capture d'écran de l'interface
  Ollama, à faire par David lui-même et à déposer sous
  `images/photos/slide19_ollama_screenshot.png` (nom attendu par
  `build_odp.py`).
- `working/build_odp.py` — script de contenu (22 slides codées en dur à
  partir de `plan_slides.md`) qui importe le module partagé
  `/projets/veille/outils/odp_builder.py` (voir CLAUDE.md racine, section
  « Outil partagé : génération d'ODP ») pour la construction pptx et la
  conversion réelle en `.odp` (filtre impress8, jamais un renommage).
  Régénérer avec `python3 build_odp.py` depuis un venv avec
  `python-pptx`/`Pillow` installés — le script écrit directement dans
  `final/`.
- `final/mistral_est_il_vraiment_opensource.odp` — **le livrable ODP**,
  généré le 2026-09-08 à partir de `build_odp.py`. Slide 19 affiche un
  placeholder texte tant que `slide19_ollama_screenshot.png` n'existe pas —
  régénérer une fois la capture ajoutée.
- `working/document_de_partage_redige.md` / `final/mistral_est_il_vraiment_opensource.pdf`
  — **document de partage rédigé**, destiné à une lecture asynchrone par
  les autres apprenants (prose complète et autonome, hiérarchie de titres
  continue, analogies en toutes lettres, sources en liens explicites) —
  écrit le 2026-09-08, déplacé un temps vers `working/` le 2026-09-09 le
  temps que le script oral (voir ci-dessous) devienne prioritaire, puis
  **réexporté en PDF le 2026-09-09** une fois le script oral achevé,
  redevenant un livrable actif à part entière. Contient le schéma manquant
  signalé par David (diagramme de Venn des 3 définitions d'« open source »,
  slide 14) et l'angle AI Act enrichi (articles 53/54, non-monétisation).
  Régénérer avec (depuis `final/`, important pour que les chemins d'image
  relatifs de `page_de_garde.tex` et du corps du document se résolvent
  correctement) :
  `pandoc ../working/document_de_partage_redige.md -o
  mistral_est_il_vraiment_opensource.pdf --pdf-engine=xelatex
  --include-in-header=/projets/veille/veille.tex
  --include-in-header=titre_entete.tex
  --include-before-body=page_de_garde.tex --toc -V lang=fr -V
  papersize=a4`.
- `working/script_oral.md` / `final/script_oral.pdf` — **le livrable
  actuel** : aide-mémoire pour la présentation orale, slide par slide.
  Format par section imposé par David le 2026-09-09 : titre exact de la
  slide (celui affiché sur l'ODP, pas un label improvisé), `**Durée**` et
  `**Fin de slide**` sur une ligne, puis le texte parlé — phrases
  complètes façon le document de partage mais condensées et orales, pas
  du télégraphique. Contenu reprend la substance de
  `document_de_partage_redige.md` (y compris l'angle AI Act enrichi :
  articles 53/54, non-monétisation) plutôt que de réinventer. En gros
  caractères pour être lu facilement pendant que David parle. Généré en
  `documentclass=extarticle`, `fontsize=17pt` (la classe `article`
  standard ne va pas au-delà de 12pt, `extarticle` du paquet `extsizes`
  est nécessaire pour 14/17/20pt), sans table des matières (inutile pour
  un document lu linéairement), **une slide par page** (`\newpage` LaTeX
  brut entre chaque section — cf. `working/correction_script_oral.md` du
  2026-09-09 pour l'historique des corrections de contenu appliquées).
  Réutilise `veille.tex` + `titre_entete.tex` pour la cohérence visuelle.
  Même piège que le document de partage : les
  caractères Unicode spéciaux (`≠`, `²⁵`) ne passent pas dans la police
  Latin Modern en gras du template — reformuler en toutes lettres (`n'est
  pas`) ou en LaTeX inline (`$10^{25}$`), jamais le caractère Unicode brut
  dans un titre de section. Régénérer avec :
  `pandoc script_oral.md -o ../final/script_oral.pdf --pdf-engine=xelatex
  --include-in-header=/projets/veille/veille.tex
  --include-in-header=../final/titre_entete.tex -V lang=fr -V
  papersize=a4 -V documentclass=extarticle -V fontsize=17pt` (depuis
  `working/`).
- `final/page_de_garde.tex` — fragment LaTeX injecté avant la table des
  matières (utilisé par le document de partage, pas par le script oral) :
  image de couverture (chat + Pinocchio, cf. slide 1 de l'ODP) + légende en
  guise de texte alternatif. Nécessaire car `--toc` s'insère automatiquement
  en tête du corps du document — une image mise en tête du `.md` atterrit
  donc APRÈS le sommaire, pas avant. Piège à ne pas répéter pour une
  prochaine veille.
- `final/titre_entete.tex` — surcharge le titre affiché en en-tête gauche
  du PDF (macro `\veilletitre`, valeur par défaut « Veille — Mini
  Manifest » dans `veille.tex` racine) par le vrai titre de cette veille.
  Un seul `\renewcommand`, à inclure en second, après `veille.tex`. Utilisé
  par le script oral ET par le document de partage si celui-ci est un jour
  ré-exporté.
- `working/Fiche de veille — IA _ de l'API fermée à l'Open Source.md` —
  document source originel : 4 libertés du logiciel libre (Stallman/FSF), standards
  ouverts, Open Source AI Definition de l'OSI (Use/Study/Modify/Share),
  continuum en 4 catégories, analogie culinaire (poids=plat,
  entraînement=recette, données=ingrédients)
- `working/veille_llm_continuum_ouverture_20_modeles.md` — fresque de 20 LLM
  répartis dans les 4 catégories du continuum, avec fiche par modèle
- `working/reglementaire_ai_act.md` — angle réglementaire AI Act : exemption
  open source (art. 2(12)), limite du risque systémique (seuil 10²⁵ FLOPs,
  cas Llama-3 405B), et surtout **trois définitions d'« open source » qui ne
  se recouvrent pas** (marketing / AI Act / OSAID) — plus-value par rapport
  à la seule vidéo de départ, relie directement au titre de la veille
- `working/LLMs/` — 20 mini-fiches modèle (une par `.md`), réparties en 4
  sous-dossiers correspondant aux catégories du continuum :
  - `ferme_api/` — GPT (famille, pas modèle précis), Claude (famille),
    Gemini 3.1 Pro, Grok 4.6, Amazon Nova 2 Pro
  - `open_weight/` — Llama 4 Maverick, Grok-1, Phi-4, Mixtral 8×7B, Mistral
    Medium 3.5
  - `open_weight_plus_plus/` — gpt-oss-120b, Gemma 4 31B, DeepSeek-R1,
    Qwen3-235B-A22B, Mistral Small 4
  - `open_source/` — Luciole-23B, OLMo 3 32B, Apertus 1.5 70B, Pythia-12B,
    Amber-7B

## Décisions prises

- **GPT et Claude en fiche « famille »**, pas modèle précis (contrairement
  aux autres) : montre que le choix fermé/ouvert est une stratégie
  d'entreprise, pas une propriété d'un modèle isolé.
- **Réglementaire retenu, frugalité/carbone en mention légère seulement** —
  pas d'angle dev durable à forcer, le lien thème Mini Manifest n'a pas
  besoin d'être rendu explicite (veilles plus libres désormais).
- **URLs vérifiées par récupération réelle** le 2026-09-07 (WebFetch) sur un
  échantillon des sources primaires — cf. piège déjà noté dans le
  `CLAUDE.md` racine du dépôt sur la vérification des sources. OpenAI bloque
  WebFetch (403) sur ses pages produit ; les autres sources testées
  (Anthropic, Google DeepMind, GitHub, HuggingFace, Mistral, Apertus) sont
  confirmées valides et cohérentes avec le contenu des fiches.

## Reste à faire

- **Capture d'écran Ollama** (interface + catalogue + 3 modes) — à faire par
  David (a l'abonnement Cloud Pro), déposer sous
  `images/photos/slide19_ollama_screenshot.png`, puis relancer
  `python3 working/build_odp.py` pour régénérer `final/*.odp`.
- Voix haute du bloc 3 (le plus dense, mélange réglementaire + physique
  énergétique) et du twist final (bloc 4, slide 21 — ton « léger, ironique »
  à caler).
- Vérifier les URLs restantes de la « Fiche de veille » originelle
  (échantillon partiel vérifié le 2026-09-07 uniquement).
