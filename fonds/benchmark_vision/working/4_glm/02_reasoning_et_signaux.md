---
title: "Reasoning et signaux de qualité"
status: "hypothèse"
---

# Reasoning et signaux de qualité

## Informations observées dans les logs

Le reasoning peut contenir des observations sur :

- type ou nature du document ;
- titre ou en-tête ;
- numéro de page ;
- position d'un numéro ;
- césures ;
- zones illisibles ;
- hésitations ;
- parasites ;
- bleed-through ;
- éléments ignorés ;
- reconstruction ;
- structure visuelle.

## Première tentative : regex et mots-clés

Le prototype extrait actuellement certains signaux avec des mots-clés :

```yaml
dehyphenation_applied:
uncertain_reading:
omission_suspected:
reconstruction_detected:
```

Cette approche est insuffisante.

Exemple :

```text
No line-end hyphenation visible
```

Une simple recherche du mot `hyphenation` peut produire :

```yaml
dehyphenation_applied: true
```

alors que le reasoning dit précisément l'inverse.

Même problème pour :

```text
recipe number
```

vs

```text
page number
```

## Piste

Utiliser un LLM texte plus léger pour interpréter sémantiquement le reasoning et
produire un JSON strict.

Candidat expérimental envisagé :

```text
gpt-oss:20b
```

Son rôle ne serait pas de refaire l'OCR, mais d'interpréter le texte déjà produit par
GLM.
