---
title: "Candidats retenus et exclusions"
status: "à compléter avec sources primaires"
---

# Candidats retenus et exclusions

## Principe

Tous les modèles identifiés pendant la veille ne sont pas nécessairement benchmarkés.

La pré-sélection repose sur la logique du « Qui est-ce ? » :

```text
multimodal ?
    ↓
taille raisonnable ?
    ↓
accessible sans GPU local ?
    ↓
provider disponible ?
    ↓
intérêt pour le besoin ?
    ↓
benchmark
```

Un modèle peut donc être :

- écarté avant test ;
- testé puis écarté ;
- benchmarké complètement ;
- retenu pour un approfondissement spécifique.

Ces statuts doivent rester distincts.

---

## Candidats effectivement benchmarkés

Le corpus actuellement consolidé contient les couples suivants :

| Couple modèle / provider | Statut | Rôle dans le benchmark |
|---|---|---|
| Tesseract | benchmark complet | Référence OCR classique |
| Gemma 4 31B / Ollama | benchmark complet | VLM cloud |
| Gemma 4 31B / Infomaniak | benchmark complet | Même modèle nominal, autre provider |
| GPT-5.4-mini / Azure | benchmark complet | Référence propriétaire performante |
| GLM-5.3-Flash / Ollama | benchmark complet + approfondissement | VLM avec `reasoning` exposé |

---

## Cas particulier : Kimi K2.6

Kimi K2.6 n'a pas été exclu avant test.

Une campagne a déjà été réalisée avec :

```text
Kimi K2.6 / Infomaniak
Corpus : cuisine
Nombre de pages : 10
```

Les résultats ont montré une qualité intéressante, mais également une consommation
très élevée pour un usage OCR page par page.

Le constat empirique actuel est donc :

- bonne qualité générale ;
- sortie très verbeuse ;
- consommation élevée ;
- latence et coût potentiellement disproportionnés pour le rôle d'OCR principal.

Kimi n'est donc pas classé comme « non testé ».

Son statut actuel est plutôt :

```text
testé sur 10 pages
        ↓
qualité correcte à bonne
        ↓
consommation très élevée
        ↓
candidat non prioritaire
```

---

## Complément de benchmark possible sur Kimi

Pour isoler l'effet du provider à modèle constant, il reste à exécuter les **mêmes
10 pages du corpus cuisine** avec :

```text
Kimi K2.6 / Azure
Kimi K2.6 / Ollama Cloud
```

Infomaniak constitue déjà la référence existante.

La comparaison porterait donc sur :

```text
Kimi K2.6
├── Infomaniak   → déjà mesuré — 10 pages cuisine
├── Azure        → à faire — mêmes 10 pages
└── Ollama Cloud → à faire — mêmes 10 pages
```

L'intérêt est de comparer, à modèle nominal constant :

- latence ;
- tokens entrants ;
- tokens sortants ;
- tokens totaux ;
- coût ;
- verbosité ;
- qualité de transcription ;
- différences éventuelles de comportement selon le provider.

Cette comparaison est particulièrement intéressante après le constat réalisé avec
Gemma 4 31B : **un même modèle nominal peut se comporter différemment selon le
provider et les conditions d'inférence**.

---

## Faut-il absolument compléter Kimi ?

Non.

Les mesures Infomaniak existantes peuvent suffire si l'objectif est simplement de
montrer que Kimi est disproportionné pour le rôle d'OCR principal.

Les tests Azure et Ollama deviennent utiles si l'on veut répondre à une question plus
précise :

> La consommation et la verbosité observées viennent-elles essentiellement du modèle,
> ou varient-elles significativement selon le provider ?

Ce complément est donc intéressant méthodologiquement, mais il ne doit pas devenir une
obligation artificielle pour terminer la veille.

---

## Modèles écartés avant test

D'autres modèles peuvent être exclus avant benchmark lorsqu'ils ne franchissent pas
les critères du « Qui est-ce ? ».

Exemples de motifs :

| Motif | Justification |
|---|---|
| Non multimodal | Pas d'entrée image : hors périmètre du rôle de VLM principal |
| Taille très élevée | 120B, 300B ou davantage jugés disproportionnés au besoin |
| Provider inaccessible | Pas de moyen réaliste d'inférence sans GPU local |
| Coût anticipé hors cible | Aucun intérêt à lancer une campagne complète |
| Redondance | Pas d'apport distinct par rapport à un candidat déjà retenu |

Une exclusion avant test ne signifie pas que le modèle est mauvais.

Elle signifie simplement :

> hors périmètre du besoin, des moyens disponibles ou de l'objectif du benchmark.

---

## Cas testé : les modèles tagués « OCR » sur Ollama

Le catalogue Ollama expose un tag `OCR` distinct du tag `vision` (filtre
`ollama.com/search?c=vision`). Deux modèles portant spécifiquement ce tag ont
été essayés :

| Modèle | Description catalogue | Résultat observé |
|---|---|---|
| `glm-ocr` | « multimodal OCR model for complex document understanding, built on the GLM-V encoder–decoder architecture » (tags `vision`, `tools` ; 7,1 M pulls) | Page vide en sortie |
| `deepseek-ocr` | « vision-language model that can perform token-efficient OCR » | Page vide en sortie |

Test informel (essai rapide, pas un benchmark complet à 25 pages comme les
candidats de `3_benchmark_model_provider/`), mais suffisant pour écarter ces
deux candidats à ce stade : une sortie vide est disqualifiante, indépendamment
de toute autre qualité.

**Enseignement méthodologique** : le tag « OCR » du catalogue n'est pas un
signal fiable de pertinence pour ce besoin — un modèle généraliste tagué
seulement `vision` (Gemma 4, GLM-5.3-Flash) s'est révélé plus exploitable que
des modèles spécifiquement étiquetés OCR. Cohérent avec la règle déjà posée
dans `2_qui_est_ce/02_criteres_preselection.md` : un critère apparemment
pertinent (ici, un tag dédié) n'est pas automatiquement un bon prédicteur.

## À compléter

Ajouter progressivement les noms exacts des autres modèles écartés et leurs
caractéristiques à partir des sources primaires utilisées pendant la veille.
