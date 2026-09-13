---
title: "Constats et limites de l'expérience GLM"
status: "provisoire"
---

# Constats

## Cuisine

GLM récupère correctement le bloc d'ingrédients qui avait disparu dans la sortie
Gemma/Ollama du cas de référence.

Des erreurs OCR réelles subsistent néanmoins.

Le rapport d'expérimentation relève par exemple une page où :

```text
flambe      → flamble
apportant   → important
```

La page concernée provoque également un reasoning long. Cela constitue un **indice**,
pas une preuve, d'un lien possible entre hésitation et risque d'erreur.

## Le Capital

Le comportement est globalement solide sur les pages textuelles.

Certaines pages difficiles produisent un reasoning beaucoup plus long et davantage
d'hésitations.

## Web

GLM ne se contente pas de lire des caractères : il décrit et reconstruit la structure
de l'interface.

Cette capacité est prometteuse pour QualiCheck, mais modifie la nature du benchmark :
une analyse d'interface ne doit pas être notée exactement comme une transcription
documentaire.

# Limites

## Le reasoning n'est pas une preuve

Le modèle peut mal interpréter la page tout en produisant un commentaire assuré.

## Longueur du reasoning

La corrélation avec le risque d'erreur n'est pas démontrée.

Elle doit être mesurée sur une vérité terrain et non déduite de quelques exemples.

## Extraction actuelle

Les regex et mots-clés sont le maillon faible du prototype.

## Métadonnées

Un grand numéro de recette a déjà été confondu par le code d'extraction avec un numéro
de page, alors que le reasoning faisait la distinction.

## Nommage des fichiers

Le prototype utilisait le numéro de page détecté pour nommer la sortie. Cela a produit
un fichier `page_011` pour une source différente.

La source doit rester l'identifiant technique du fichier ; les métadonnées détectées
ne doivent pas modifier son nom.
