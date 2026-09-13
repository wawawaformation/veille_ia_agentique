---
title: "Contrôleur du reasoning"
status: "à prototyper"
---

# Contrôleur du reasoning

## Objectif

Transformer le reasoning brut en données structurées utiles à une décision de qualité.

Exemple de sortie cible :

```json
{
  "document_type": "book_page",
  "page": null,
  "recipe_number": 11,
  "page_number_position": null,
  "dehyphenation_applied": false,
  "uncertain_reading": false,
  "omission_suspected": false,
  "confidence": 0.0
}
```

## Few-shot à préparer

Cas réels à utiliser :

- bon OCR ;
- omission complète ;
- faux positif ;
- ambiguïté réelle ;
- texte secondaire volontairement ignoré ;
- numéro de recette ≠ numéro de page ;
- absence réelle de césure ;
- césure reconstruite ;
- capture web ;
- entrée hors domaine.

## Évaluation

Le contrôleur ne doit pas être noté sur la qualité de son style.

Mesures prioritaires :

- précision des alertes ;
- rappel des pages réellement problématiques ;
- taux de fallback déclenché ;
- coût supplémentaire ;
- latence supplémentaire.
