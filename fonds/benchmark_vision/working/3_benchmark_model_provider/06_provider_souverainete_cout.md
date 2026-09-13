---
title: "Provider, souveraineté et coût"
status: "analyse en cours"
---

# Provider, souveraineté et coût

## Ollama Cloud

Points appréciés dans cette expérimentation :

- choix de modèles plus large que celui actuellement utilisé chez Infomaniak ;
- accès à de nombreux modèles open weight ;
- possibilité d'utiliser de gros modèles sans GPU local ;
- tarification perçue comme particulièrement intéressante dans certains créneaux et
  pour certains modèles.

Point de vigilance identifié :

- localisation de l'inférence et conséquences pour l'envoi de données personnelles.

**Sourcé le 2026-09-13** (voir `annexes/sources/providers/ollama-cloud.md`) :
infrastructure principalement hébergée aux États-Unis, avec débordement
possible vers l'UE et Singapour selon la charge ; prompts et réponses non
conservés ni utilisés pour l'entraînement ; facturation par abonnement
(Pro : 20 $/mois, 60 $ de crédits inclus) avec tarif par token propre à
chaque modèle au-delà.

## Infomaniak

Intérêts dans le cadre du projet :

- provider déjà envisagé pour des choix de souveraineté ;
- Gemma 4 31B produit de très bons résultats dans le corpus ;
- alternative intéressante lorsque la nature des données rend le provider plus
  important que la télémétrie avancée.

Limite observée pour l'expérience présente :

- pas de `reasoning` séparé comparable à celui exploité avec GLM/Ollama.

**Sourcé le 2026-09-13** (voir `annexes/sources/providers/infomaniak.md`) :
data centers en Suisse, conformité RGPD/LPD confirmée, prompts non conservés
ni utilisés pour l'entraînement — confirmé à la fois par la page officielle
et par un appel direct à l'API catalogue (`/openai/v1/models`), qui liste
bien `google/gemma-4-31B-it` et `moonshotai/Kimi-K2.6` à la date du benchmark.

## Azure

GPT-5.4-mini sert de référence de qualité et de rapidité dans la campagne
actuelle — utilisé « par acquis de conscience » pour situer les VLM ouverts
par rapport à un propriétaire, pas comme candidat de production : David reste
porté sur Infomaniak et Ollama pour les choix de souveraineté.

Son intérêt ne préjuge pas du choix de production : le benchmark technique et la
décision de déploiement sont deux étapes différentes.

## Coût sourcé (2026-09-13)

Tarifs par million de tokens (voir `annexes/sources/providers/` pour le détail
et les sources) :

| Couple | Entrée | Sortie |
| --- | --- | --- |
| GPT-5.4-mini / Azure | 0,75 $ | 4,50 $ |
| Gemma 4 31B / Ollama | 0,14 $ | 0,40 $ |
| Gemma 4 31B / Infomaniak | 0,20 CHF | 0,40 CHF |
| GLM-5.3-Flash / Ollama | 0,15 $ | 0,50 $ |
| Kimi K2.6 / Infomaniak | 0,60 CHF | 3,00 CHF |

Coût estimé pour 1000 pages, à partir des tokens/page mesurés dans
`04_resultats.md` (25 pages, sauf Kimi : voir note) :

| Couple | Tokens entrée/page | Tokens sortie/page | Coût / 1000 pages |
| --- | ---: | ---: | ---: |
| Gemma 4 31B / Ollama | 381,92 | 595,52 | 0,29 $ |
| Gemma 4 31B / Infomaniak | 376,92 | 608,76 | 0,32 CHF |
| GLM-5.3-Flash / Ollama | 8 071,32 | 2 511,52 | 2,47 $ |
| GPT-5.4-mini / Azure | 1 166,92 | 554,92 | 3,37 $ |
| Kimi K2.6 / Infomaniak* | 4 283 | 5 784,3 | 19,92 CHF |

\* Kimi K2.6 n'a été mesuré que sur les 10 pages du corpus cuisine (pas les
25 pages agrégées) — chiffre non strictement comparable en base, mais l'écart
d'ordre de grandeur (~7x plus cher que GLM, ~68x plus cher que Gemma) confirme
le constat qualitatif déjà posé dans `08_kimi_benchmark_optionnel.md`.

CHF et $ sont proches de la parité en 2026 ; l'ordre de grandeur des
comparaisons ci-dessus n'est pas affecté par cette approximation.

**Conclusion chiffrée** : Gemma 4 31B reste, aux deux providers, l'option la
moins chère d'un ordre de grandeur par rapport à GLM et Kimi — ce qui rend le
cas d'omission silencieuse (`3_benchmark_model_provider/05_meme_modele_deux_providers.md`)
d'autant plus critique à trancher : c'est le seul point qui empêche Gemma
d'être un choix évident sur le seul critère du coût.

## Coût : ne pas regarder uniquement €/1000 pages

Le coût utile est plutôt :

```text
coût pour obtenir 1000 pages acceptées
au niveau de qualité attendu
```

Un moteur très bon marché qui déclenche de nombreuses relectures ou un second passage
peut être moins intéressant qu'il n'y paraît.

À l'inverse, un moteur plus cher mais capable de détecter efficacement ses cas à
risque peut réduire le coût global.

C'est précisément l'hypothèse qui motive l'expérience GLM.
