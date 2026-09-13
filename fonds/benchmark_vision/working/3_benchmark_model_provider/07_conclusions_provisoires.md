---
title: "Conclusions provisoires du benchmark général"
status: "provisoire"
---

# Conclusions provisoires

## Il n'y a pas de vainqueur unique

La campagne actuelle permet surtout de distinguer plusieurs profils.

### Pour la vitesse et la robustesse brute

GPT-5.4-mini est très performant dans les mesures actuelles.

### Pour un compromis économique

Gemma 4 31B est particulièrement intéressant. Son comportement doit toutefois être
contrôlé à cause du cas d'omission silencieuse observé.

### Pour la souveraineté

Le provider devient un critère de premier ordre. Le même modèle peut être disponible
dans plusieurs environnements sans offrir les mêmes garanties, coûts ni paramètres.

### Pour la structure et la télémétrie

GLM attire l'attention par sa restitution et surtout par l'exposition séparée du
`reasoning`, au prix d'une consommation et d'une latence beaucoup plus élevées.

## Le résultat méthodologique le plus fort

Le benchmark ne compare pas seulement des modèles.

Il compare des **solutions d'inférence réelles** :

```text
modèle + provider + configuration + prompt
```

Le cas Gemma/Infomaniak vs Gemma/Ollama l'illustre directement.

## Pourquoi poursuivre avec GLM

GLM n'est pas retenu parce qu'il « gagne » le benchmark.

Il est approfondi parce qu'il permet de tester une autre question :

> Peut-on transformer le reasoning et les métriques d'un VLM en signaux permettant de
> repérer les pages à risque et de réserver un second VLM aux cas suspects ?

La section suivante documente cette hypothèse.
