---
title: "Hypothèses GLM à tester"
status: "non démontré"
---

# Hypothèses

## H1 — Le reasoning contient des signaux prédictifs

Certaines erreurs ou pages difficiles sont accompagnées d'hésitations, de corrections
ou d'un reasoning inhabituellement long.

**À démontrer**, pas à supposer.

## H2 — La longueur du reasoning est utile

Hypothèse :

```text
reasoning inhabituellement long
        ↓
probabilité de page difficile plus élevée
```

Test attendu : corrélation avec une vérité terrain, par type de document.

## H3 — Un LLM texte peut interpréter le reasoning

`gpt-oss:20b` pourrait convertir le reasoning en JSON fiable, notamment pour gérer
les négations et distinguer des concepts proches.

Il faut mesurer :

- exactitude des métadonnées ;
- précision/rappel des alertes ;
- coût ;
- latence ;
- stabilité.

## H4 — La cascade coûte moins qu'un double OCR

À comparer :

```text
A. VLM A + VLM B sur toutes les pages

B. GLM
   + contrôleur texte
   + VLM B seulement sur les pages suspectes
```

L'intérêt doit être démontré en coût **et** en qualité.

## H5 — Un seul pipeline convient aux livres et au Web

Ce n'est pas acquis.

Les métriques et seuils pourraient devoir être différents entre :

- OCR documentaire ;
- analyse d'interface.
