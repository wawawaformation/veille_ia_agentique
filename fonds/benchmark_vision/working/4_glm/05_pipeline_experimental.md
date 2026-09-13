---
title: "Pipeline expérimental envisagé"
status: "hypothèse d'architecture"
---

# Pipeline expérimental

Le schéma `pipeline_ocr_reasoning_v5_lisible.drawio.png` représente un état de la
réflexion **antérieur aux dernières mesures**.

Il doit être lu comme une hypothèse, pas comme une architecture validée.

```text
PNG / capture / maquette
          ↓
     GLM-5.3-Flash
          ↓
 content + reasoning + usage
    │          │          │
    │          │          └── métriques
    │          ↓
    │      LLM texte
    │      gpt-oss:20b
    │      + few-shot
    │          ↓
    │    analyse structurée
    │    métadonnées + qualité
    │          ↓
    └──── paquet page ─────┘
              ↓
       qualité suffisante ?
          ├── oui → normalisation → Markdown final
          └── non → VLM 2 sur le PNG original
```

En parallèle, un log d'audit conserve :

- reasoning brut ;
- réponse API ;
- métriques ;
- analyse structurée.

## Principe économique

Le fallback ne doit pas être systématique.

Le pipeline n'est intéressant que si le premier VLM et son contrôleur permettent de
réserver le second appel à une fraction pertinente des pages.

## Condition de validation

Cette architecture n'est justifiée que si le contrôleur atteint une qualité
suffisante pour détecter les erreurs graves, en particulier les omissions silencieuses,
avec un taux de faux positifs acceptable.
