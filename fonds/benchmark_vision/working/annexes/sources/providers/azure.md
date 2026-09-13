---
title: "Sources — Azure AI Foundry"
consulted: "2026-09-13"
---

# Azure AI Foundry — sources primaires

## Tarification GPT-5.4-mini

Entrée : 0,75 $/M tokens ; sortie : 4,50 $/M tokens.

Chiffres recoupés sur deux agrégateurs indépendants citant la page officielle
Azure (`azure.microsoft.com/en-us/pricing/details/azure-openai/`), avec une
date de dernière vérification affichée au 2026-08-06 :

- [GPT 5.4 mini pricing — Azure AI Foundry | Future AGI](https://futureagi.com/llm-cost-calculator/azure-ai-foundry/gpt-5-4-mini/)
- [gpt-5.4-mini Cost Calculator - Azure | Bifrost](https://www.getmaxim.ai/bifrost/llm-cost-calculator/provider/azure/model/gpt-5.4-mini)

(consultés le 2026-09-13). La page officielle Microsoft n'a pas pu être
récupérée directement (page de sélection dynamique par région/SKU) ; les deux
agrégateurs concordent à l'identique sur les deux montants, ce qui limite le
risque d'erreur de recopie.

Ces tarifs sont cohérents avec ceux déjà utilisés (marqués « à confirmer »)
dans `annexes/benchmark/comparatif_ocr_llm_calc_.xlsx` — le statut peut passer
de « indicatif » à « sourcé ».

## Statut du modèle

GPT-5.4-mini est un modèle propriétaire OpenAI servi via Azure AI Foundry :
pas de poids publiés, pas de fiche de licence de type Hugging Face. Utilisé
dans le benchmark comme référence de qualité/robustesse propriétaire, pas
comme candidat à l'ouverture ou à la souveraineté (cf.
`2_qui_est_ce/02_criteres_preselection.md` §Règle méthodologique).
