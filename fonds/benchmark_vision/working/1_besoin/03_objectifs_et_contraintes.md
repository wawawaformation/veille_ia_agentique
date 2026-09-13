---
title: "Objectifs et contraintes de la veille"
status: "cadre"
---

# Objectifs et contraintes

## Question générale

> Peut-on aujourd'hui construire un pipeline de transcription et d'analyse visuelle
> suffisamment fiable, économique et maîtrisable pour la numérisation de livres
> anciens, tout en réutilisant une partie de ces travaux pour l'analyse de captures
> dans QualiCheck ?

## Contraintes techniques

- Pas de GPU local adapté aux gros VLM.
- L'inférence cloud est donc acceptable pour l'expérimentation.
- Le coût doit rester raisonnable pour un traitement page par page à volume élevé.
- Les modèles multimodaux trop lourds pour l'usage visé peuvent être éliminés avant
  benchmark.
- La sortie doit être exploitable en Markdown.
- La latence compte, mais n'est pas le seul critère.

## Contraintes de qualité

- Ne pas confondre fidélité OCR et correction éditoriale.
- Ne pas récompenser une sortie « jolie » si elle omet une information.
- Distinguer erreur visible et omission silencieuse.
- Évaluer séparément la structure documentaire.
- Pour le Web, distinguer OCR strict et analyse d'interface.

## Contraintes de souveraineté et d'ouverture

La veille accorde une importance particulière :

- au logiciel libre ;
- aux modèles open source lorsqu'ils le sont réellement ;
- aux modèles open weight, sans les présenter abusivement comme open source ;
- à la possibilité de changer de provider ;
- à la possibilité théorique d'exécuter les poids ailleurs ;
- à la juridiction et à la localisation de l'inférence ;
- à la politique de conservation des requêtes ;
- à la nature des données envoyées.

**Ouverture du modèle et souveraineté du provider sont deux dimensions distinctes.**

Un modèle open weight exécuté dans un cloud étranger reste un traitement réalisé
dans l'infrastructure de ce provider.
