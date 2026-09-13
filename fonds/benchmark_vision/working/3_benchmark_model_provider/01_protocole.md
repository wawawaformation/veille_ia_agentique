---
title: "Protocole du benchmark général"
status: "réalisé — à renforcer"
---

# Protocole

## Objectif

Comparer plusieurs solutions de transcription visuelle sur des documents réels, sans
chercher uniquement le modèle donnant le texte le plus élégant.

L'unité réellement comparée est le **couple modèle + provider + configuration**.

## Corpus

25 pages au total :

- 10 pages de livre de cuisine ;
- 10 pages de *Le Capital* ;
- 5 captures web.

## Solutions présentes dans le benchmark actuel

- Tesseract ;
- Gemma 4 31B via Ollama ;
- Gemma 4 31B via Infomaniak ;
- GPT-5.4-mini via Azure ;
- GLM-5.3-Flash via Ollama.

## Mesures techniques

Les fichiers `infos.json` permettent de comparer :

- durée totale du lot ;
- nombre de pages ;
- tokens entrants ;
- tokens sortants ;
- tokens totaux.

Tesseract ne produit naturellement pas de métriques de tokens.

## Mesures de qualité observées

L'analyse actuelle est principalement qualitative et par cas difficiles :

- texte absent ;
- substitution ;
- ajout ;
- ordre de lecture ;
- restitution des listes et titres ;
- structure de la page ;
- traitement des petits textes ;
- comportement sur scans dégradés ;
- comportement sur captures web.

## Limite actuelle

Le corpus ne dispose pas encore d'une vérité terrain manuelle complète permettant
de calculer CER/WER de manière robuste.

Une prochaine version doit créer une vérité terrain sur un sous-ensemble de pages
représentatives plutôt que d'étendre indéfiniment le corpus.
