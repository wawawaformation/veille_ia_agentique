# Bloc 2 — Le continuum d'ouverture en IA générative

**Durée cible** : 4 minutes

---

## Contexte : pourquoi l'IA complique la notion d'open source

Pour un logiciel traditionnel, le code source constitue l'élément central permettant de comprendre comment le programme fonctionne.

Un modèle de machine learning est radicalement différent.

Son comportement ne provient pas uniquement du programme qui l'exécute. Il résulte de **trois composantes distinctes** :

1. **Les poids du modèle** : les paramètres numériques appris pendant l'entraînement
2. **Le code et le processus d'entraînement** : architecture, prétraitement, hyperparamètres, algorithmes
3. **Les données d'entraînement** : le corpus sur lequel le modèle a appris

**Chacune de ces trois composantes peut être ouverte, fermée ou partiellement publiée indépendamment des deux autres.**

C'est cette multiplication de degrés d'ouverture qui crée le continuum.

---

## OSAID — la définition d'open source appliquée à l'IA

Avant d'explorer le continuum, une question : **qui décide si un modèle d'IA est « open source » ?**

L'**Open Source Initiative (OSI)**, créée en 1998 pour le logiciel, a développé en 2024 l'**Open Source AI Definition (OSAID)**.

### Principes clés de l'OSAID

Pour être certifié « open source » au sens OSAID, un modèle doit permettre les 4 libertés du logiciel libre, **mais appliquées à l'IA** :

1. **Utiliser** librement (Liberté 0) ✓
2. **Étudier et comprendre** comment fonctionne le modèle (Liberté 1) — nécessite poids + données + recettes
3. **Modifier** et réentraîner (Liberté 2) — impossible si données/code manquent
4. **Redistribuer** les modifications (Liberté 3)

### La distinction critique : open weight vs open source

**Conséquence majeure** :

- **Open weight** = poids publiés, mais données et code d'entraînement fermés
  - Tu peux **utiliser** ✓
  - Tu ne peux **pas réellement étudier ni modifier** (Liberté 1-3 bloquées)
  - **Exemple** : Llama, Mistral, DeepSeek

- **Open source** (au sens OSAID) = poids + données + code tous publiés
  - Tu peux **utiliser, étudier, modifier, redistribuer** ✓✓✓✓
  - **Exemple** : OLMo, Amber, Luciole, Nemotron

> **Conséquence du titre de la veille** : « Mistral est-il vraiment open source ? »
> **Réponse** : Non. Mistral est **open weight**. Pour être open source, il faudrait aussi publier les données et le code d'entraînement.

---

## Pourquoi cette distinction importe vraiment

Ce n'est pas une question administrative de cases cochées. Voici deux exemples concrets.

### Exemple 1 : Données cachées = biais invisibles

Imagine un modèle entraîné sur un dataset contaminé par la propagande d'un dictateur. Le modèle en hérite les biais.

**Avec open weight seul** : tu vois le poids, mais pas l'origine du biais. Tu ne peux même pas l'auditer.

**Avec open source** : tu accès aux données d'entraînement. Tu vois d'où ça vient, tu peux corriger.

→ **L'indépendance de penser dépend de la transparence de la fabrication.**

### Exemple 2 : Erreurs méthodologiques révélées

**Cas réel : Lucie (OpenLLM France, janvier 2025)**

- Lancée en version inachevée, non censurée, sans safeguards
- Erreurs flagrantes, réponses incohérentes
- La communauté open source l'a **vu et dénoncé**
- Forcé de corriger et d'améliorer

**Si Lucie était fermée** : personne n'aurait jamais su qu'il y avait ces problèmes méthodologiques.

→ **La transparence du processus permet à la communauté de corriger.**

---

## Les 4 catégories du continuum

### Catégorie 1 : Fermé / API

**Définition** : aucune composante n'est accessible. Seul un accès distant (API) est proposé.

**Caractéristiques** :
- Poids : fermés
- Code/processus : fermés
- Données : fermées
- Accès : API seulement (parfois avec restriction d'usage commercial)
- Liberté utilisateur : minimale (exécution seulement, via la plate-forme du fournisseur)

**Modèles de cette catégorie** :
- **GPT** (famille OpenAI : GPT-4, GPT-4o, etc.) — accès via API OpenAI payante
- **Claude** (famille Anthropic) — accès via API Anthropic payante
- **Gemini 3.1 Pro** (Google) — accès via Vertex AI
- **Grok** (xAI) — accès via Grok API
- **Amazon Nova 2 Pro** (AWS) — accès via Bedrock

**Apport pédagogique** :
> Aucun degré de liberté selon les 4 libertés FSF. Mais c'est un choix stratégique valide : ces entreprises investissent massivement dans la R&D et choisissent de monétiser via l'infrastructure cloud plutôt que de laisser les poids circuler.

---

### Catégorie 2 : Open weight

**Définition** : les poids sont publiés, mais pas le code/processus ni les données.

**Caractéristiques** :
- Poids : **publiés** (souvent sous licence permissive type Apache 2.0, MIT)
- Code/processus : **fermés** ou minimalement documentés
- Données : **fermées**
- Accès local : possible (tu peux télécharger et exécuter le modèle chez toi)
- Liberté utilisateur : **Utiliser** (Liberté 0) ✓ — **Étudier et modifier** (Liberté 1) ✗ (pas assez d'info)

**Modèles de cette catégorie** :
- **Llama 4 Maverick** (Meta) — 405B, flagship
- **Grok-1** (xAI) — le modèle open weight, pas l'API
- **Phi-4** (Microsoft) — petit modèle efficace
- **Mixtral 8×7B** (Mistral) — modèle MoE
- **Mistral Medium 3.5** (Mistral)

**Apport pédagogique** :
> « Open weight » n'est **pas** open source. Tu peux utiliser et redistribuer les poids, mais tu ne peux pas réellement étudier comment le modèle a été entraîné ni reproduire l'entraînement.
>
> Llama et Mistral, bien que très populaires et bien documentées, entrent techniquement dans cette catégorie.

---

### Catégorie 3 : Open weight++ (intermédiaire)

**Définition** : poids publiés + documentation significative du processus, mais pas l'accès complet aux données ni au code d'entraînement reproductible.

**Caractéristiques** :
- Poids : **publiés**
- Code/processus : **partiellement documentés** (plus de détails que open weight classique)
- Données : **partiellement documentées** (synthèse, pas accès complet)
- Liberté utilisateur : **Utiliser** (Liberté 0) ✓ — **Étudier** (Liberté 1 partielle) ≈ — **Modifier** très difficile

**Modèles de cette catégorie** :
- **gpt-oss-120b** — model open weights avec recettes de fine-tuning
- **Gemma 4 31B** (Google) — documentation détaillée du processus
- **DeepSeek-R1** (DeepSeek) — poids + rapport technique complet
- **Qwen3-235B** (Alibaba) — modèle MoE documenté
- **Mistral Small 4** (Mistral)

**Apport pédagogique** :
> Cette catégorie est celle où les entreprises trouvent un équilibre : assez transparent pour faire confiance, pas assez pour permettre une vraie reproduction indépendante.
>
> On peut étudier **davantage**, mais pas modifier vraiment (car on n'a pas les données complètes ni les outils de réentraînement).

---

### Catégorie 4 : Open source (au sens strict, OSAID)

**Définition** : poids + code + données **tous publiés** et librement modifiables.

**Caractéristiques** :
- Poids : **publiés**
- Code/processus : **complètement documenté et publicatif** (scripts d'entraînement reproductibles)
- Données : **publiées** (ou accès aux données de synthèse/entraînement)
- Liberté utilisateur : **toutes les 4 libertés FSF** ✓✓✓✓

**Modèles de cette catégorie** :
- **Luciole-23B** (OpenLLM France) — poids + données + code d'entraînement
- **OLMo 3 32B** (Allen Institute for AI) — 10B+ tokens de données publiés
- **Apertus 1.5 70B** (LLM360) — reproduction complète documentée
- **Pythia-12B** (EleutherAI) — modèles de recherche reproductibles
- **Amber-7B** (LLM360) — même approche qu'Apertus
- **Nemotron-3** (NVIDIA) — poids + données + recettes ouvertes

**Apport pédagogique** :
> C'est **ici et seulement ici** qu'on peut réellement appliquer les 4 libertés du logiciel libre.
>
> Quelques acteurs clés :
> - Académiques (AI2, EleutherAI, LLM360)
> - Associatifs (OpenLLM France)
> - **Industriels** (NVIDIA avec Nemotron démontre que l'ouverture complète n'est pas l'apanage des petits acteurs)

---

## Pourquoi cette distinction importe

### Cas d'usage : chercheur en reproducibilité
- **Fermé/API** : impossible d'audit, impossible de tester la robustesse
- **Open weight** : tu peux tester le modèle, mais pas comprendre comment il a été entraîné
- **Open weight++** : meilleure documentation, mais tu ne peux pas refaire l'entraînement
- **Open source** : tu peux **tout** auditer, reproduire, modifier

### Cas d'usage : entreprise cherchant l'indépendance technologique
- **Fermé/API** : totalement dépendant du fournisseur (coût, disponibilité, conformité)
- **Open weight** : tu peux auto-héberger, mais difficile de fine-tuner sérieusement
- **Open weight++** : meilleure documentation pour adaptation
- **Open source** : vraie indépendance, tu maîtrises tout le cycle

### Cas d'usage : contribution communautaire
- **Fermé/API** : aucune contribution possible
- **Open weight** : tu peux créer des outils pour l'inférence, mais pas améliorer le modèle
- **Open weight++** : tu peux proposer des adaptations
- **Open source** : tu peux contribuer directement au modèle de base

---

## Message clé du bloc 2

> **Le continuum montre que « ouvert » en IA ne signifie pas une seule chose.**
>
> Publier les poids n'est pas la même chose que publier le code et les données.
>
> Et c'est exactement pour ça que Llama et Mistral — bien que leurs poids soient accessibles — **ne satisfont pas la définition « open source » au sens de la Free Software Foundation ou de l'OSAID.**
>
> Dire « open source » est donc inexact. Dire « open weight » est plus précis. Et si tu veux vraiment de l'open source au sens historique, il faut aller jusqu'à la catégorie 4.

---

## Transition vers le bloc 3

Maintenant que tu comprends le continuum technique, une question réglementaire surgit : **comment les gouvernements définissent-ils « open source » pour l'IA ?**

L'Union européenne, avec l'AI Act, a donné une réponse. Et elle n'est pas celle qu'on attendrait...
