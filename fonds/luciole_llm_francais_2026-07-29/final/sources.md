---
title: Sources — Pourquoi je ne veux pas de Luciole
author: David LEGRAND
date: 2026-07-29
lang: fr-FR
---

## Objectif

Ce document liste les sources effectivement consultées pour la veille
« Luciole, LLM français » et regroupées dans `fiches_recherche/`. Chaque
entrée précise, quand c'est pertinent, ce qui en fait une source fiable
(auteur identifié, nature officielle ou académique, contenu daté) — ou au
contraire une réserve à garder en tête avant de citer un chiffre en
restitution.

## OpenLLM France et LINAGORA

- [openllm-france.fr](https://openllm-france.fr/) — page officielle du
  collectif, source primaire pour sa présentation et ses objectifs.
- [Manifeste OpenLLM France (GitHub)](https://github.com/OpenLLM-France/Manifesto)
  — texte fondateur publié par le collectif lui-même.
- [Création de la communauté francophone OpenLLM France (LinkedIn)](https://fr.linkedin.com/pulse/cr%C3%A9ation-de-la-communaut%C3%A9-francophone-openllm-france-maudet)
  — retour d'un membre identifié du collectif sur sa création.
- [OpenLLM France sur Hugging Face](https://huggingface.co/OpenLLM-France)
  — organisation officielle hébergeant les modèles publiés.
- [linagora.com](https://linagora.com/) et
  [linagora.com/en/mission](https://linagora.com/en/mission) — site officiel
  de l'entreprise porteuse du collectif.
- [Linagora (Wikipédia)](https://en.wikipedia.org/wiki/Linagora) — recoupement
  encyclopédique de l'historique de l'entreprise.
- [linagora.ai — communauté OpenLLM France](https://linagora.ai/fr/communaute/openllm-france)
  — page LINAGORA dédiée au collectif.

## Financement — Bpifrance et France 2030

- [Communiqué Bpifrance (presse.bpifrance.fr)](https://presse.bpifrance.fr/?p=225494)
  et [Bpifrance — nos partenaires France 2030](https://www.bpifrance.fr/nous-decouvrir/nos-partnaires/france-2030)
  — communication officielle de l'opérateur public.
- [Bpifrance engage 10 milliards d'euros pour l'IA (FrenchWeb)](https://www.frenchweb.fr/bpifrance-engage-10-milliards-deuros-sur-4-ans-pour-structurer-lecosysteme-ia-francais/451250)
  — recoupement presse spécialisée, daté.
- [Luciole-Training-Dataset (Hugging Face)](https://huggingface.co/datasets/OpenLLM-France/Luciole-Training-Dataset)
  — fiche officielle du jeu de données, mentionne explicitement le
  financement Bpifrance.

## Lucie, le lancement raté

- [Analyse du lancement manqué de Lucie (SIDE Blog, Alain Goudey)](https://alain.goudey.eu/side/2025/01/26/analyse-du-lancement-manque-de-lucie-llm-open-source-francais/)
  — analyse détaillée signée par un auteur identifié (enseignant-chercheur en
  marketing/innovation), publiée à chaud (janvier 2025) : source la plus
  substantielle sur les 5 reproches faits à Lucie.
- [OpenLLM France, LINAGORA, Luciole (GoodTech Info)](https://goodtech.info/openllm-france-linagora-luciole-modeles-fondations-ia-open-source/)
  — média spécialisé, recoupement sur le contexte Lucie → Luciole.
- [Collection Luciole LLM (Hugging Face)](https://huggingface.co/collections/OpenLLM-France/luciole-llm)
  et [Luciole-23B-Instruct-1.1 (Hugging Face)](https://huggingface.co/OpenLLM-France/Luciole-23B-Instruct-1.1)
  — model cards officielles.

## Cas d'usage et essai de Luciole

- [Luciole-Instruct-1.1 (Ollama)](https://ollama.com/OpenLLM-France/Luciole-Instruct-1.1),
  variantes [8B](https://ollama.com/OpenLLM-France/Luciole-Instruct-1.1:8B) et
  [1B](https://ollama.com/OpenLLM-France/Luciole-Instruct-1.1:1B) — pages
  officielles de distribution du modèle quantifié.
- [Luciole-23B-Instruct-1.1 (Hugging Face)](https://huggingface.co/OpenLLM-France/Luciole-23B-Instruct-1.1)
  — model card, cas d'usage documentés (RAG, fine-tuning) et réserve
  explicite des auteurs sur la validation avant intégration industrielle.
- [Utiliser des modèles Ollama depuis Hugging Face (documentation officielle)](https://huggingface.co/docs/hub/ollama)
- [Luciole-8B-Instruct-1.1 (Hugging Face)](https://huggingface.co/OpenLLM-France/Luciole-8B-Instruct-1.1)
  — modèle réellement testé lors de l'essai RAG concret (`decouverte.md`).

## Architecture Mamba et State Space Models

- [Mamba: Linear-Time Sequence Modeling with Selective State Spaces (arXiv, papier original)](https://arxiv.org/abs/2312.00752)
  — source primaire académique (Albert Gu, Tri Dao, décembre 2023).
- [A Visual Guide to Mamba and State Space Models](https://newsletter.maartengrootendorst.com/p/a-visual-guide-to-mamba-and-state)
  — vulgarisation par un auteur identifié, utile pour l'intuition mais
  secondaire par rapport au papier original.
- [What Is A Mamba Model? (IBM)](https://www.ibm.com/think/topics/mamba-model)
  — ressource éditoriale d'un acteur reconnu du secteur.
- [Achilles' Heel of Mamba (arXiv)](https://arxiv.org/pdf/2509.17514),
  [Exploring the Limitations of Mamba in COPY and CoT Reasoning (arXiv)](https://arxiv.org/pdf/2410.03810)
  et [Mimetic Initialization Helps State Space Models Learn to Recall (arXiv)](https://arxiv.org/pdf/2410.11135)
  — articles académiques sur les limites documentées de Mamba (rappel en
  contexte, tâches de copie), utilisés pour nuancer la réserve sur le RAG.
- [Jamba: A Hybrid Transformer-Mamba Language Model (arXiv)](https://arxiv.org/pdf/2403.19887)
  et [The rise of hybrid LLMs (AI21)](https://www.ai21.com/blog/rise-of-hybrid-llms/)
  — référence pour l'architecture hybride Transformer/Mamba reprise par
  Luciole 8B.

## CroissantLLM

- [CroissantLLM: A Truly Bilingual French-English Language Model (arXiv)](https://arxiv.org/abs/2402.00786)
  — source primaire académique (février 2024).
- [croissantllm (Hugging Face)](https://huggingface.co/croissantllm) —
  organisation officielle du modèle.
- [CroissantLLM, une percée en IA générative (CentraleSupélec)](https://www.centralesupelec.fr/croissant-llm-une-percee-en-ia-generative-realisee-par-le-laboratoire-mics)
  — communication officielle de l'établissement porteur.

## Paysage des LLM souverains européens

- [arXiv — Teuken-7B-Base & Teuken-7B-Instruct](https://arxiv.org/pdf/2410.03730)
  et [Teuken-7B-instruct (Hugging Face)](https://huggingface.co/openGPT-X/Teuken-7B-instruct-commercial-v0.4)
  — sources primaires pour Teuken/OpenGPT-X.
- [EuroLLM, le modèle open source qui pourrait redéfinir la place de l'Europe (actu IA)](https://intelligence-artificielle.developpez.com/actu/377272/EuroLLM-le-modele-open-source-qui-pourrait-redefinir-la-place-de-l-Europe-dans-la-course-mondiale-a-l-IA)
  — média spécialisé pour EuroLLM.
- [Europe's open-source AI pioneers (Techblog Finalist)](https://techblog.finalist.nl/blog/europes-open-source-ai-pioneers-10-groups-shaping-llms-under-eu-ai-act)
  et [Open Source AI Index](https://osai-index.eu/) — panoramas comparatifs
  de l'écosystème européen.
- [QuelLLM.fr — souverain](https://quelllm.fr/meilleur-llm/souverain),
  [français](https://quelllm.fr/meilleur-llm/francais) et
  [multilingue européen](https://quelllm.fr/meilleur-llm/multilingue-europeen)
  — **réserve** : média de comparaison sans auteur identifié sur les pages
  consultées. Utile pour un survol du paysage, mais chaque chiffre précis
  repris de ces pages a été recoupé avec la page officielle ou la model card
  du projet concerné avant citation.

## Licences

- [Apache License (Wikipédia)](https://en.wikipedia.org/wiki/Apache_License)
- [GNU AGPL v3 (texte officiel)](https://www.gnu.org/licenses/agpl-3.0.html)
- [CC-BY-SA 4.0 (Creative Commons, texte officiel)](https://creativecommons.org/licenses/by-sa/4.0/deed.fr)

Trois textes de licence officiels, utilisés pour expliquer les trois
licences distinctes sous lesquelles Luciole publie poids, scripts et corpus.
