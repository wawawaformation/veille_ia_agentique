# Fiche — CroissantLLM

Matériau de travail (recherche du 2026-07-28), à retravailler pour `final/`.
Objectif : documenter le candidat retenu pour le prochain test (« terrain
équitable », Transformer pur, cf. `decouverte.md` — conclusion), déjà cité en
une ligne dans `fiche-paysage-llm-souverain-europeen.md`.

## Ce que c'est

Modèle de langage **1,3 milliard de paramètres**, entraîné sur **3 000
milliards de tokens anglais et français**, avec un ratio **1:1** entre les
deux langues — pas un modèle multilingue générique avec de l'anglais
dominant et un peu de français en plus, un modèle pensé **bilingue dès la
conception** (tokenizer dédié, jeux de données de fine-tuning bilingues).

Publié par le **laboratoire MICS de CentraleSupélec**, en collaboration avec
**Illuin Technology** (et des contributions Sorbonne Université, Carnegie
Mellon parmi les 16 auteurs, dont Manuel Faysse, Pierre Colombo, Antonio
Loison...) — article *"CroissantLLM: A Truly Bilingual French-English
Language Model"* (février 2024). Entraîné sur le supercalculateur **Jean
Zay**. Décrit comme "le modèle francophone le plus performant pour sa
taille", pensé en cohérence avec l'AI Act, usage commercial autorisé (données
d'entraînement comme modèle).

## Corpus français

Le corpus français (303 milliards de tokens) est **manuellement curé** —
sources variées : données internet, littérature, documents juridiques,
articles scientifiques. Contraste avec beaucoup de modèles "multilingues"
où le français n'est qu'une fraction résiduelle d'un corpus anglo-centré.

## Pourquoi il convient bien au prochain test

- **Frugalité revendiquée comme argument central, pas un effet de bord** :
  la page CentraleSupélec le décrit comme fonctionnant sur **CPU et même
  téléphone**, précisément parce qu'il est très compact — contrairement à
  Luciole (8B) ou Apertus (70B). Bon candidat pour un test sur `cloclo` sans
  les soucis de RAM/latence rencontrés.
- **Disponible en GGUF/GGML** sur Hugging Face — compatible avec le même
  type d'outillage local (llama.cpp) que Luciole, donc comparaison sur un
  terrain technique équivalent (à vérifier : présence ou non dans la
  bibliothèque officielle Ollama, sinon import GGUF manuel).
- **Plusieurs variantes disponibles** : base (`CroissantLLMBase`), chat
  (plusieurs quantifications), et même des modèles de traduction dédiés
  (`CroissantLLM_ft_translation_correction`) — 55 modèles au total sur le
  compte Hugging Face de l'organisation.
- **Architecture Transformer pur** (cf. note déjà présente dans
  `fiche-paysage-llm-souverain-europeen.md` : "Llama-based") — donc pas de
  facteur confondant Mamba/outillage immature comme avec Luciole : un test
  de latence ici mesurerait un Transformer classique, comparable
  directement à Mistral.

## Limite à garder en tête

1,3B est très petit comparé à Luciole (8B/23B) ou Mistral (7B) — la
comparaison de latence sera favorable presque par construction (moins de
paramètres = moins de calcul). Utile pour un test de faisabilité RAG rapide
et sobre, mais pas un comparatif à paramètres égaux avec Mistral 7B ou
Luciole 8B. À nommer explicitement si présenté comme point de comparaison,
pour ne pas laisser croire à un test toutes choses égales par ailleurs.

## Illustration

`croissantllm_centralesupelec.png` — photo de l'équipe (laboratoire MICS),
chacun tenant un croissant, publiée sur l'article CentraleSupélec cité en
source. Clin d'œil assumé au nom du modèle, utile pour une slide de
conclusion vivante plutôt qu'un simple mur de texte.

## Sources

- [CroissantLLM: A Truly Bilingual French-English Language Model (arXiv)](https://arxiv.org/abs/2402.00786)
- [croissantllm (Hugging Face)](https://huggingface.co/croissantllm)
- [CroissantLLM, une percée en IA générative réalisée par le laboratoire MICS (CentraleSupélec)](https://www.centralesupelec.fr/croissant-llm-une-percee-en-ia-generative-realisee-par-le-laboratoire-mics)
