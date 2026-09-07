# Veille — Mistral est-il vraiment open source ?

Veille sur la distinction open weight / open source / standards ouverts en IA
générative. Point de départ : une vidéo YouTube d'Anaïs distinguant poids,
code d'entraînement et données. Angle titre : le vocabulaire « open source »
est souvent employé à tort (Llama, Mistral, DeepSeek qualifiés d'« open
source » alors qu'ils ne satisfont pas les critères stricts).

## État actuel (2026-09-07)

Tout est encore en `working/` — rien basculé en `final/`.

## Contenu

- `working/Fiche de veille — IA _ de l'API fermée à l'Open Source.md` —
  document principal : 4 libertés du logiciel libre (Stallman/FSF), standards
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

- **Refonte du document principal** pour intégrer l'angle AI Act /
  trois définitions d'« open source » — décidé, pas encore fait.
- Vérifier les URLs restantes (échantillon partiel vérifié pour l'instant).
- Basculer en `final/` une fois la refonte faite, en respectant le format à
  deux rôles du dépôt (ODP support live / MD-ODT document de partage).
