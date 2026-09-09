# Bibliographie — Veille Mistral est-il vraiment open source ?

## Ollama — Pricing et modèles

- [Ollama Cloud Pricing — page officielle](https://ollama.com/pricing)
- [Ollama Cloud Pricing 2026 : plans et peak hours](https://pooyagolchian.com/blog/ollama-cloud-pricing-hardware-requirements-2026/)
- [Ollama Cloud TPS pricing details](https://ollamatps.com/pricing/)
- [Ollama Cloud vs Claude & GPT: Cost 2026](https://pooyagolchian.com/blog/ollama-cloud-vs-claude-gpt-cost-2026/)

## Ollama — Modèles et vision

- [Best Ollama Vision Models 2026 — Serverman](https://www.serverman.co.uk/ai/ollama/best-ollama-models-for-vision/)
- [Ollama Vision Models 2026 — PromptQuorum](https://www.promptquorum.com/prompt-bites/which-ollama-models-support-vision)
- [Build OCR System with Ollama Vision Models](https://markaicode.com/build-ocr-system-ollama-vision-models/)

## Open Source AI Definition (OSAID)

- [Open Source AI Definition (OSAID) — Open Source Initiative](https://opensource.org/deepdive/open-source-ai-definition)
- [OSI Open Source Definition](https://opensource.org/osd/)
- [Free Software Definition — Free Software Foundation](https://www.gnu.org/philosophy/free-sw.html)

## Infomaniak — alternative souveraine

- [Infomaniak Trust Center — conformité RGPD & sécurité](https://www.infomaniak.com/en/trust-center)
- Liste des modèles : appel direct `GET https://api.infomaniak.com/2/ai/{id}/openai/v1/models` (source primaire, vérifiée par David le 2026-09-08 — pas la doc, l'API elle-même) : 8 modèles de génération (Ministral-3-14B, Qwen3.5-122B/397B, Gemma-4-31B, Kimi-K2.6, Nemotron-3-Nano-30B, Mistral-Small-4-119B, Apertus-v1.5-70B) + 3 modèles d'embedding
- [Infomaniak Developer Portal — doc de l'endpoint](https://developer.infomaniak.com/docs/api/get/1/ai/models)
- Suisse : décision d'adéquation de la Commission européenne (LPD révisée reconnue équivalente RGPD depuis septembre 2023) — pas de clauses contractuelles supplémentaires nécessaires pour transfert UE↔Suisse

## AI Act et réglementation

- [AI Act — European Commission](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai)
- [AI Act Article 2(12) — exemption open source](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1689)
- [AI Act Article 51(2) — seuil risque systémique (10²⁵ FLOPs)](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1689)
- [What Open-Source Developers Need to Know about the EU AI Act's Rules for GPAI Models — Hugging Face](https://huggingface.co/blog/yjernite/eu-act-os-guideai) — **source clé, vérifiée le 2026-09-08** : détaille précisément ce dont l'open source est exempté (art. 53(1)(a-b) documentation technique, art. 54 représentant UE) et ce qui reste obligatoire (art. 53(1)(c) politique copyright, art. 53(1)(d) résumé du contenu d'entraînement), plus les 3 conditions d'éligibilité (licence libre, paramètres/architecture publics, **non-monétisation**). Corrige une erreur initiale de cette veille qui affirmait « aucune exigence sur les données » côté AI Act.
- [Article 2: Scope — EU Artificial Intelligence Act (texte annoté)](https://artificialintelligenceact.eu/article/2/)
- [Llama-3 405B specifications and FLOP count — Meta](https://www.llama.com/docs/llama-3-1/)

## Logiciel libre et standards ouverts

- [Four Freedoms of Free Software — Richard Stallman, FSF](https://www.gnu.org/philosophy/free-sw.html)
- [Free Software Foundation — About FSF](https://www.fsf.org/about)
- [Open Source Initiative — History and mission](https://opensource.org/)
- [RFC - Request for Comments — IETF](https://www.ietf.org/standards/rfc/)
- [Standards and open specifications — W3C, OASIS](https://www.w3.org/)

## Frugalité énergétique et efficacité inférence

- [arXiv 2507.11417 — Local vs API inference energy comparison](https://arxiv.org/abs/2507.11417)
- [PUE (Power Usage Effectiveness) — datacenter efficiency](https://en.wikipedia.org/wiki/Power_usage_effectiveness)
- [Batching and inference optimization — Hugging Face](https://huggingface.co/docs/transformers/v4.30.0/perf_infer_gpu_inference)
- [Jevons Paradox — economic efficiency and consumption](https://en.wikipedia.org/wiki/Jevons_paradox)
- [GPT-4o energy consumption estimation — OpenAI research](https://openai.com/research)

## Modèles d'IA mentionnés

### Open weight
- Llama series (Meta)
- Mistral series (Mistral AI)
- DeepSeek series (DeepSeek)
- Qwen series (Alibaba)
- Grok-1 (xAI)

### Open source (poids + données + code)
- OLMo (Allen Institute for AI)
- Amber / Apertus (LLM360)
- Luciole (OpenLLM France)
- Nemotron (NVIDIA)
- Pythia (EleutherAI)

### Fermé/API
- GPT (OpenAI)
- Claude (Anthropic)
- Gemini (Google)
- Amazon Nova (AWS)
