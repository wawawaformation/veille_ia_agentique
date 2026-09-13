---
title: "Intégration future dans QualiCheck US2"
status: "conception à venir"
---

# Intégration Vision dans QualiCheck

## À ne pas concevoir trop tôt

La veille doit d'abord déterminer :

- quel VLM ou quels VLM sont retenus ;
- dans quels cas ;
- avec quelles garanties ;
- quel niveau de structure est réellement utile au RAG Opquast.

## Routing possible à étudier

```text
URL
 ├── HTML / DOM
 ├── parsing statique
 └── Playwright si nécessaire

Image / capture
 └── outil Vision
      ↓
 contexte visuel structuré
      ↓
 RAG Opquast
```

Les deux chemins pourront ensuite être combinés lorsqu'une URL et une capture sont
disponibles.

## Données personnelles

Avant tout appel vers un provider dont la localisation ou la politique de données
l'exige :

- informer explicitement l'utilisateur ;
- lui demander de ne pas envoyer de données personnelles/confidentielles ;
- envisager un masquage local avant transfert ;
- éventuellement proposer un provider alternatif selon le niveau de confidentialité.

## Souveraineté

Un futur écran de configuration pourrait distinguer plusieurs modes, mais aucune UX
ne doit être figée tant que les providers réellement retenus et leurs conditions ne
sont pas établis.
