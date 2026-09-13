---
title: "Sources — Ollama Cloud"
consulted: "2026-09-13"
---

# Ollama Cloud — sources primaires

## Localisation de l'inférence

> Ollama hosts models and compute resources primarily in the United States,
> and to serve global demand, may route to Europe and Singapore for
> additional capacity.

Source : [Cloud models · Ollama Blog](https://ollama.com/blog/cloud-models)
(consulté le 2026-09-13).

Confirme le point de vigilance déjà noté dans
`2_qui_est_ce/04_ouverture_et_souverainete.md` : l'infrastructure est
principalement américaine, avec un débordement possible vers l'UE et
Singapour selon la charge. `docs.ollama.com/cloud` (documentation technique
d'usage) ne mentionne pas cette information — seule la page blog l'indique.

## Politique de données

> Ollama's cloud does not retain your data to ensure privacy and security.
> Prompt or response data is never logged or trained on.

Source : [Cloud - Ollama](https://docs.ollama.com/cloud) et
[Cloud models · Ollama Blog](https://ollama.com/blog/cloud-models)
(consultés le 2026-09-13).

## Tarification

Modèle de facturation : abonnement mensuel avec crédits d'usage inclus,
consommés au tarif par million de tokens propre à chaque modèle (pas un
forfait illimité). Source : [Pricing · Ollama](https://ollama.com/pricing)
(consulté le 2026-09-13).

| Offre | Prix / mois | Crédits inclus | Concurrence |
| --- | --- | --- | --- |
| Free | 0 $ | quota de démarrage | 1 requête |
| Pro | 20 $ | 60 $ d'usage | 3 requêtes |
| Max | 100 $ | 300 $ d'usage | 10 requêtes |
| Team | 500 $ | 1000 $ d'usage partagés | 10 requêtes |

Le catalogue précise que l'abonnement Pro utilisé pour cette veille (déjà
noté dans `fonds/mistral_est_il_vraiment_opensource_2026-09-09/working/catalogue_ollama_pro_classification.md`)
donne accès au catalogue complet de modèles ouverts.

### Tarifs par modèle utilisés dans le benchmark

| Modèle | Entrée ($/M tok) | Entrée cache ($/M tok) | Sortie ($/M tok) | Source |
| --- | --- | --- | --- | --- |
| GLM-5.3-Flash | 0,15 | 0,03 | 0,50 | [ollama.com/library/glm-5.3-flash:cloud](https://ollama.com/library/glm-5.3-flash:cloud) |
| Gemma 4 31B | 0,14 | 0,05 | 0,40 | [ollama.com/library/gemma4:31b-cloud](https://ollama.com/library/gemma4:31b-cloud) |
| Kimi K2.6 | 0,95 | 0,16 | 4,00 | [ollama.com/library/kimi-k2.6:cloud](https://ollama.com/library/kimi-k2.6:cloud) |

Consulté le 2026-09-13. Ces tarifs sont cohérents avec ceux déjà utilisés
(convertis en EUR) dans `annexes/benchmark/comparatif_ocr_llm_calc_.xlsx`.

## Catalogue et filtre « vision »

Le catalogue Ollama expose un filtre par capacité (`ollama.com/search?c=vision`)
qui liste les modèles multimodaux disponibles, combinable avec d'autres tags
(`thinking`, `tools`, `cloud`). Ce filtre opérationnalise directement la
première question du « Qui est-ce ? » (`2_qui_est_ce/01_principe.md`) :
multimodalité, sans avoir à vérifier modèle par modèle.

Relevé du 2026-09-13 : le filtre liste notamment `glm-5.3-flash`, `gemma4`,
`kimi-k2.6`, `kimi-k2.7-code`, `kimi-k3` (ces trois derniers portant aussi le
tag `thinking`), ainsi que des candidats non encore considérés dans cette
veille — `glm-ocr` (modèle dédié OCR), `medgemma` / `medgemma1.5`,
`minicpm-v4.6` / `minicpm-v4.5`. À faire passer par le filtre « Qui est-ce ? »
si la campagne se poursuit.
