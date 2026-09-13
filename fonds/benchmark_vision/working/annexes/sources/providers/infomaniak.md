---
title: "Sources — Infomaniak AI Tools"
consulted: "2026-09-13"
---

# Infomaniak — sources primaires

## Localisation et souveraineté

> The AI and GPU services are powered from data centers located in
> Switzerland, with no dependence on foreign players. [...] Infomaniak
> guarantees full compliance with the FADP and GDPR. [...] Customer prompts
> and data are not used to train models and are processed under Swiss law.

Source : [GDPR compliance & data security - Swiss sovereign cloud | Infomaniak](https://www.infomaniak.com/en/trust-center)
et [AI service - open source AI on demand via API, hosted in Europe | Infomaniak](https://www.infomaniak.com/en/hosting/ai-services)
(consultés le 2026-09-13).

Confirme le statut de référence de souveraineté qu'Infomaniak occupe déjà
dans `2_qui_est_ce/04_ouverture_et_souverainete.md` et dans les veilles
précédentes (`ia_souverain_2026-05-27`).

## Tarification (modèles utilisés dans le benchmark)

| Modèle | Entrée (CHF/M tok) | Sortie (CHF/M tok) |
| --- | --- | --- |
| Gemma 4 31B IT | 0,20 | 0,40 |
| Kimi K2.6 | 0,60 | 3,00 |

Source : [AI service - the best open-source alternatives to ChatGPT | Infomaniak](https://www.infomaniak.com/en/hosting/ai-services/prices)
(consulté le 2026-09-13, page non entièrement récupérable en une fois — tarifs
recoupés via une seconde requête).

Ces tarifs correspondent exactement à ceux déjà utilisés (traités comme
équivalents EUR) dans `annexes/benchmark/comparatif_ocr_llm_calc_.xlsx`
(colonnes « Tarif entrée/sortie (€/M) », statut « Tarifs Infomaniak fournis
par l'utilisateur ») — la source primaire confirme les chiffres qui avaient
été saisis sans lien vers la page officielle.

## Catalogue réellement exposé (appel API direct)

Relevé par David le 2026-09-13 via Bruno, appel direct à
`GET https://api.infomaniak.com/2/ai/<mon-id>/openai/v1/models` :

```json
{
  "object": "list",
  "data": [
    {"id": "bge_multilingual_gemma2", "owned_by": "system"},
    {"id": "mini_lm_l12_v2", "owned_by": "system"},
    {"id": "Qwen/Qwen3-Embedding-8B", "owned_by": "system"},
    {"id": "mistralai/Ministral-3-14B-Instruct-2512", "owned_by": "system"},
    {"id": "Qwen/Qwen3.5-122B-A10B-FP8", "owned_by": "system"},
    {"id": "google/gemma-4-31B-it", "owned_by": "system"},
    {"id": "moonshotai/Kimi-K2.6", "owned_by": "system"},
    {"id": "nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-FP8", "owned_by": "system"},
    {"id": "mistralai/Mistral-Small-4-119B-2603", "owned_by": "system"},
    {"id": "Qwen/Qwen3.5-397B-A17B-FP8", "owned_by": "system"},
    {"id": "swiss-ai/Apertus-v1.5-70B", "owned_by": "system"}
  ]
}
```

Confirme directement, à la source (pas via une page marketing), que
`google/gemma-4-31B-it` et `moonshotai/Kimi-K2.6` sont réellement disponibles
sur Infomaniak à la date du benchmark — même méthode de vérification que
celle déjà appliquée dans `catalogue_ollama_pro_classification.md`
(mistral_est_il_vraiment_opensource) et dans `sources.md` (vérification des
flux RSS par récupération réelle, pas de mémoire).

Ni GLM ni GPT-5.4-mini ne figurent dans ce catalogue — cohérent avec le fait
que ces deux modèles sont benchmarkés respectivement via Ollama Cloud et
Azure, pas via Infomaniak.

`swiss-ai/Apertus-v1.5-70B` est également présent — c'est le même modèle déjà
recommandé dans `fonds/ia_souverain_2026-05-27/` et repris dans
`conception/annexes/F_choix_llm.md` côté QualiCheck : confirme la continuité
de catalogue entre les deux veilles.
