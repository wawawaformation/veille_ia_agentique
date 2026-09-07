---
title: "Veille IA — 20 LLM sur le continuum Fermé / API → Open Source"
date: 2026-09-07
lang: fr-FR
---

# Veille IA — 20 LLM sur le continuum d’ouverture

## Objet

Cette fiche propose une **fresque de 20 LLM**, répartis en quatre catégories pédagogiques :

1. **Fermé / API**
2. **Open weight**
3. **Open weight ++**
4. **Open Source / ouverture de bout en bout**

L’objectif n’est **pas** de classer les modèles du « moins bon » au « meilleur ».  
La fresque décrit **le niveau d’ouverture** d’un modèle et les libertés qu’il donne à l’utilisateur.

> **Important :** `Open weight ++` n’est pas une catégorie officielle.  
> Elle sert ici à distinguer les modèles qui publient non seulement leurs poids, mais aussi une documentation technique, des informations d’entraînement, du code ou des éléments de la « recette » nettement plus riches qu’une simple publication de poids.

De même, la colonne **Open Source / ouverture de bout en bout** ne signifie pas que chaque modèle a reçu une « certification OSI ». L’OSI ne certifie pas les modèles individuels. Certains projets de cette colonne ont été utilisés pendant la phase de validation de l’Open Source AI Definition (OSAID), d’autres sont classés ici parce qu’ils publient poids, code, données et recette d’entraînement de manière particulièrement complète.

---

# 1. Tableau de la fresque — 5 × 4

| Fermé / API | Open weight | Open weight ++ | Open Source / ouverture de bout en bout |
|---|---|---|---|
| **GPT-5.6 Sol** — OpenAI | **Llama 4 Maverick** — Meta | **gpt-oss-120b** — OpenAI | **Luciole-23B** — OpenLLM France |
| **Claude Fable 5.1** — Anthropic | **Grok-1** — xAI | **Gemma 4 31B** — Google DeepMind | **OLMo 3 32B** — Ai2 |
| **Gemini 3.1 Pro** — Google DeepMind | **Phi-4** — Microsoft | **DeepSeek-R1** — DeepSeek | **Apertus 1.5 70B** — Swiss AI Initiative |
| **Grok 4.6** — xAI | **Mixtral 8×7B** — Mistral AI | **Qwen3-235B-A22B** — Alibaba / Qwen | **Pythia-12B** — EleutherAI |
| **Amazon Nova 2 Pro** — AWS | **Mistral Medium 3.5** — Mistral AI | **Mistral Small 4** — Mistral AI | **Amber-7B** — LLM360 |

---

# 2. Comment lire la fresque

## Fermé / API

Le modèle est essentiellement consommé comme un **service**.

L’utilisateur peut l’interroger, l’intégrer à une application et parfois le personnaliser via les mécanismes prévus par le fournisseur, mais il ne dispose généralement pas :

- des poids ;
- du pipeline complet d’entraînement ;
- du corpus d’entraînement ;
- des éléments nécessaires pour reconstruire le modèle.

Cette approche peut répondre à une logique de :

- simplicité d’usage ;
- maîtrise de l’infrastructure ;
- sécurité et contrôle ;
- protection du savoir-faire ;
- **rentabilisation des investissements de R&D** ;
- facturation récurrente du service.

## Open weight

Les **poids entraînés sont téléchargeables**.

Cela permet généralement :

- l’inférence locale ;
- l’auto-hébergement ;
- le fine-tuning autonome ;
- la quantification ;
- l’adaptation à son propre matériel ;
- la création de dérivés, selon la licence.

Mais les données et la recette complète d’entraînement peuvent rester fermées.

## Open weight ++

Catégorie pédagogique utilisée dans cette veille.

On dispose des poids **et** d’une partie significative de la recette :

- architecture détaillée ;
- rapport technique ;
- description du préentraînement ;
- étapes de post-entraînement ;
- code d’inférence ou d’entraînement ;
- informations substantielles sur les données ;
- parfois checkpoints ou datasets intermédiaires.

La reproduction complète du modèle n’est toutefois pas nécessairement possible.

## Open Source / ouverture de bout en bout

L’ambition est de permettre non seulement d’utiliser le modèle, mais aussi de **comprendre sa fabrication**.

On cherche donc à rendre disponibles, autant que possible :

- les poids ;
- le code ;
- les données ou les éléments permettant de reconstruire le dataset ;
- la recette d’entraînement ;
- les configurations ;
- les checkpoints ;
- les outils d’évaluation.

Cette démarche se rapproche des libertés historiques du logiciel libre : **utiliser, étudier, modifier et partager**.

---

# 3. Fermé / API

## 3.1 GPT-5.6 Sol — OpenAI

**Position dans la fresque : Fermé / API**

GPT-5.6 Sol est le modèle phare de la famille GPT-5.6 d’OpenAI. Il est destiné aux tâches complexes de développement, de recherche, de sciences, de cybersécurité et de travail intellectuel. OpenAI le distribue via ses produits et son API, mais ne publie pas ses poids.

### Informations notables

- Modèle phare de la famille GPT-5.6.
- Disponible via l’API OpenAI et les produits OpenAI.
- Fenêtre de contexte annoncée supérieure à un million de tokens.
- Les poids ne sont pas publiés.
- Le dataset d’entraînement et la chaîne complète de fabrication ne sont pas fournis.

### Pourquoi il est particulièrement intéressant dans la fresque

Il permet un parallèle immédiat avec **gpt-oss** :

> **OpenAI peut commercialiser GPT comme service fermé tout en publiant parallèlement une autre famille à poids ouverts.**

Cela montre que le degré d’ouverture n’est pas une propriété d’une entreprise : c’est **un choix de publication pour un modèle donné**.

**Source principale :**  
https://openai.com/index/gpt-5-6/

---

## 3.2 Claude Fable 5.1 — Anthropic

**Position dans la fresque : Fermé / API**

Claude Fable 5.1 est l’un des modèles les plus avancés d’Anthropic en septembre 2026, orienté notamment vers le code, le travail intellectuel et les tâches longues.

### Informations notables

- Lancé en septembre 2026.
- Accessible via Claude et la plateforme API d’Anthropic.
- Disponible également via plusieurs clouds partenaires.
- Anthropic publie des system cards détaillant capacités, risques et évaluations.
- Les poids du modèle ne sont pas disponibles.
- Le corpus d’entraînement et la recette complète ne sont pas publiés.

### Pourquoi il est intéressant

Claude illustre bien le modèle **« intelligence comme service »** :

> l’utilisateur bénéficie du modèle, des mises à jour, de la sécurité et de l’infrastructure d’Anthropic, mais ne possède pas le modèle lui-même.

**Source principale :**  
https://www.anthropic.com/claude/fable

---

## 3.3 Gemini 3.1 Pro — Google DeepMind

**Position dans la fresque : Fermé / API**

Gemini 3.1 Pro est un modèle multimodal de Google DeepMind destiné aux tâches complexes et au raisonnement.

### Informations notables

- Entrées texte, image, audio et vidéo.
- Contexte annoncé jusqu’à environ 1 million de tokens.
- Accessible via Gemini, Google AI Studio et les API Google.
- Google publie une model card décrivant notamment les capacités, les limites et certains éléments liés aux données.
- Les poids ne sont pas publiés.

### Pourquoi il est essentiel dans la fresque

Il permet le deuxième parallèle majeur de la présentation :

> **Gemini ↔ Gemma**

Google dispose donc à la fois :

- d’une famille propriétaire distribuée comme service : **Gemini** ;
- d’une famille à poids ouverts : **Gemma**.

Ce parallèle répond directement au couple :

> **GPT ↔ gpt-oss**

**Source principale :**  
https://deepmind.google/models/gemini/pro/

---

## 3.4 Grok 4.6 — xAI

**Position dans la fresque : Fermé / API**

Grok 4.6 est un modèle récent de xAI, orienté vers les agents de longue durée, le code et les tâches interactives complexes.

### Informations notables

- Lancé en août 2026.
- Accessible comme service et via l’API xAI.
- Accent mis sur les tâches agentiques longues.
- Les poids de Grok 4.6 ne sont pas publiés.

### Pourquoi il est intéressant

xAI permet de montrer qu’une même entreprise peut avoir adopté des stratégies d’ouverture différentes selon les générations :

> **Grok-1 : poids publiés**  
> **Grok 4.6 : modèle distribué comme service**

L’histoire d’un éditeur n’est donc pas nécessairement une progression linéaire vers davantage d’ouverture.

**Source principale :**  
https://x.ai/news/grok-4-6

---

## 3.5 Amazon Nova 2 Pro — AWS

**Position dans la fresque : Fermé / API**

Amazon Nova 2 Pro est le modèle haut de gamme de la génération Nova 2, destiné aux tâches complexes et multi-étapes.

### Informations notables

- Disponible via Amazon Bedrock / Nova Forge.
- Raisonnement avec différents niveaux d’effort.
- Contexte annoncé jusqu’à environ 1 million de tokens.
- AWS propose des mécanismes de personnalisation de ses modèles sur son infrastructure.
- Les poids ne sont pas publiés comme un modèle téléchargeable indépendant.

### Pourquoi il est intéressant

Nova représente bien la logique **cloud / plateforme** :

> le modèle fait partie d’un ensemble comprenant infrastructure, déploiement, personnalisation, observabilité et facturation.

Cela illustre une raison rationnelle de rester fermé : vendre non seulement un modèle, mais **un service industriel complet**.

**Source principale :**  
https://aws.amazon.com/nova/models/

---

# 4. Open weight

## 4.1 Llama 4 Maverick — Meta

**Position dans la fresque : Open weight**

Llama 4 Maverick est l’un des grands modèles multimodaux de Meta. Il utilise une architecture Mixture-of-Experts.

### Informations notables

- Environ 400 milliards de paramètres au total.
- Environ 17 milliards de paramètres actifs par token.
- Poids téléchargeables.
- Licence spécifique : **Llama 4 Community License Agreement**.
- Meta emploie volontiers le terme « open source » dans sa communication.

### Pourquoi il est central pour la veille

**Llama est probablement l’exemple le plus connu de confusion entre open weight et open source.**

La disponibilité des poids permet :

- l’auto-hébergement ;
- le fine-tuning ;
- la quantification ;
- la création de dérivés.

Mais la publication des poids n’équivaut pas à une ouverture complète du processus d’entraînement et des données.

La licence Llama est également une licence spécifique à Meta, et non une licence open source classique de type Apache 2.0 ou MIT.

### Message à retenir

> **« Llama est téléchargeable » est vrai.  
> « Llama est Open Source AI au sens strict » demande beaucoup plus de prudence.**

L’OSI avait analysé Llama 2 pendant la conception de l’OSAID et conclu que cette version ne satisfaisait pas les critères étudiés. Cela ne constitue pas une certification ou une évaluation automatique de Llama 4.

**Sources principales :**  
https://ai.meta.com/resources/models-and-libraries/llama-downloads/  
https://opensource.org/ai/faq

---

## 4.2 Grok-1 — xAI

**Position dans la fresque : Open weight**

En 2024, xAI a publié les poids et une implémentation de référence de Grok-1.

### Informations notables

- 314 milliards de paramètres.
- Architecture Mixture-of-Experts.
- 8 experts, dont 2 actifs par token.
- Code et poids sous licence Apache 2.0.
- Code JAX fourni pour charger et exécuter le modèle.

### Limite de l’ouverture

Le dépôt précise explicitement que la licence concerne le code publié et les poids associés.

Le corpus d’entraînement et la chaîne complète ayant produit le modèle ne sont pas publiés de manière permettant de reconstruire Grok-1.

### Pourquoi il est intéressant

C’est un **cas presque scolaire d’open weight** :

> on peut récupérer le modèle entraîné et son architecture, mais pas nécessairement refaire son entraînement.

Il permet aussi le parallèle historique avec Grok 4.6.

**Source principale :**  
https://github.com/xai-org/grok-1

---

## 4.3 Phi-4 — Microsoft

**Position dans la fresque : Open weight**

Phi-4 est un modèle compact de Microsoft Research orienté vers le raisonnement, les mathématiques et le code.

### Informations notables

- 14 milliards de paramètres.
- Transformer dense.
- Licence MIT.
- Environ 9,8 trillions de tokens d’entraînement annoncés.
- Microsoft décrit les grandes catégories de données :
  - données synthétiques ;
  - données du Web filtrées ;
  - livres académiques ;
  - questions-réponses.
- Processus de post-entraînement comprenant notamment SFT et DPO.

### Pourquoi il est intéressant

Phi-4 montre qu’un modèle peut être **juridiquement très permissif et techniquement bien documenté**, sans pour autant fournir le dataset complet ni tous les éléments de reproductibilité.

> **Licence ouverte ≠ processus de fabrication entièrement ouvert.**

**Source principale :**  
https://huggingface.co/microsoft/phi-4

---

## 4.4 Mixtral 8×7B — Mistral AI

**Position dans la fresque : Open weight**

Mixtral 8×7B a joué un rôle historique important dans la popularisation des modèles Mixture-of-Experts à poids ouverts.

### Informations notables

- Architecture MoE.
- Environ 47 milliards de paramètres au total.
- Environ 13 milliards de paramètres actifs.
- Poids sous licence Apache 2.0.
- Modèle aujourd’hui retiré des offres actives de Mistral, mais toujours important historiquement.

### Pourquoi il est intéressant

Mistral l’a présenté comme un modèle « open source », mais l’OSI a utilisé Mixtral comme cas d’étude pendant la validation de l’OSAID et l’a classé parmi les systèmes analysés ne disposant pas de tous les composants requis.

Il illustre donc parfaitement le problème de vocabulaire :

> **poids Apache 2.0 + modèle téléchargeable ≠ automatiquement Open Source AI au sens OSAID.**

**Sources principales :**  
https://docs.mistral.ai/models/mixtral-8x7b-0-1  
https://opensource.org/ai/faq

---

## 4.5 Mistral Medium 3.5 — Mistral AI

**Position dans la fresque : Open weight**

Mistral Medium 3.5 est un modèle multimodal de 128 milliards de paramètres orienté notamment vers les agents et le code.

### Informations notables

- 128 milliards de paramètres.
- Contexte annoncé à 256k.
- Poids disponibles.
- Licence **Modified MIT**.
- Disponible également comme API commerciale.

### Pourquoi il est particulièrement intéressant

Il démontre qu’il ne faut pas opposer automatiquement :

> **API** et **open weight**.

Un même modèle peut être :

- téléchargeable ;
- auto-hébergeable ;
- et parallèlement proposé comme API managée.

La vraie distinction est donc plutôt :

> **« Est-ce que les poids me sont accessibles ? »**

que :

> **« Existe-t-il une API ? »**

**Source principale :**  
https://docs.mistral.ai/models/mistral-medium-3-5-26-04

---

# 5. Open weight ++

## 5.1 gpt-oss-120b — OpenAI

**Position dans la fresque : Open weight ++**

OpenAI a lancé gpt-oss-120b et gpt-oss-20b comme modèles de raisonnement **open-weight**.

### Informations notables

- gpt-oss-120b : environ 117 milliards de paramètres.
- Environ 5,1 milliards de paramètres actifs par token.
- Architecture MoE.
- Licence Apache 2.0.
- Poids téléchargeables.
- Exécution possible sur une infrastructure contrôlée par l’utilisateur.
- Fine-tuning et adaptation possibles avec des outils ouverts.
- OpenAI fournit model card, documentation technique et implémentations de référence.

### Pourquoi il est dans « Open weight ++ »

OpenAI ne prétend pas que gpt-oss soit un modèle totalement reproductible depuis ses données brutes.

En revanche, l’ouverture est nettement plus riche qu’une simple publication d’un fichier de poids.

### Le parallèle clé

> **GPT-5.6 Sol : intelligence consommée comme service**  
> **gpt-oss : modèle téléchargeable et adaptable**

C’est probablement l’un des parallèles les plus pédagogiques de la fresque.

**Sources principales :**  
https://openai.com/index/gpt-oss-model-card/  
https://help.openai.com/en/articles/11870455

---

## 5.2 Gemma 4 31B — Google DeepMind

**Position dans la fresque : Open weight ++**

Gemma est la famille de modèles ouverts de Google DeepMind. Gemma 4 comprend plusieurs tailles et architectures.

### Informations notables

- Licence Apache 2.0.
- Poids ouverts.
- Versions pré-entraînées et instruction-tuned.
- Multimodalité texte + image, et audio sur certaines variantes.
- Jusqu’à 256k de contexte selon les versions.
- Plus de 140 langues annoncées.
- Model card et rapport technique détaillés.

### Pourquoi il est dans cette catégorie

Google fournit davantage qu’un simple binaire :

- architecture ;
- documentation ;
- rapport technique ;
- informations importantes sur les catégories de données et l’entraînement.

Mais cela ne signifie pas pour autant que l’intégralité du corpus et chaque artefact permettant de reproduire Gemma soient publiés.

### Parallèle clé

> **Gemini : fermé / API**  
> **Gemma : poids ouverts**

Il répond directement au parallèle OpenAI :

> **GPT ↔ gpt-oss**

**Source principale :**  
https://ai.google.dev/gemma/docs/core/model_card_4

---

## 5.3 DeepSeek-R1 — DeepSeek

**Position dans la fresque : Open weight ++**

DeepSeek-R1 est un grand modèle de raisonnement dérivé de DeepSeek-V3-Base.

### Informations notables

- 671 milliards de paramètres au total.
- Environ 37 milliards de paramètres actifs.
- Fenêtre de contexte de 128k.
- Code et poids sous licence MIT.
- Usage commercial autorisé.
- Modifications et dérivés autorisés.
- Distillation explicitement autorisée.
- Publication de plusieurs modèles distillés.
- Documentation importante sur les différentes étapes de renforcement et de post-entraînement.

### Pourquoi DeepSeek est central pour cette présentation

DeepSeek est très souvent qualifié d’**« open source »** dans la presse et dans les discussions techniques.

Il est incontestablement **très ouvert** sur plusieurs dimensions :

- poids ;
- code ;
- licence permissive ;
- architecture ;
- description du processus de raisonnement et du post-entraînement.

Mais l’ensemble des données et artefacts nécessaires pour reproduire intégralement le modèle de départ ne sont pas fournis.

### Message à retenir

> **DeepSeek-R1 est extrêmement ouvert, mais “très ouvert” et “Open Source AI de bout en bout” ne sont pas exactement la même affirmation.**

C’est un excellent pendant de Llama : les deux sont souvent appelés « open source », mais pour des raisons et avec des niveaux d’ouverture différents.

**Source principale :**  
https://github.com/deepseek-ai/DeepSeek-R1

---

## 5.4 Qwen3-235B-A22B — Alibaba / Qwen

**Position dans la fresque : Open weight ++**

Qwen3-235B-A22B est un grand modèle MoE de la famille Qwen3.

### Informations notables

- 235 milliards de paramètres au total.
- Environ 22 milliards de paramètres actifs.
- 128 experts, dont 8 activés.
- Licence Apache 2.0.
- Qwen emploie lui-même l’expression **open-weighting**.
- Environ 36 trillions de tokens de préentraînement annoncés.
- 119 langues et dialectes.
- Description des grandes sources :
  - Web ;
  - PDF ;
  - données mathématiques ;
  - code ;
  - données synthétiques.
- Préentraînement décrit en plusieurs étapes.
- Post-entraînement documenté en quatre grandes phases, dont CoT et reinforcement learning.

### Pourquoi il est dans « Open weight ++ »

Qwen est particulièrement intéressant parce qu’on connaît **beaucoup d’éléments de la recette**.

On sait :

- quelle architecture est employée ;
- combien de tokens ont été utilisés ;
- quelles grandes familles de données interviennent ;
- comment se déroule une partie du post-entraînement.

Mais on ne dispose pas nécessairement de tous les ingrédients exacts permettant de refaire le modèle.

**Source principale :**  
https://qwenlm.github.io/blog/qwen3/

---

## 5.5 Mistral Small 4 — Mistral AI

**Position dans la fresque : Open weight ++**

Mistral Small 4 est un modèle hybride récent réunissant conversation, raisonnement, code et multimodalité.

### Informations notables

- 119 milliards de paramètres au total.
- Environ 6,5 milliards de paramètres actifs.
- Architecture hybride / MoE.
- Contexte de 256k.
- Texte + image.
- Raisonnement configurable.
- Licence Apache 2.0.
- Poids publiés.

### Pourquoi il est intéressant

Mistral utilise volontiers le vocabulaire d’« open source » pour ses modèles sous licence Apache.

La fresque permet de ne pas contester l’utilité de cette ouverture, tout en distinguant :

- **ouverture des poids et du code d’usage** ;
- **ouverture de la fabrication de bout en bout**.

Il est donc placé ici comme exemple de modèle **très ouvert et facilement réutilisable**, mais pour lequel la totalité des données et du processus de production n’est pas publiée comme dans un projet scientifique totalement reproductible.

**Source principale :**  
https://mistral.ai/news/mistral-small-4/

---

# 6. Open Source / ouverture de bout en bout

## 6.1 Luciole-23B — OpenLLM France

**Position dans la fresque : Open Source / ouverture de bout en bout**

Luciole est particulièrement intéressant dans cette veille parce qu’il avait déjà fait l’objet d’un test personnel lors d’une précédente veille du **29 juillet 2026**.

### Informations notables

OpenLLM France publie pour Luciole-23B :

- les poids ;
- le dataset de préentraînement ;
- les informations de prétraitement ;
- le dépôt d’entraînement ;
- les checkpoints intermédiaires ;
- les différentes phases du préentraînement ;
- les éléments de post-entraînement.

Le préentraînement de Luciole-23B est décrit en plusieurs grandes phases :

1. environ 3,5 trillions de tokens pour le préentraînement initial ;
2. environ 1 trillion supplémentaire avec davantage de données de qualité, de maths et de code ;
3. environ 300 milliards de tokens pour une phase d’annealing ;
4. deux étapes supplémentaires pour étendre le contexte jusqu’à environ 131k tokens.

### Pourquoi il est particulièrement important

Luciole permet de relier **deux veilles différentes**.

Lors du test du 29 juillet 2026, l’intérêt initial portait sur :

- la souveraineté ;
- la frugalité ;
- le français ;
- le RAG ;
- l’architecture hybride Mamba / Transformer.

Le modèle n’avait finalement pas été retenu pour l’usage testé, principalement parce que l’inférence CPU mesurée était trop lente sur l’environnement disponible.

Cette nouvelle veille permet de le regarder autrement :

> **un modèle peut ne pas être le meilleur choix opérationnel pour un usage donné, tout en étant exemplaire sur la transparence et l’ouverture.**

C’est un très bon argument pour rappeler que :

> **niveau d’ouverture ≠ niveau de performance ≠ adéquation à un usage.**

**Source principale :**  
https://huggingface.co/OpenLLM-France/Luciole-23B-Base

---

## 6.2 OLMo 3 32B — Ai2

**Position dans la fresque : Open Source / ouverture de bout en bout**

OLMo est l’un des projets les plus emblématiques d’une approche scientifique réellement ouverte.

### Informations notables

Pour OLMo 3, Ai2 publie notamment :

- code d’entraînement ;
- scripts officiels ;
- checkpoints ;
- logs de monitoring ;
- détails des différentes phases ;
- données et corpus associés ;
- recettes de préentraînement et de post-entraînement.

Pour OLMo 3 32B, la documentation décrit notamment :

- une phase principale de préentraînement ;
- du mid-training ;
- une phase long-context ;
- les ressources GPU utilisées ;
- les volumes de tokens par phase.

### Pourquoi il est fondamental

Avec OLMo, il devient possible d’étudier non seulement **le modèle final**, mais aussi **son évolution pendant l’entraînement**.

Cela change complètement la nature de l’audit scientifique.

L’OSI cite OLMo parmi les systèmes ayant passé la phase de validation utilisée lors de la construction de l’OSAID.

### Analogie culinaire

OLMo ne fournit pas seulement :

> **le plat**

mais aussi :

> **la recette, les ingrédients, les étapes de cuisson et plusieurs photos du plat pendant sa préparation.**

**Sources principales :**  
https://github.com/allenai/OLMo-core  
https://opensource.org/ai/faq

---

## 6.3 Apertus 1.5 70B — Swiss AI Initiative

**Position dans la fresque : Open Source / ouverture de bout en bout**

Apertus est développé par la Swiss AI Initiative, portée notamment par l’EPFL, l’ETH Zurich et le CSCS.

### Informations notables

Apertus 1.5 existe notamment en versions 8B et 70B.

Le projet revendique explicitement :

- **open weights** ;
- **open data** ;
- **open science** ;
- code d’entraînement ;
- recettes ;
- informations détaillées sur les données ;
- documentation liée à la conformité et à l’AI Act.

Apertus 1.5 ajoute notamment :

- multimodalité ;
- image ;
- audio ;
- raisonnement configurable ;
- contexte jusqu’à environ 262k tokens.

### Pourquoi il est intéressant

Apertus introduit une autre motivation de l’ouverture :

> **la souveraineté technologique.**

Le projet ne cherche pas seulement à permettre le hacking ou la recherche académique. Il vise également à créer une infrastructure de modèle de fondation :

- inspectable ;
- indépendante ;
- documentée ;
- réutilisable.

### Nuance

Apertus se décrit comme **fully open**. Cela ne signifie pas qu’il existe une certification OSI du modèle : l’OSI n’en délivre pas.

**Sources principales :**  
https://www.apertus-ai.org/  
https://huggingface.co/swiss-ai/Apertus-v1.5-70B

---

## 6.4 Pythia-12B — EleutherAI

**Position dans la fresque : Open Source / ouverture de bout en bout**

Pythia est moins intéressant aujourd’hui pour sa performance brute que pour sa valeur scientifique.

### Informations notables

La famille Pythia comprend plusieurs tailles jusqu’à 12B.

Pour chaque modèle, EleutherAI publie :

- les poids ;
- le code ;
- les données ;
- les instructions de reproductibilité ;
- l’ordre des données ;
- **154 checkpoints intermédiaires**.

Les modèles ont été entraînés sur environ 300 milliards de tokens.

### Pourquoi Pythia est exceptionnel

Son objectif est précisément de permettre l’étude de la **dynamique d’apprentissage**.

Avec les checkpoints successifs, un chercheur peut étudier :

- quand une connaissance apparaît ;
- quand une capacité émerge ;
- comment un biais évolue ;
- comment la mémorisation se développe.

Pythia rend donc concrète une idée centrale de cette veille :

> **l’ouverture des données et du processus ne sert pas seulement à réutiliser le modèle ; elle permet de comprendre comment le modèle s’est construit.**

L’OSI cite Pythia parmi les modèles ayant passé sa phase de validation OSAID.

**Sources principales :**  
https://github.com/EleutherAI/pythia  
https://opensource.org/ai/faq

---

## 6.5 Amber-7B — LLM360

**Position dans la fresque : Open Source / ouverture de bout en bout**

Amber est le premier modèle publié par le projet LLM360.

### Informations notables

Amber est un modèle de 7 milliards de paramètres basé sur une architecture de type Llama.

LLM360 publie :

- le modèle final ;
- le dataset préparé ;
- le code de préparation des données ;
- le code d’entraînement ;
- les configurations ;
- les détails d’entraînement ;
- les résultats intermédiaires ;
- **360 checkpoints**.

Le corpus est notamment construit à partir de :

- RedPajama ;
- RefinedWeb ;
- StarCoderData.

### Pourquoi il est particulièrement pédagogique

Amber montre que la valeur d’un modèle ouvert ne dépend pas nécessairement de sa place sur les benchmarks du moment.

Sa valeur est de permettre à la communauté de répondre à des questions telles que :

> **« Qu’est-ce qui s’est passé entre le checkpoint 120 et le checkpoint 240 ? »**

La totalité de la trajectoire d’apprentissage devient un objet d’étude.

L’OSI cite également Amber parmi les modèles ayant passé la phase de validation de l’OSAID.

**Sources principales :**  
https://github.com/LLM360/amber-train  
https://github.com/LLM360/amber-data-prep  
https://opensource.org/ai/faq

---

# 7. Les parallèles importants à faire ressortir à l’oral

## OpenAI : GPT ↔ gpt-oss

| GPT-5.6 Sol | gpt-oss-120b |
|---|---|
| Poids fermés | Poids publiés |
| Utilisation via service/API | Exécution autonome |
| Infrastructure OpenAI | Infrastructure choisie par l’utilisateur |
| Fine-tuning selon les services proposés | Fine-tuning autonome possible |
| Logique de service | Logique d’écosystème et de réutilisation |

**Message :**

> Une même entreprise peut choisir plusieurs stratégies de diffusion.

---

## Google : Gemini ↔ Gemma

| Gemini 3.1 Pro | Gemma 4 |
|---|---|
| Famille propriétaire | Famille à poids ouverts |
| API / services Google | Téléchargement et auto-hébergement |
| Poids non publiés | Poids Apache 2.0 |
| Contrôle du fournisseur | Adaptation locale |

**Message :**

> « Google est fermé » ou « Google est open source » sont deux formulations trop simples.  
> Il faut parler du **modèle précis**.

---

## xAI : Grok 4.6 ↔ Grok-1

Le contraste est ici temporel :

- Grok-1 a été publié avec ses poids et du code ;
- les générations Grok actuelles sont essentiellement distribuées comme services.

**Message :**

> Le niveau d’ouverture peut changer d’une génération à l’autre.

---

# 8. Deux cas de vocabulaire à discuter : Llama et DeepSeek

## Llama

Llama est probablement le modèle que le grand public qualifie le plus facilement d’« open source ».

Il est effectivement :

- téléchargeable ;
- auto-hébergeable ;
- fine-tunable ;
- très largement réutilisé.

Mais :

- sa licence est spécifique à Meta ;
- les données complètes ne sont pas publiées ;
- toute la fabrication n’est pas reproductible.

La formulation la plus prudente est donc :

> **Llama est un modèle open weight sous licence communautaire Meta.**

---

## DeepSeek

DeepSeek-R1 est plus ouvert sur plusieurs dimensions :

- licence MIT ;
- poids ;
- code ;
- dérivés autorisés ;
- distillation autorisée ;
- importante documentation technique.

Mais il ne fournit toujours pas tout ce qui permettrait de reconstruire le modèle complet depuis les données initiales.

La formulation utile est :

> **DeepSeek-R1 est un modèle open weight très ouvert et très documenté, mais cela ne suffit pas à lui seul à démontrer une reproductibilité complète de bout en bout.**

---

# 9. Fine-tuning et accès aux poids

Le continuum permet également d’introduire rapidement le fine-tuning.

## Modèle fermé

Un fournisseur peut proposer du **fine-tuning via API**.

Dans ce cas :

> le modèle est adapté, mais l’opération reste contrôlée par le fournisseur.

## Open weight

À partir du moment où les poids sont disponibles, l’utilisateur peut réaliser un **fine-tuning autonome**.

Il peut choisir :

- son matériel ;
- son infrastructure ;
- son dataset ;
- son framework ;
- ses hyperparamètres ;
- LoRA / QLoRA / full fine-tuning ;
- ses évaluations.

La formulation correcte est donc :

> **L’open weight ne rend pas le fine-tuning possible ; il rend possible le fine-tuning autonome.**

---

# 10. Le rôle des données : au-delà de la reproduction

La transparence sur les données est importante pour comprendre :

- les langues représentées ;
- les cultures présentes ou absentes ;
- les biais possibles ;
- les domaines surreprésentés ;
- la période couverte ;
- l’origine des connaissances ;
- les données synthétiques utilisées ;
- les méthodes de filtrage ;
- les choix éditoriaux ;
- les questions de droits et de consentement.

Une formulation utile pour la présentation :

> **Les données ne disent pas ce que “pense” le modèle.  
> Elles renseignent sur le monde qu’on lui a donné à voir.**

---

# 11. Analogie culinaire appliquée à la fresque

| Élément IA | Analogie |
|---|---|
| Poids | Le plat terminé |
| Code et processus d’entraînement | La recette et le procédé de cuisson |
| Données | Les ingrédients |

On peut ensuite lire le continuum ainsi :

### Fermé / API
> Je commande le plat au restaurant.

### Open weight
> Je peux repartir avec le plat et le retravailler moi-même.

### Open weight ++
> J’ai le plat et une bonne partie de la recette.

### Open Source / ouverture de bout en bout
> J’ai le plat, la recette, les ingrédients et suffisamment d’informations pour refaire la cuisine.

---

# 12. Conclusion

La question utile n’est pas :

> **« Est-ce que ce modèle est ouvert ? »**

mais :

> **« Qu’est-ce qui est ouvert ? »**

Il faut regarder séparément :

- les poids ;
- la licence ;
- le code ;
- le processus d’entraînement ;
- les données ;
- les checkpoints ;
- les outils d’évaluation ;
- les droits de modification et de redistribution.

Le continuum :

> **Fermé / API → Open weight → Open weight ++ → Open Source**

n’est donc pas une échelle morale.

Il représente différents arbitrages entre :

- contrôle ;
- coût ;
- rentabilisation de la R&D ;
- adoption ;
- sécurité ;
- diffusion ;
- souveraineté ;
- auditabilité ;
- reproductibilité ;
- contribution.

---

# 13. Références générales

## Open Source AI Definition

Open Source Initiative — Open Source AI Definition :  
https://opensource.org/ai/open-source-ai-definition

FAQ OSAID et modèles utilisés pendant la phase de validation :  
https://opensource.org/ai/faq

## Logiciel libre

GNU / Free Software Foundation — Les quatre libertés :  
https://www.gnu.org/philosophy/free-sw.fr.html

## Modèles

OpenAI GPT-5.6 :  
https://openai.com/index/gpt-5-6/

OpenAI gpt-oss :  
https://openai.com/index/gpt-oss-model-card/

Anthropic Claude Fable :  
https://www.anthropic.com/claude/fable

Google Gemini 3.1 Pro :  
https://deepmind.google/models/gemini/pro/

Google Gemma 4 :  
https://ai.google.dev/gemma/docs/core/model_card_4

Meta Llama :  
https://ai.meta.com/resources/models-and-libraries/llama-downloads/

xAI Grok-1 :  
https://github.com/xai-org/grok-1

xAI Grok 4.6 :  
https://x.ai/news/grok-4-6

Microsoft Phi-4 :  
https://huggingface.co/microsoft/phi-4

DeepSeek-R1 :  
https://github.com/deepseek-ai/DeepSeek-R1

Qwen3 :  
https://qwenlm.github.io/blog/qwen3/

Mistral Medium 3.5 :  
https://docs.mistral.ai/models/mistral-medium-3-5-26-04

Mistral Small 4 :  
https://mistral.ai/news/mistral-small-4/

Luciole-23B :  
https://huggingface.co/OpenLLM-France/Luciole-23B-Base

OLMo :  
https://github.com/allenai/OLMo-core

Apertus :  
https://www.apertus-ai.org/

Pythia :  
https://github.com/EleutherAI/pythia

Amber :  
https://github.com/LLM360/amber-train

Amazon Nova :  
https://aws.amazon.com/nova/models/
