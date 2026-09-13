# Annexes à compléter manuellement

Les sous-dossiers sont préparés mais les fichiers bruts ne sont volontairement pas
dupliqués dans cette archive.

## `corpus/`

À déplacer ici :

- PDF / images du corpus cuisine ;
- PDF / images de *Le Capital* ;
- captures Web utilisées dans les tests.

## `benchmark/`

À déplacer ici :

- `benchmark.zip` décompressé ou son contenu utile ;
- `comparatif_ocr_llm_calc_.xlsx` ;
- tableaux complémentaires ;
- éventuelles sorties Kimi si elles doivent rester dans l'historique.

## `glm/logs/`

À déplacer ici :

- contenu de `logs(1).zip` ;
- reasonings bruts ;
- réponses API.

## `glm/output/`

À déplacer ici :

- contenu de `output(1).zip`.

## `glm/scripts/`

À déplacer ici :

- `test_glm_vision.py` ;
- `run_corpus.sh` ;
- futures versions du contrôleur.

## `schemas/`

- `pipeline_ocr_reasoning_v5_lisible.drawio.png` — déplacé le 2026-09-13.
  Source `.drawio` non déplacée : le seul fichier `.drawio` retrouvé
  (`pipeline_ocr_temporaire_v2.drawio`, nommé « Pipeline OCR temporaire »)
  correspond à une itération antérieure (v2), pas à ce PNG (v5) — pas de
  source vectorielle fiable pour l'instant.
- futurs schémas du logiciel : à déplacer ici au fil de l'eau.

## `sources/`

- `models/` — licence, architecture et statut d'ouverture de chaque modèle
  benchmarké (GLM-5.3-Flash, Gemma 4 31B, Kimi K2.6), sourcés le 2026-09-13.
  GPT-5.4-mini (propriétaire, pas de fiche de licence) est couvert dans
  `providers/azure.md`.
- `providers/` — localisation de l'inférence, politique de données et
  tarifs par token pour Ollama Cloud, Infomaniak et Azure, sourcés le
  2026-09-13.

Reste à déplacer ici : référentiel Simplon / RNCP utilisé (actuellement à la
racine du dépôt, `referentiel-c6-c7-c8.md`).

## Règle

Les informations susceptibles de changer (tarifs, disponibilité des modèles,
localisation, conditions de service) doivent être accompagnées d'une source primaire
et d'une date de consultation.
