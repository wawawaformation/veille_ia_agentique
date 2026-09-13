---
title: "Résultats du benchmark"
status: "mesures actuelles"
---

# Résultats

## Mesures agrégées sur les 25 pages

Les valeurs ci-dessous sont recalculées directement à partir des `infos.json` des
trois corpus fournis.

| Couple | Durée totale | s/page | Tokens entrée/page | Tokens sortie/page | Tokens totaux/page |
|---|---:|---:|---:|---:|---:|
| GPT-5.4-mini / Azure | 179,169 s | 7,17 | 1 166,92 | 554,92 | 1 721,84 |
| Gemma 4 31B / Ollama | 231,255 s | 9,25 | 381,92 | 595,52 | 977,44 |
| Tesseract | 289,484 s | 11,58 | — | — | — |
| Gemma 4 31B / Infomaniak | 294,208 s | 11,77 | 376,92 | 608,76 | 985,68 |
| GLM-5.3-Flash / Ollama | 588,080 s | 23,52 | 8 071,32 | 2 511,52 | 10 582,84 |

Ces chiffres décrivent cette campagne, pas une performance universelle.

## Premiers constats

### GPT-5.4-mini / Azure

- meilleur temps moyen de cette campagne ;
- transcription globalement robuste ;
- comportement propre sur les scans difficiles ;
- pas de télémétrie équivalente au `reasoning` séparé exploité avec GLM dans
  l'expérience dédiée.

### Gemma 4 31B

- très bon rapport qualité / volume de tokens ;
- résultats souvent proches entre providers ;
- cas d'omission silencieuse important chez Ollama sur `cuisine/page-0003` ;
- comportement non strictement identique chez Infomaniak et Ollama.

### Tesseract

- constitue une référence OCR classique utile ;
- peut produire beaucoup de texte correct sur des pages propres ;
- se dégrade nettement sur certains défauts de scan et certaines structures ;
- ne fournit pas la compréhension de page d'un VLM.

### GLM-5.3-Flash

- très bonne restitution de structure ;
- récupère notamment le bloc d'ingrédients omis par Gemma/Ollama sur le cas de
  référence ;
- consommation de tokens et latence nettement supérieures dans le benchmark ;
- intérêt principal actuel : propriété supplémentaire observée via l'API Ollama,
  avec `content`, `reasoning` et `usage` séparés.

## Attention : fidélité et qualité éditoriale

Un VLM peut produire un texte plus lisible que le scan en corrigeant implicitement
une graphie qu'il juge improbable.

Pour une publication éditée, cela peut être souhaitable.

Pour un benchmark OCR strict, cela doit être considéré séparément de la fidélité au
scan.
