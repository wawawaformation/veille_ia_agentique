---
title: "Expérimentation GLM"
status: "réalisée — prototype"
---

# Expérimentation

## Chaîne actuelle

Le script Python :

1. reçoit une image ;
2. l'encode et l'envoie à GLM-5.3-Flash via Ollama Cloud ;
3. récupère `content`, `reasoning` et `usage` ;
4. tente d'extraire des métadonnées depuis le reasoning ;
5. nettoie le contenu ;
6. construit un front matter ;
7. enregistre le Markdown ;
8. conserve un log JSON détaillé.

## Traces conservées

Le log comprend notamment :

- métadonnées source ;
- métadonnées documentaires ;
- métriques OCR ;
- signaux extraits ;
- état qualité ;
- `content_raw` ;
- `content_clean` ;
- `reasoning_raw` ;
- réponse API complète.

Cette conservation est importante pour :

- audit ;
- analyse d'erreur ;
- comparaison ;
- reproduction ;
- création future de few-shot ;
- entraînement d'un contrôleur heuristique ou LLM.

## Trois corpus

L'expérience GLM dédiée a été exécutée sur :

- cuisine : 10 pages ;
- Le Capital : 10 pages ;
- web : 5 captures.

Le reasoning est particulièrement volumineux sur certaines pages difficiles,
notamment une page de *Le Capital* et certaines captures Web.
