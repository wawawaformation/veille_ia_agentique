---
title: "Qui est-ce ? — Pré-sélection avant benchmark"
status: "méthode"
---

# Le jeu « Qui est-ce ? »

Tester tous les modèles disponibles n'aurait pas de sens.

La pré-sélection reprend volontairement la mécanique du jeu **Qui est-ce ?** :
chaque question élimine des candidats qui ne répondent pas au besoin avant de
consommer du temps ou du budget en benchmark.

```text
Le modèle accepte-t-il une image ?
├── non → éliminé
└── oui
     ↓
Sa taille / son coût potentiel sont-ils raisonnables pour l'usage ?
├── non → éliminé
└── oui
     ↓
Est-il accessible sans GPU local via un provider utilisable ?
├── non → éliminé pour cette expérimentation
└── oui
     ↓
Présente-t-il un intérêt distinct des candidats déjà retenus ?
├── non → non prioritaire
└── oui → benchmark
```

## Pourquoi cette étape est importante

Un benchmark sérieux doit documenter non seulement ce qui a été testé, mais aussi
les candidats connus qui n'ont pas été étudiés et **la raison de leur exclusion**.

Une exclusion avant test n'est pas un jugement sur la qualité intrinsèque du modèle.
Elle signifie simplement : **hors périmètre de ce besoin et de ces contraintes**.
