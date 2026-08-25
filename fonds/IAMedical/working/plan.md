# Plan — Veille IA, médecine et évolution des paradigmes

Présentation Mini Manifest — **mercredi 26 août, 9h00**. Format ODP linéaire
(pas de Sozi, faute de temps). Cible : **10 minutes maximum**.

Ceci est le **plan** : structure des slides, idées-clés par slide, timing
indicatif. Le **script** (texte oral rédigé mot pour mot, prêt à être dit ou
mémorisé) reste à écrire à partir de ce plan, une fois la structure validée.

Convention de numérotation : pour chaque cas, `X.0` = slide image (déjà
présente dans `working/`), `X.1` = slide 4 idées.

---

## Slide de couverture — Titre

**Titre** : IA, médecine et évolution des paradigmes

**Accroche / sous-titre** : Jusqu'où va le paradigme des LLM ?

**Auteur** : David Legrand
**Contexte** : Mini Manifest — Développeur IA agentique
**Date** : 26 août 2026

**Durée estimée** : 10 s (annonce du titre, pas de script à dire au-delà)

---

## Slide 0 — Rappel de la veille précédente

**Image** : `green_by_ai.jpg`

**Script oral** :

> La dernière fois, on avait vu qu'il fallait décomposer le mot « IA » selon
> ses usages et ses impacts : AI for Brown, AI for Green, Green AI. Aujourd'hui,
> on va voir que dans le médical aussi, plusieurs formes d'IA très différentes
> se cachent derrière le même mot.

**Durée estimée** : 20 s

---

## Slide sommaire — Fresque des 4 cas

**Contenu** : une fresque/frise avec les 4 cas à venir, posée comme sommaire
visuel de la présentation — pas de nouvelle idée, juste la carte du chemin
qu'on va parcourir.

| # | Cas | Nature |
| --- | --- | --- |
| 1 | Dario Amodei | prédiction |
| 2 | o1-preview | modèle seul |
| 3 | Claude / Mythos | système agentique |
| 4 | Vaccination | IA spécialisée non-LLM |

**Script oral** :

> Quatre cas vont nous guider, dans cet ordre : une prédiction de Dario
> Amodei, ce qu'un modèle de raisonnement seul sait déjà faire avec
> o1-preview, ce qu'un système agentique fait de plus avec Claude et Mythos,
> et pour finir un contre-pied — une IA spécialisée qui n'a rien d'un LLM.

**Durée estimée** : 15 s

---

## Slide 1 — Dario Amodei, la prédiction

**Image** : `dario_amodei.jpeg`

**Script oral** :

> Dario Amodei, cofondateur et CEO d'Anthropic — l'entreprise derrière
> Claude —, ancien d'OpenAI, acteur majeur des travaux sur le scaling et la
> sécurité des modèles.
>
> En octobre 2024, dans son essai *Machines of Loving Grace*, il avance une
> hypothèse radicale : une « powerful AI » pourrait condenser plusieurs
> décennies de progrès biologique et médical en quelques années — la formule
> médiatique dit « guérir la plupart des maladies en 5 à 10 ans ».
>
> Point important : Amodei ne postule pas un paradigme différent des LLM
> actuels. Sa « powerful AI » reste dans la continuité : Transformer,
> scaling, post-training, outils, capacité d'action, parallélisation
> massive. Son image : un « country of geniuses in a datacenter ».
>
> La vraie question de cette présentation : est-ce seulement une prédiction
> spectaculaire, ou voit-on déjà des indices allant dans cette direction ?

**Durée estimée** : 60 s

---

## Slide 2.0 — o1-preview : le cas (image)

**Image** : `urgence.jpeg`

**Script oral** :

> Un préprint déposé en décembre 2024 — la publication finale dans *Science*
> n'arrivera qu'en 2026 — évalue o1-preview, un gros modèle généraliste de
> raisonnement, sur des cas cliniques réels aux urgences. Le titre médiatique
> dit « l'IA surpasse les médecins ». Regardons l'architecture réelle.

**Durée estimée** : 25 s

---

## Slide 2.1 — o1-preview : 4 idées

**Script oral** — 4 idées à l'écran :

1. **Résultat** : performances remarquables sur des cas cliniques réels
   (urgences), sans dispositif spécifique
2. **Architecture** : `Dossier clinique → Prompt → o1-preview → diagnostic`
   — **pas de RAG, pas d'outils, pas d'agent**
3. **Limites** : modèle fermé, taille et corpus non audités, étude
   américaine (pas de cadre RGPD), tâche textuelle contrôlée — le modèle ne
   voit pas et n'examine pas le patient
4. **Question** : si le modèle seul fait déjà ça, à quel moment le harness,
   le RAG et l'agentification deviennent-ils réellement utiles ?

**Durée estimée** : 45 s

---

## Slide 3.0 — Claude / Mythos : le cas (image)

**Image** : `mythos.webp`

**Script oral** :

> Après le modèle seul, une expérience qui ressemble beaucoup plus à la
> trajectoire imaginée par Amodei. Dans les travaux de conception de
> protéines publiés par Anthropic en août 2026, Claude — via Mythos, pas un
> Claude public ordinaire — travaille dans un environnement scientifique
> outillé.

**Durée estimée** : 25 s

---

## Slide 3.1 — Claude / Mythos : 4 idées

**Script oral** — 4 idées à l'écran :

1. **Contexte** : Claude/Mythos orchestre modèles scientifiques spécialisés,
   outils, calcul GPU, sous-agents, corpus — un système, pas un chat
2. **Boucle** : `raisonner → choisir une action → appeler une ressource →
   observer → itérer → optimiser`
3. **Résultat physique** : les protéines candidates sortent du numérique —
   des laboratoires les fabriquent et les testent réellement
4. **Message** : le LLM devient orchestrateur de modèles spécialisés, d'outils
   et de calcul — pas un oracle qui « sait tout »

**Durée estimée** : 50 s

---

## Slide 4.0 — Vaccination : le cas (image)

**Image** : `vaccination.jpg`

**Script oral** :

> Après le modèle seul, puis le système agentique, un contre-pied volontaire.
> Vous cherchez le LLM ? Il n'y en a pas.

**Durée estimée** : 15 s

---

## Slide 4.1 — Vaccination : 4 idées

**Script oral** — 4 idées à l'écran :

1. **Contre-exemple volontaire** : ni LLM, ni agent, ni RAG
2. **Méthode** : `données biologiques → deep learning spécialisé →
   prédiction de la réponse vaccinale`
3. **Message** : l'équation « IA = LLM = agent » est fausse — classification,
   régression, modèles spécialisés restent pertinents selon le problème
4. **Constat** : pour une prédiction bien définie sur des données
   biologiques structurées, un modèle spécialisé peut être plus naturel
   qu'un LLM

**Durée estimée** : 40 s

---

## Slide 5 — Dézoom : trois architectures côte à côte

**Script oral** :

> Récapitulons. o1 : un LLM généraliste de raisonnement, utilisé presque
> seul. Claude/Mythos : un LLM au centre d'un système agentique, qui
> orchestre outils, calcul et modèles spécialisés. Vaccination : du deep
> learning spécialisé, sans LLM. Et Amodei : une prospective qui extrapole
> très loin la montée en capacité et en action.
>
> La chronologie n'est pas « ancienne IA puis LLM puis agents puis
> disparition du reste ». En 2026, plusieurs familles coexistent.

**Durée estimée** : 40 s

---

## Slide 6 — Conclusion et question ouverte

**Script oral** :

> Le futur n'est probablement pas tout LLM. Il peut être composé de modèles
> généralistes pour raisonner et orchestrer, de modèles spécialisés pour
> prédire ou calculer, d'outils, d'humains et du monde physique.
>
> Jusqu'où le paradigme Transformer — prédiction de tokens, scaling,
> post-training, raisonnement au moment de l'inférence, outils — peut-il
> aller avant qu'une rupture de paradigme soit nécessaire ?
>
> On ne sait pas.

**Durée estimée** : 30 s

---

## Budget temps total

| Slide | Durée |
| --- | --- |
| Couverture — Titre | 10 s |
| 0 — Rappel | 20 s |
| Sommaire — Fresque des 4 cas | 15 s |
| 1 — Amodei | 60 s |
| 2.0 — o1 image | 25 s |
| 2.1 — o1 idées | 45 s |
| 3.0 — Mythos image | 25 s |
| 3.1 — Mythos idées | 50 s |
| 4.0 — Vaccination image | 15 s |
| 4.1 — Vaccination idées | 40 s |
| 5 — Dézoom | 40 s |
| 6 — Conclusion | 30 s |
| **Total** | **375 s ≈ 6 min 15** |

Marge confortable sous les 10 minutes — de la place pour respirer entre les
slides, ralentir sur Mythos (le cas le plus dense), ou absorber une question
en cours de route.

## Points de vigilance — rappel avant de monter l'ODP

- Ne pas présenter o1 comme un agent ReAct.
- Ne pas confondre date de publication *Science* (2026) et date réelle du
  travail o1-preview (préprint, décembre 2024).
- Ne pas transformer la prédiction d'Amodei en fait établi.
- Ne pas dire que Claude a conçu « un médicament prêt à l'emploi » — conception
  de protéines/binders puis validation expérimentale en laboratoire.
- Ne pas présenter le cas vaccinal comme un LLM — c'est le contre-exemple.
- Ne pas refaire un cours sur RAG / ReAct / agents.

## Sources à garder sous la main (Q&A)

- Amodei — *Machines of Loving Grace* : https://darioamodei.com/essay/machines-of-loving-grace
- o1-preview — préprint : https://arxiv.org/abs/2412.10849
- o1-preview — publication *Science* : https://doi.org/10.1126/science.adz4433
- Claude/Mythos — Anthropic : https://www.anthropic.com/research/Claude-accelerates-protein-design
- Vaccination — ASU News : https://news.asu.edu/20260820-science-and-technology-why-immune-responses-vaccines-vary-person-person
- Vaccination — publication : https://doi.org/10.1016/j.cpblue.2026.100088
