---
title: "Prompts utilisés"
status: "historique du benchmark"
---

# Prompts

## Benchmark général

Le prompt général transmis aux VLM dans la campagne fournie était :

```text
Tu transcris la page d'un livre scannée en Markdown propre.
Respecte l'ordre de lecture visuel (une mise en page en colonnes doit être lue
colonne par colonne, dans l'ordre où un lecteur humain la lirait).
Marque les titres avec '## '. Ignore les éléments purement décoratifs
(chiffres stylisés, icônes, filigranes). Réponds uniquement avec le Markdown,
sans commentaire ni explication.
```

Ce prompt appartient à l'historique du benchmark et doit être conservé tel quel
lorsqu'on interprète les résultats.

## Prompt GLM expérimental

Le pipeline GLM approfondi utilise un prompt différent, destiné à provoquer une
analyse interne exploitable séparément du contenu final :

```text
Tu transcris cette page scannée en Markdown propre.

Respecte strictement le texte principal visible et son ordre de lecture.

Pendant ton analyse, identifie notamment :
- le titre courant ou l'en-tête ;
- le numéro de page ;
- la position du numéro de page ;
- les éventuelles césures de fin de ligne ;
- les zones ambiguës, illisibles ou parasites.

Ces éléments servent uniquement à ton analyse interne.

Dans la réponse finale :
- retourne uniquement le texte principal transcrit ;
- n'ajoute aucun commentaire ;
- n'ajoute aucune section "Transcription" ;
- n'ajoute aucune section de métadonnées ;
- n'inclus pas l'en-tête courant ;
- n'inclus pas le numéro de page ;
- rétablis les mots coupés artificiellement en fin de ligne ;
- ne résume pas ;
- n'invente pas ;
- ne complète pas ce qui n'est pas lisible.
```

## Attention méthodologique

Le benchmark général et l'expérience GLM ne sont donc **pas strictement la même
expérience**.

Le premier compare plusieurs moteurs.

Le second cherche à déterminer si le reasoning exposé par GLM peut devenir un signal
de contrôle qualité. Il doit être analysé comme une expérimentation dédiée, et non
fusionné naïvement avec le classement général.
