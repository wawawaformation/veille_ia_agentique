---
title: "Correspondance avec les compétences C6, C7 et C8"
status: "repère certification"
---

# Correspondance avec le référentiel

La veille est conduite d'abord pour répondre à un besoin technique réel. Elle fournit
néanmoins naturellement des preuves pour le bloc de compétences portant sur
l'intégration de services d'intelligence artificielle.

Pour le texte officiel (savoir-faire, critères de performance/réussite,
modalité d'évaluation E2), voir `referentiel-c6-c7-c8.md` à la racine du dépôt — ce
document-ci n'en est que l'application concrète à cette veille.

## C6 — Veille technique et réglementaire

La démarche couvre notamment :

- définition d'une thématique ;
- identification et qualification des sources ;
- collecte et synthèse d'informations ;
- partage de la veille ;
- prise en compte de l'accessibilité, de la sécurité et de la gestion des données ;
- maintien d'une recommandation en phase avec l'état de l'art.

### Preuves possibles dans ce dossier

- sources primaires et secondaires ;
- synthèses sur VLM, open source/open weight et souveraineté ;
- présentation finale de veille ;
- historique des décisions.

## C7 — Identifier un service d'IA par benchmark

C'est le cœur des dossiers `2_qui_est_ce/` et `3_benchmark_model_provider/`.

Le dossier documente :

- expression du besoin ;
- contraintes ;
- services étudiés ;
- services écartés avant test et motifs ;
- benchmark ;
- avantages et limites ;
- contraintes techniques ;
- critères de souveraineté et d'éco-responsabilité lorsque l'information est
  disponible ;
- recommandations provisoires.

Le cas « Gemma 4 31B chez deux providers » renforce la nécessité de comparer des
services réels et non uniquement des noms de modèles.

## C8 — Paramétrer un service d'IA

Le dossier `4_glm/` apporte une mise en œuvre concrète :

- accès au service Ollama Cloud ;
- configuration du modèle ;
- prompt ;
- script Python ;
- traitement des images ;
- récupération des réponses ;
- métriques ;
- logs ;
- analyse du reasoning ;
- documentation du prototype.

Le service est réellement appelé et les sorties sont auditées.

## Point d'attention

Ne pas réorganiser artificiellement toute la veille « pour cocher le référentiel ».

La correspondance C6–C7–C8 est une **lecture de preuves** produites par une démarche
technique réelle.
