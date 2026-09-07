# Catalogue Ollama Pro — classification sur le continuum d'ouverture

## Constat de départ

Le catalogue **Ollama Cloud** (abonnement Pro, 20$/mois — catalogue complet + 3 modèles
cloud concurrents) liste les modèles suivants (relevé du 2026-09-07) :

| Modèle | Éditeur |
| --- | --- |
| deepseek-v4-flash / deepseek-v4-pro | DeepSeek |
| gemma4 | Google |
| glm-5.1 / glm-5.2 / glm-5.3 / glm-5.3-flash | Zhipu AI |
| gpt-oss:20b / gpt-oss:120b | OpenAI |
| kimi-k2.6 / kimi-k2.7-code / kimi-k3 | Moonshot AI |
| minimax-m2.7 / minimax-m3 | MiniMax |
| mistral-large-3 | Mistral AI |
| nemotron-3-nano / -super / -ultra | NVIDIA |
| qwen3.5:397b | Alibaba (Qwen) |

**Constat immédiat, avant même la classification détaillée** : aucun modèle du catalogue
Ollama Cloud n'est « Fermé/API » au sens de la fresque de cette veille — le « cloud » ici
désigne un hébergement distant d'Ollama pour des modèles trop gros pour tourner localement,
pas une fermeture de licence. Chaque modèle listé a des poids publiés quelque part (le plus
souvent Hugging Face). Ollama Cloud est structurellement une vitrine de modèles ouverts,
jamais de modèles propriétaires.

## Tableau de classification

| Modèle | Licence | Catégorie | Point de vigilance |
| --- | --- | --- | --- |
| DeepSeek V4 (Pro/Flash) | MIT | **Open weight++** | Cohérent avec DeepSeek-R1 déjà dans la fresque |
| Gemma4 | Apache 2.0 | **Open weight++** | Déjà dans la fresque (5.2) |
| GLM-5.1/5.2/5.3 | MIT (poids) + Apache 2.0 (code) | **Open weight++** | Voir nuance ci-dessous |
| gpt-oss 20b/120b | Apache 2.0 | **Open weight++** | Déjà dans la fresque (5.1) |
| Kimi K2.6 / K2.7-code | Modified MIT | **Open weight++** | Licence bien documentée |
| Kimi K3 | Licence distincte, non « Modified MIT » | **Open weight** (à vérifier) | Voir nuance ci-dessous |
| MiniMax M2 (historique) | MIT | Open weight++ | Antérieur au catalogue actuel |
| MiniMax M2.7 / M3 | Restreinte (autorisation écrite au-delà d'un seuil commercial) | **Open weight** | Voir nuance ci-dessous |
| Mistral Large 3 | Apache 2.0 | **Open weight** | Cohérent avec Mistral Medium 3.5 déjà dans la fresque |
| Nemotron 3 (nano/super/ultra) | NVIDIA Open Model License / OpenMDW-1.1 | **Open Source / bout en bout** | Le cas le plus ouvert du catalogue — voir ci-dessous |
| Qwen3.5:397b | Apache 2.0 | **Open weight++** | Cohérent avec Qwen3-235B déjà dans la fresque |

## Nuances qui méritent d'être développées à l'oral

### GLM (Zhipu AI) — la revendication « fully open source » à vérifier

Zhipu communique sur GLM-5.2 comme « **fully open source** ». Les sources trouvées confirment
poids MIT + code Apache 2.0 sur Hugging Face/GitHub — mais **aucune mention d'une publication
du dataset d'entraînement ou de la recette complète**, contrairement à Nemotron ou aux
modèles déjà classés Open Source dans la fresque (OLMo, Pythia, Amber).

> **C'est exactement le type de vigilance que porte le titre de cette veille** : « fully
> open source » dans la communication d'un éditeur ne garantit pas la présence des trois
> composantes (poids + code + données) — à ce stade des sources trouvées, GLM reste
> Open weight++, pas Open Source au sens strict, en attendant confirmation sur les données.

### MiniMax — un glissement de licence à observer

MiniMax M2 était sous MIT sans restriction. **M2.7 introduit une clause de licence
commerciale** (autorisation écrite requise au-delà d'un certain usage). C'est le mouvement
inverse de ce qu'on attendrait d'un éditeur cherchant l'adoption — et un parallèle direct
avec le cas Grok déjà noté dans la fresque :

> **L'histoire d'un éditeur n'est pas nécessairement une progression linéaire vers
> davantage d'ouverture.** Grok l'illustrait par génération (Grok-1 ouvert → Grok 4.6
> fermé) ; MiniMax l'illustre par un durcissement de licence à revenu/usage croissant,
> une variante du même phénomène.

### Kimi K3 — licence à vérifier avant restitution

Une source titre littéralement *« a license nobody actually read »* pour Kimi K3 (par
opposition au Modified MIT bien documenté de K2). C'est un signal explicite d'incertitude
dans la littérature elle-même — **à vérifier directement sur le dépôt Hugging Face/GitHub
avant toute restitution**, plutôt que de trancher sur la seule base de résumés secondaires.

### Nemotron (NVIDIA) — le cas le plus ouvert du catalogue, absent de la fresque initiale

C'est la trouvaille la plus intéressante de ce catalogue : NVIDIA publie pour Nemotron 3
**les poids, les données d'entraînement et les recettes** (pré-entraînement, post-entraînement,
environnements RL, plus de 10 000 milliards de tokens et 40 millions d'échantillons de
post-entraînement) — un niveau de transparence comparable à OLMo ou Amber, déjà classés
« Open Source / bout en bout » dans la fresque des 20 modèles.

**Nemotron mériterait d'être ajouté à la catégorie `open_source/` de la fresque** — il n'y
figure pas actuellement alors qu'il correspond le mieux à la définition, davantage que
plusieurs modèles déjà classés « Open weight++ » du catalogue.

## Ce que ce catalogue apporte à la veille

1. **Confirmation empirique du continuum** : un même outil (Ollama Cloud) héberge des
   modèles à différents niveaux d'ouverture, tous « ouverts » au sens large, mais pas de
   façon équivalente — exactement la thèse centrale de la fiche pédagogique principale.
2. **Un candidat sérieux pour enrichir la catégorie Open Source** (Nemotron), qui n'était
   représentée dans la fresque que par des acteurs académiques/associatifs (Ai2, EleutherAI,
   LLM360, OpenLLM France, Swiss AI) — NVIDIA y ajoutant un acteur industriel majeur change
   la lecture : l'ouverture de bout en bout n'est pas réservée aux structures non lucratives.
3. **Deux cas concrets de vocabulaire à surveiller** (GLM, MiniMax) qui viennent allonger la
   liste déjà ouverte par Llama et DeepSeek dans le document principal.

---

## Sources

- [Ollama Pricing](https://ollama.com/pricing)
- [GLM-5.2 Open Source: Zhipu's Answer to the US AI Block](https://pasqualepillitteri.it/en/news/4948/glm-5-2-fully-open-frontier-ai-us-block)
- [Kimi K3 Open Weights Are Live — licence non lue](https://roo.beehiiv.com/p/kimi-k3-open-weights-license-benchmarks)
- [GitHub — MoonshotAI/Kimi-K2](https://github.com/moonshotai/Kimi-K2)
- [MiniMax Revises License After Releasing M2.7 Weights](https://letsdatascience.com/news/minimax-revises-license-after-releasing-m27-weights-04b47c74)
- [NVIDIA Nemotron 3 Ultra: 550B Open-Weight Model](https://www.mindstudio.ai/blog/nvidia-nemotron-3-ultra-550b-open-weight-agent-model)
- [Nemotron AI Models — NVIDIA Developer](https://developer.nvidia.com/topics/ai/nemotron)
- [DeepSeek V4 Launch — Open-Weight Model of 2026](https://www.mindstudio.ai/blog/deepseek-v4-launch-specs-open-weight-2026)
- [Mistral Large 3: The 675B Open-Weight MoE Model](https://dev.to/jangwook_kim_e31e7291ad98/mistral-large-3-the-675b-open-weight-moe-model-developer-guide-250a)

**Vérification faite le 2026-09-07** via WebSearch/WebFetch. Classification basée sur des
résumés secondaires (blogs spécialisés, pas systématiquement les pages officielles éditeur) —
**à recontrôler sur les sources primaires (Hugging Face, GitHub, site éditeur) avant
restitution**, notamment pour GLM (données d'entraînement) et Kimi K3 (licence).
