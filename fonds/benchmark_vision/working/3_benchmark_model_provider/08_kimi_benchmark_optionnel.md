---
title: "Complément de benchmark Kimi K2.6"
status: "optionnel — Infomaniak déjà réalisé"
---

# Complément de benchmark Kimi K2.6

## État actuel

Kimi K2.6 a déjà été testé sur :

```text
Provider : Infomaniak
Corpus   : cuisine
Pages    : 10
```

Ces mesures existent déjà.

La campagne a montré une consommation élevée pour un usage de transcription page par
page.

Il n'est donc pas nécessaire de refaire Infomaniak.

---

## Ce qu'il reste éventuellement à faire

Pour comparer le **même modèle chez plusieurs providers**, lancer les mêmes 10 pages
du corpus cuisine avec :

```text
Kimi K2.6 / Azure
Kimi K2.6 / Ollama Cloud
```

On obtiendrait ainsi :

| Modèle | Provider | Corpus | Statut |
|---|---|---|---|
| Kimi K2.6 | Infomaniak | cuisine — 10 pages | fait |
| Kimi K2.6 | Azure | cuisine — 10 pages | à faire |
| Kimi K2.6 | Ollama Cloud | cuisine — 10 pages | à faire |

---

## Pourquoi conserver exactement les mêmes 10 pages

Le but est de faire varier principalement le provider.

```text
même modèle
+
même corpus
+
même objectif
        ↓
provider différent
```

Cela permettra d'étudier :

- consommation de tokens ;
- latence ;
- coût ;
- verbosité ;
- qualité de transcription ;
- éventuelles omissions ;
- différences de structure ;
- variations de comportement entre providers.

---

## Lien avec le cas Gemma

Le benchmark a déjà révélé un résultat important :

```text
Gemma 4 31B / Ollama
        ≠
Gemma 4 31B / Infomaniak
```

sur au moins une page critique du corpus cuisine.

Kimi permettrait de pousser cette question plus loin :

> Un même modèle présente-t-il également des différences importantes de consommation,
> de latence ou de verbosité selon le provider ?

---

## Conditions de comparaison

Pour rendre les mesures aussi comparables que possible, conserver :

- les 10 mêmes images ;
- le même objectif de transcription ;
- le prompt exact utilisé pour chaque run ;
- les paramètres accessibles ;
- la date du test ;
- le nom/version du modèle exposé par le provider ;
- les métriques de tokens ;
- la durée ;
- le coût calculé selon le tarif du provider.

Lorsque les prompts ou API diffèrent, le documenter explicitement plutôt que prétendre
à une égalité parfaite des conditions.

---

## Pas d'obligation de terminer la campagne

Ce benchmark complémentaire reste **optionnel**.

Les chiffres Infomaniak peuvent déjà suffire pour conclure :

> Kimi K2.6 est capable de produire de bonnes sorties, mais sa consommation observée
> est trop importante pour en faire un candidat prioritaire comme OCR principal.

Azure et Ollama Cloud deviennent intéressants si l'objectif est d'aller plus loin et
de séparer :

```text
effet modèle
```

de :

```text
effet provider
```

Le benchmark doit rester au service de la décision, pas devenir une collection de
runs sans valeur supplémentaire.
