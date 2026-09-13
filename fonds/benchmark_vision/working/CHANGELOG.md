# CHANGELOG

## 2026-09-13 — Réouverture de l'hypothèse de pipeline

### Contexte

L'approfondissement initial s'était concentré sur **GLM-5.3-Flash via Ollama Cloud**,
car son `reasoning` séparé semblait offrir une piste intéressante pour construire un
contrôle qualité avant fallback.

Une nouvelle observation change cependant l'ordre des expérimentations : le mode
`thinking` est également disponible pour d'autres VLM utilisés dans la veille,
notamment **Kimi K2.6** et potentiellement **Gemma 4 31B** via Ollama.

L'hypothèse « GLM comme VLM principal parce qu'il expose du reasoning » n'est donc
plus suffisante en l'état.

---

### Changement de priorité

Ancienne piste envisagée :

```text
image
  ↓
GLM-5.3-Flash
  ↓
content + reasoning
  ↓
contrôle qualité
  ↓
fallback vers un second VLM si nécessaire
```

Nouvelle hypothèse à tester :

```text
image
  ↓
Gemma 4 31B / Ollama
  ↓
content + thinking
  ↓
qualité suffisante ?
  ├── oui → sortie retenue
  └── non → GLM-5.3-Flash / Ollama
```

Cette inversion de l'arbre de décision est **une hypothèse**, pas encore une décision
d'architecture.

Elle devient intéressante si Gemma conserve son avantage de coût / latence tout en
produisant, avec `thinking` activé, des signaux de qualité suffisamment exploitables.

---

### Expériences prioritaires à lancer

#### Gemma 4 31B / Ollama

Comparer sur les mêmes pages :

```text
Gemma / Ollama / thinking OFF
Gemma / Ollama / thinking ON
```

À mesurer :

- qualité de transcription ;
- omissions silencieuses ;
- structure Markdown ;
- contenu du thinking ;
- capacité du thinking à signaler les ambiguïtés ou reconstructions ;
- prompt tokens ;
- completion tokens ;
- total tokens ;
- durée ;
- coût.

Page prioritaire :

```text
cuisine/page-03
```

Cette page est critique car une exécution Gemma/Ollama du benchmark précédent avait
omis silencieusement le bloc d'ingrédients de la crème au chocolat.

Question principale :

> Le mode thinking permet-il à Gemma d'éviter ou au moins de signaler ce type
> d'omission ?

---

#### Kimi K2.6 / Ollama

Comparer :

```text
Kimi / Ollama / thinking OFF
Kimi / Ollama / thinking ON
```

À mesurer :

- qualité de transcription ;
- verbosité ;
- consommation de tokens ;
- durée ;
- coût ;
- contenu du thinking ;
- intérêt réel du thinking pour un contrôle qualité.

L'objectif est également de vérifier si la consommation très élevée déjà observée
avec **Kimi K2.6 / Infomaniak** est principalement liée au modèle ou si elle varie
fortement selon le provider et l'activation du thinking.

---

### Benchmark Kimi multi-provider

État actuel :

```text
Kimi K2.6 / Infomaniak
→ déjà mesuré
→ corpus cuisine
→ 10 pages
```

Reste éventuellement à compléter :

```text
Kimi K2.6 / Azure
→ 10 pages cuisine

Kimi K2.6 / Ollama Cloud
→ 10 pages cuisine
```

Le benchmark complet Azure/Ollama n'est pas prioritaire avant le test
`thinking OFF / ON` sur Ollama.

---

### Conséquence méthodologique

La veille ne doit plus présenter le reasoning comme une propriété distinctive de GLM
sans comparaison.

La question devient :

> Quel couple modèle + provider + configuration offre le meilleur compromis entre
> qualité OCR, coût, latence et signaux de contrôle exploitables ?

L'unité de comparaison devient donc encore plus précisément :

```text
modèle
+ provider
+ configuration de reasoning/thinking
+ prompt
+ paramètres disponibles
```

---

### Décision reportée

Aucune architecture définitive n'est arrêtée avant les tests suivants :

- Gemma / Ollama / thinking OFF ;
- Gemma / Ollama / thinking ON ;
- Kimi / Ollama / thinking OFF ;
- Kimi / Ollama / thinking ON.

Après ces quatre essais, réévaluer :

1. le VLM principal ;
2. le rôle éventuel de GLM comme fallback ;
3. l'intérêt d'un contrôleur textuel séparé (`gpt-oss:20b`) ;
4. la nécessité d'un second VLM ;
5. le coût réel du pipeline en cascade.
