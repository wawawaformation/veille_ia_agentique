---
title: "Ouverture, open weight et souveraineté"
status: "cadre d'analyse"
---

# Ouverture et souveraineté

## Ne pas confondre les niveaux

La veille distingue au minimum :

### Logiciel libre

Le code du logiciel est distribué sous une licence libre.

### Modèle open source

L'emploi du terme doit être réservé aux modèles qui répondent réellement au cadre
d'ouverture revendiqué et dont les éléments nécessaires sont effectivement ouverts.

### Modèle open weight

Les poids sont disponibles sous une licence donnée, mais cela ne signifie pas
automatiquement que l'ensemble du modèle, des données et du processus d'entraînement
est « open source ».

### Provider cloud

Le provider exécute le modèle. Sa juridiction, son infrastructure, sa politique de
données, ses tarifs et ses paramètres d'inférence constituent une couche distincte.

## Position actuelle dans cette veille

GLM est classé **open weight** — confirmé et sourcé le 2026-09-13 : licence
MIT, poids publiés par Zhipu AI (Z.ai) le 26 août 2026, 320B paramètres
totaux / 18B actifs (`annexes/sources/models/glm-5.3-flash.md`). MIT est
l'une des licences de poids les plus permissives, mais cela ne change pas la
classification open weight/open source : rien n'indique que les données et
le code d'entraînement complets soient publiés.

Gemma 4 31B est également open weight, sous licence Apache 2.0 depuis Gemma 4
(2 avril 2026) — rupture avec les Gemma Terms of Use restrictives des
générations précédentes (`annexes/sources/models/gemma-4-31b.md`). Kimi K2.6
est open weight sous licence Modified MIT, avec obligation de crédit visible
au-delà d'un seuil d'usage commercial (`annexes/sources/models/kimi-k2.6.md`).

Ollama Cloud présente plusieurs intérêts pratiques pour l'expérimentation :

- catalogue de modèles large ;
- présence de nombreux modèles open weight ;
- inférence distante adaptée à l'absence de GPU local ;
- tarification jugée attractive dans l'usage observé.

Point de vigilance identifié par l'auteur, confirmé et sourcé le 2026-09-13 :
l'infrastructure est principalement hébergée aux États-Unis, avec débordement
possible vers l'UE et Singapour selon la charge — prompts et réponses non
conservés ni utilisés pour l'entraînement (`annexes/sources/providers/ollama-cloud.md`).

Conséquence de conception envisagée : **ne pas envoyer de données personnelles sans
cadre adapté et informer l'utilisateur avant l'utilisation de la vision**.

Infomaniak dispose notamment de Gemma 4 31B, jugé très bon dans ce benchmark, avec
un contexte de souveraineté plus favorable au projet, mais sans la sortie de
`reasoning` séparée qui motive l'expérimentation GLM. Confirmé le 2026-09-13
par un appel direct à l'API catalogue d'Infomaniak (`google/gemma-4-31B-it`
et `moonshotai/Kimi-K2.6` bien présents), data centers en Suisse, conformité
RGPD/LPD (`annexes/sources/providers/infomaniak.md`).

## Principe de décision

Le meilleur résultat brut n'est pas nécessairement le meilleur choix de production.

La décision finale doit pouvoir distinguer :

```text
meilleur résultat technique
          ≠
meilleur compromis de déploiement
```
