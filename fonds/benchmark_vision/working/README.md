---
title: "Veille OCR / VLM — numérisation, vision et modèles multimodaux"
date: "2026-09"
status: "travail en cours"
---

# Veille OCR / VLM

## Pourquoi cette veille existe

Cette veille a un double objectif.

Le premier est **opérationnel** : faire avancer la conception d'un futur logiciel de
numérisation de livres anciens. Le besoin vient d'un cas réel dans l'entourage de
l'auteur : transformer des scans parfois difficiles en texte fidèle, structuré et
réutilisable, sans devoir disposer d'un GPU local.

Le second est **pédagogique et professionnel** : documenter une démarche de veille
technique qui pourra être présentée, notamment dans le cadre des compétences C6, C7
et C8 du référentiel « Développeur en intelligence artificielle ».

Un second cas d'usage est apparu en cours de travail : **QualiCheck US2**, qui doit
pouvoir analyser une capture d'écran ou une maquette avant d'interroger les règles
Opquast pertinentes.

## Fil conducteur

La démarche ne part pas d'un modèle à défendre.

```text
besoin réel
   ↓
pré-sélection des candidats — « Qui est-ce ? »
   ↓
benchmark modèle + provider
   ↓
constats techniques
   ↓
approfondissement d'une propriété particulière de GLM
   ↓
hypothèses à valider
   ↓
conception future
```

Le dossier `4_glm/` ne signifie donc pas que GLM est définitivement retenu. Il
documente une piste expérimentale née du benchmark : l'API utilisée expose
séparément `content`, `reasoning` et `usage`, ce qui pourrait permettre de construire
un contrôle qualité avant déclenchement d'un fallback.

## Deux notions à ne pas confondre

Cette veille distingue volontairement :

- **le modèle** : ses capacités, son ouverture, sa taille, sa multimodalité ;
- **le provider** : l'infrastructure qui exécute le modèle, ses tarifs, ses paramètres,
  sa localisation et ses règles de traitement des données.

Un résultat important du benchmark est justement que **le même modèle nominal,
Gemma 4 31B, n'a pas produit exactement la même sortie chez Ollama et chez
Infomaniak**.

## Organisation

```text
1_besoin/
    Les problèmes concrets auxquels la veille doit répondre.

2_qui_est_ce/
    Pré-sélection des modèles avant benchmark, sur le principe du jeu « Qui est-ce ? ».

3_benchmark_model_provider/
    Protocole, corpus, prompts, résultats et comparaison des couples modèle/provider.

4_glm/
    Approfondissement du reasoning exposé par GLM et hypothèse de pipeline qualité.

5_reste_a_faire/
    Ce qui n'est pas démontré et doit être testé avant une conception détaillée.

annexes/
    Emplacements préparés pour les fichiers bruts à déplacer manuellement.
```

## Posture

Le but n'est pas de désigner un « meilleur VLM » universel. Le choix dépend du
besoin : fidélité OCR, structure visuelle, coût, latence, souveraineté, possibilité
d'exécution locale, confidentialité des données et réversibilité.

Les affirmations commerciales, de licence, de localisation d'inférence et de
politique de données devront être reliées à des **sources primaires datées** avant la
version destinée à la présentation.
