# Open weight = plus frugal ? Une idée reçue à nuancer

## L'idée reçue

Un raccourci fréquent dans la veille IA : « open weight → exécution locale → plus écologique
que l'API ». Ce raccourci ne tient pas à l'examen — la réalité dépend surtout du **taux
d'utilisation du matériel**, et un facteur bien plus déterminant que le lieu d'exécution
domine largement le débat : **l'effet rebond**.

## Ce que montrent les études récentes

### Le seuil qui inverse le résultat : le taux d'utilisation

> **L'infrastructure cloud mutualisée reste la plus efficace par token pour des
> organisations dont la charge coexiste avec d'autres utilisateurs. Une infrastructure GPU
> dédiée n'atteint le niveau d'efficacité du cloud qu'au-dessus d'environ 85 % de taux
> d'utilisation soutenu — en dessous, du matériel edge très efficient (type Apple Silicon)
> est plus soutenable.**

Concrètement : un GPU personnel qui tourne occasionnellement (la plupart des usages
individuels) a un mauvais rendement énergétique par rapport à un datacenter mutualisé qui
sert des milliers d'utilisateurs en continu. Mais un edge device très optimisé, utilisé pour
un modèle de taille adaptée, peut inverser ce constat.

**Ce n'est donc pas « local vs cloud » qui tranche, c'est « quel taux d'utilisation, sur
quel matériel, pour quel modèle ».**

### Le poids du refroidissement (PUE)

Le PUE (Power Usage Effectiveness) des datacenters IA se situe entre **1,05 et 1,40**
(intervalle P5–P95), avec un surcoût de refroidissement de l'ordre de **1,3 à 1,5×** par
rapport à la seule consommation de calcul. C'est un coût réel mais qui reste inférieur à
l'écart d'efficacité entre un GPU sous-utilisé et un GPU exploité à pleine charge.

### Le batching : un vrai levier, indépendant du lieu

- Le *continuous batching* réduit la consommation d'environ **5 %** par rapport au batching
  statique hors-ligne.
- La combinaison optimisation de modèle + batching + réglage infrastructure permet des
  réductions de **8 à 20×** l'énergie par requête par rapport à un déploiement naïf.
- Des moteurs d'inférence optimisés (vLLM/PagedAttention, TensorRT-LLM, DeepSpeed) surpassent
  un Transformer vanilla de **25 à 55 %** en énergie par token, surtout à fort batch size.

**Le batching est un avantage structurel du datacenter mutualisé** : plus il y a de
requêtes simultanées à traiter, plus il est facile à rentabiliser. Un usage local individuel
ne peut quasiment jamais batcher.

### Edge CPU vs GPU : des chiffres qui trompent si mal lus

Une étude compare l'efficacité énergétique brute :
- **CPU edge** (3–6 W) : 0,54 à 2,38 tokens/J
- **GPU** (40–700 W) : 0,06 à 0,86 tokens/J

Le CPU edge paraît plus efficace par joule — **mais cette comparaison n'a de sens que si
les deux exécutent un modèle de taille comparable pour une tâche comparable**, ce qui est
rarement le cas : un edge device tourne un modèle minuscule et quantifié, pas le même modèle
qu'un GPU de datacenter. Le vrai levier de frugalité n'est pas le matériel, c'est la
**taille du modèle choisie pour la tâche**.

## Le vrai facteur dominant : l'effet rebond (paradoxe de Jevons)

C'est le point le plus important, et il dépasse largement la question local/API :

> **Rendre l'inférence moins chère (par optimisation cloud ou par modèle local léger)
> encourage à l'utiliser davantage. Le gain d'efficacité par requête est souvent effacé par
> l'explosion du volume d'usage.**

Exemple chiffré : une requête GPT-4o consomme environ 0,43 Wh. À l'échelle de 700 millions
de requêtes/jour, cela équivaut à l'électricité consommée par ~35 000 foyers américains, et
une empreinte carbone qu'il faudrait une forêt de la taille de Chicago pour compenser.

**Optimiser l'inférence (locale ou cloud) sans questionner le volume d'usage ne réduit pas
nécessairement l'impact total — ça peut même l'aggraver en rendant l'usage plus accessible.**

## Message à retenir pour la veille

> **« Open weight, donc exécuté localement, donc plus frugal » est un raccourci faux dans sa
> généralité. Ce qui compte réellement : le taux d'utilisation du matériel, la taille du
> modèle choisie pour la tâche — et, plus largement, si l'accessibilité gagnée en efficacité
> ne se traduit pas par un usage démultiplié qui annule le gain.**

Ce point recoupe directement le contraste **GPT ↔ gpt-oss** et **Gemini ↔ Gemma** déjà
présents dans la fresque : la question n'est pas seulement « qui a les poids », mais aussi
« sur quelle infrastructure, à quelle échelle, ce modèle tourne-t-il réellement ».

---

## Sources

- [LLM Inference Energy Use — Emergent Mind](https://www.emergentmind.com/topics/llm-inference-energy-consumption)
- [Quantifying the Energy Consumption and Carbon Emissions of LLM Inference via Simulations (arXiv 2507.11417)](https://arxiv.org/pdf/2507.11417)
- [Energy use of AI inference, efficiency pathways, and test-time scaling — ScienceDirect](https://www.sciencedirect.com/science/article/pii/S2542435126001145)
- [AI Inference Power Consumption and GPU Electricity Costs: 2026 Guide — Spheron](https://www.spheron.network/blog/ai-inference-power-electricity-cost-2026/)
- [Electricity Demand and Grid Impacts of AI Data Centers (arXiv 2509.07218)](https://arxiv.org/html/2509.07218v3)
- [From Efficiency Gains to Rebound Effects: The Problem of Jevons' Paradox in AI's Polarized Environmental Debate (arXiv 2501.16548)](https://arxiv.org/html/2501.16548v1)
- [How Hungry is AI? Benchmarking Energy, Water, and Carbon Footprint of LLM Inference (arXiv 2505.09598)](https://arxiv.org/html/2505.09598v1)

**Vérification faite le 2026-09-07** via WebSearch — chiffres issus de préprints arXiv
récents (2025-2026), à recouper avec des sources publiées/peer-reviewed si utilisés en
restitution formelle.
