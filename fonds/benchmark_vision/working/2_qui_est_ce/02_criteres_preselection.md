---
title: "Critères de pré-sélection"
status: "à compléter avec sources primaires"
---

# Critères de pré-sélection

## Éliminatoires

### 1. Multimodalité

Un LLM texte seul n'est pas candidat au rôle de VLM principal : il doit accepter une
image en entrée.

Un LLM texte peut toutefois avoir un autre rôle dans le pipeline, par exemple pour
analyser le `reasoning` d'un VLM.

### 2. Dimensionnement

Les modèles annoncés à environ 120B, 300B ou davantage peuvent être écartés sans test
lorsqu'ils sont manifestement disproportionnés au besoin visé ou à son économie.

Le seuil n'est pas une vérité universelle. Il exprime ici un choix de conception :
chercher une solution utilisable pour de la transcription page par page, pas le plus
gros modèle disponible.

### 3. Accessibilité réelle

L'auteur ne disposant pas de GPU local adapté, le modèle doit être accessible via un
service permettant l'inférence distante, ou rester suffisamment léger pour une autre
forme d'exécution réaliste.

## Non éliminatoires mais importants

- open source / open weight / propriétaire ;
- licence ;
- possibilité d'exécution locale théorique ;
- diversité des providers ;
- coût ;
- latence ;
- localisation de l'inférence ;
- politique de données ;
- capacités de sortie structurée ;
- télémétrie exposée par l'API.

## Règle méthodologique

Un critère important n'est pas automatiquement un critère d'exclusion.

Par exemple, un modèle propriétaire peut rester utile comme **référence de qualité**
dans le benchmark, même si la solution de production recherchée privilégie
l'ouverture ou la souveraineté.
