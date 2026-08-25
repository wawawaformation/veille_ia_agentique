# Script oral — IA, médecine et évolution des paradigmes

Restitution Mini Manifest — **mercredi 26 août 2026, 9h00**.
Support : `ia-medecine-evolution-paradigmes.odp` (12 slides).

**Cible : 9 à 10 minutes.** État actuel : **1 435 mots — 11 min 44**, calculé au
débit réel mesuré le 25/08 (130 mots/min, slide 9 chronométrée à 86 s).

Chaque slide se termine par un repère `⏱ **Fin de slide → m:ss**` : c'est l'heure
à laquelle tu dois avoir fini de la dire. Si tu es en retard, les deux endroits
les plus élastiques sont les cartes 3 des slides 6 et 8.

Convention : `[…]` = indication de scène, pas à dire. Le texte en clair est ce
qui se dit.

---

## Slide 1 — Couverture · 6 s

*À l'écran : titre + « Jusqu'où va le paradigme des LLM ? »*

Bonjour à tous. Dans cette veille, on va parler d'IA et de médecine.

*[Enchaîner directement, ne pas laisser de silence. Le sous-titre à l'écran pose
la vraie question, pas besoin de la dire.]*

⏱ **Fin de slide → 0:06**

---

## Slide 2 — Rappel d'une veille précédente · 57 s

*À l'écran : « Rappel : AI for Brown/Green et Green in AI » + schéma*

*[Ton léger, presque de la confidence. C'est le moment où on sourit.]*

D'abord, une remarque sur mes veilles. Je crois que je suis devenu un empêcheur
de tourner en rond — la Cassandre du groupe. Je vous parle de l'AI Act, du RGPD,
des turbines à gaz, de *Black Mirror*.

Bref, quand je passe, c'est pour vous expliquer ce qu'il ne faut pas faire et
comment tout va mal.

*[Petite pause. Puis, plus franc.]*

Aujourd'hui, pour une fois, non. Mais je reste dans mon thème : je prends un
domaine où l'IA est franchement du bon côté — la médecine.

Avant ça, un rappel : lors d'une précédente veille, on avait parlé de
consommation des data centers, d'effet rebond, d'IA frugale. Et on avait évoqué
AI for Brown, AI for Green, Green in AI. Là, on est dans les bénéfices.

⏱ **Fin de slide → 1:02**

---

## Slide 3 — Une prédiction, trois cas · 36 s

*À l'écran : frise avec les 4 cartes, titres seulement*

*[Slide sommaire. Annoncer le plan, pas argumenter. Débit tranquille.]*

Au sommaire, trois temps.

D'abord **une prédiction**, faite en 2024. Un oracle, si vous voulez.

Ensuite **trois expériences médicales**, toutes postérieures, qui vont chacune
essayer de confirmer ou d'infirmer cet oracle : un modèle de raisonnement lâché
sur des cas cliniques, un système agentique qui conçoit des protéines, et une
prédiction de réponse vaccinale.

Et pour finir, **on analyse** : qu'est-ce qui reste vrai dans les trois cas, et
qu'est-ce qu'on peut en garder comme invariant ?

⏱ **Fin de slide → 1:38**

---

## Slide 4 — Dario Amodei, la prédiction · 95 s

*À l'écran : portrait + « Dario Amodei » + « La prédiction — Octobre 2024 » +
3 lignes (plus de mention Anthropic/OpenAI, c'est dit à l'oral)*

*[Regarder la salle, pas l'écran. Vraie question — le nom est affiché, mais son
rôle, non. Laisser vraiment répondre.]*

Est-ce que vous savez qui est ce monsieur ?

*[Laisser deux ou trois secondes. Rebondir sur ce qui vient.]*

Oui, c'est écrit. C'est aussi le patron d'Anthropic, et un ancien d'OpenAI.

Octobre 2024, il publie un essai : *Machines of Loving Grace*. Ça ne parle pas
que de médecine — mais moi je ne prends que la santé.

Son image, un concept très fort : « un pays de génies dans un datacenter ». Un
truc qui dépasse des prix Nobel, travaille tout seul pendant des semaines, et
qui existe en millions de copies en parallèle.

Et ce qu'il en déduit — accrochez-vous : cinquante à cent ans de progrès médical
condensés en cinq à dix ans. 95 % des cancers éliminés, espérance de vie
doublée.

*[Pause. Baisser d'un ton.]*

Et pour être honnête jusqu'au bout — parce que ce serait trop facile de
m'arrêter là : lui-même écrit que *« tout ça pourrait très facilement être
faux »*, et que son calendrier ne repose *« sur aucune méthodologie
rigoureuse »*. Donc voilà. C'est une prospective, pas un résultat.

Moi, ce que j'aimerais savoir, c'est : est-ce qu'il vend son truc, ou est-ce
qu'on voit déjà des indices ?

⏱ **Fin de slide → 3:13**

---

## Slide 5 — o1-preview : le cas · 53 s

*À l'écran : photo urgences + « Le modèle seul — Préprint déc. 2024 → Science 2026 »*

Premier cas. Une équipe de Harvard et d'un hôpital de Boston met un gros modèle
de raisonnement à l'épreuve sur le métier de médecin : diagnostic,
probabilité, prise en charge. Noté par des médecins experts, avec des grilles
validées, publié dans *Science*. Donc pas une démo de chatbot — une évaluation
clinique.

Un détail que j'aime bien : le préprint disait « performance **surhumaine** ».
Dans *Science*, le mot a disparu du titre, mais il est resté dans le texte. Je ne
sais pas pourquoi ils ont fait ça.

La presse titrait « l'IA surpasse les médecins ». Entrons dans les détails.

⏱ **Fin de slide → 4:05**

---

## Slide 6 — o1-preview : les 4 idées · 75 s

*À l'écran : 4 cartes numérotées, bleu*

**[Item 1 · Résultat — Performances « superhuman » sur des cas réels]**

Le résultat. Je prends le chiffre le plus parlant : on demande au
modèle d'estimer la probabilité d'une maladie après un test positif. Et on le
compare à GPT-4 — l'état de l'art à l'époque — et à plus de 500 médecins.

Sur l'ischémie cardiaque — l'infarctus — le modèle se trompe de **6 %**. GPT-4 et
les médecins, de **56 %**.

Environ dix fois moins d'erreur que les humains. Voilà ce qui donne un contenu
réel au mot « surhumain ».

**[Item 2 · Architecture — Dossier clinique → Prompt → o1-preview → Diagnostic]**

L'architecture, et c'est là que ça nous concerne. Le flux, c'est : dossier
clinique, prompt, modèle, diagnostic. C'est tout. Pas de RAG, pas de
fine-tuning, pas d'outils. **Rien n'indique un agent derrière.**

**[Item 3 · Limites — Modèle fermé · étude US · aucun examen physique]**

Les limites, et là je vous parle technique : c'est un **modèle fermé**. Pas de
poids, pas de dataset à examiner. Donc rien à auditer — on croit sur parole.

**[Item 4 · Question — Si le modèle seul suffit déjà... pourquoi un agent ?]**

D'où la question, directe pour nous : si le modèle seul atteint ce niveau, quand
est-ce qu'un harness devient vraiment nécessaire ?

⏱ **Fin de slide → 5:20**

---

## Slide 7 — Claude / Mythos : le cas · 49 s

*À l'écran : logo Claude Mythos + « Le système agentique — Anthropic, août 2026 »*

Deuxième cas, on change de registre. Août 2026, Anthropic publie des travaux de
conception de protéines.

*[Contexte simple — ce n'est pas notre métier, ne pas le supposer connu.]*

Le but : fabriquer une protéine qui vient se coller sur une cible précise. Une
clé taillée pour une seule serrure — sauf qu'elle ne sert pas à ouvrir. Elle
sert à **bloquer**. On neutralise la cible, et la maladie avec.

C'est le principe de beaucoup de médicaments récents — en cancérologie, dans les
maladies auto-immunes.

Et le problème du domaine, c'est que fabriquer ces clés, ça rate la plupart du
temps. Retenez ça.

Un point technique à ne pas laisser passer à propos du LLM : ce n'est **pas** un
Claude grand public. C'est Mythos Preview, surtout — un modèle de recherche.
Aucun abonnement ne reproduit ce dispositif.

Ici, on est enfin très proche de ce que le fondateur d'Anthropic décrivait.

⏱ **Fin de slide → 6:10**

---

## Slide 8 — Claude / Mythos : les 4 idées · 74 s

*À l'écran : 4 cartes numérotées, orange*

**[Item 1 · Contexte — Mythos = un système, pas un chat]**

Ce n'est pas une conversation avec un modèle. C'est tout un
**écosystème**. Autour de Claude : des modèles scientifiques spécialisés, un
corpus, des sous-agents, et surtout du calcul — jusqu'à **12 500 heures de GPU
H100**.

**[Item 2 · Boucle — Raisonner → Agir → Observer → Itérer]**

La boucle ReAct, vous la connaissez. Ce qui compte c'est l'échelle : le
système opère seul pendant 48 heures, sur quinze cibles en parallèle.

**[Item 3 · Résultat physique — Protéines fabriquées et testées en labo]**

Et là, le plus important : ça finit dans un laboratoire médical.

En général c'est **10 à 15 %** de réussite dans le domaine. Là, on monte à
**35 %**. Donc ça rate encore deux fois sur trois.

Mais au bout, il reste **354 protéines qui marchent** — fabriquées et testées
pour de vrai, par deux laboratoires indépendants d'Anthropic.

Des protéines, pas des médicaments : bien sûr, il reste les essais cliniques à
faire. Cinq à dix ans à prévoir.

**[Item 4 · Message — Le LLM devient orchestrateur]**

Le message : la valeur ne vient pas du LLM seul, mais de
**l'écosystème qu'il orchestre**.

⏱ **Fin de slide → 7:23**

---

## Slide 9 — Vaccination : le cas · 86 s

*À l'écran : photo vaccination + « L'IA non-LLM — ASU / Cell Press Blue, août 2026 »*

Troisième cas. Août 2026 aussi.

*[Poser la prémisse — ce n'est pas évident pour tout le monde.]*

Le point de départ : **un vaccin ne marche pas pareil chez tout le monde**.
Selon les vaccins, quelques pourcents de gens ne développent quasiment pas de
défenses. Et chez les immunodéprimés — greffés, chimio — c'est beaucoup plus
fréquent. Le problème, c'est qu'aujourd'hui on s'en aperçoit après. On vaccine,
et on voit.

Cette étude, elle, prédit la force de la réponse **avant** l'injection.

*[Pause. Regarder la salle.]*

Vous cherchez le LLM ?

*[Pause.]*

Il n'y en a pas. C'est du **machine learning** — un modèle de deep learning
entraîné pour cette tâche, et rien d'autre.

⏱ **Fin de slide → 8:50**

---

## Slide 10 — Vaccination : les 4 idées · 58 s

*À l'écran : 4 cartes numérotées, violet*

**[Item 1 · Contre-exemple — Ni LLM, ni agent, ni RAG]**

Un contre-exemple, pour ce troisième cas, choisi exprès. Ce n'est ni un LLM, ni
un agent, ni un RAG. Rien de ce qu'on apprend en ce moment.

**[Item 2 · Méthode — Données bio → Deep learning spécialisé → Prédiction]**

La méthode : un modèle de deep learning entraîné sur des données sanguines, qui
fait de la **prédiction**. Une entrée, un modèle, une sortie.

Et le résultat marquant n'est pas celui qu'on attend. Que des malades
répondent mal, on le savait. Le modèle montre que **5 à 6 % des gens en bonne
santé** répondent mal aussi.

**[Item 3 · Message — IA ≠ LLM ≠ agent]**

Le message : la mode veut que « IA = LLM = agent ». Cette affirmation est
fausse.

**[Item 4 · Constat — Un modèle spécialisé peut suffire — et consomme moins]**

Sur un problème bien défini, un modèle spécialisé est plus naturel
qu'un LLM. Et — je referme la boucle avec ma slide du début — **il consomme
beaucoup moins**.

⏱ **Fin de slide → 9:47**

---

## Slide 11 — Ce qu'on a vu · 44 s

*À l'écran : frise complète avec Nature / Idée clé / Question + bandeau Fil rouge*

Analysons un peu ce qu'on a vu.

La prédiction : de la prospective, assumée comme telle par son auteur.

o1 : un LLM utilisé quasiment seul, déjà mieux calibré que des médecins sur le
raisonnement probabiliste — mais irrégulier ailleurs.

Claude et Mythos : le même type de modèle, mais au centre d'un système
agentique, validé physiquement en laboratoire.

La vaccination : du deep learning spécialisé, sans aucun LLM.

*[Ralentir sur la phrase suivante — c'est le fil rouge.]*

Et ce n'est pas une succession. Pas « l'ancienne IA, puis les LLM, puis les
agents, et le reste disparaît ». En 2026, ces familles **coexistent**.

⏱ **Fin de slide → 10:32**

---

## Slide 12 — Conclusion et question ouverte · 72 s

*À l'écran : « Le futur n'est probablement pas tout LLM. » + question + « On ne sait pas. »*

En conclusion, je garde deux invariants.

**Premier invariant : l'écosystème avant le modèle.** Les protéines produites
dans le deuxième cas ne sortent pas d'un modèle plus gros, elles sortent d'une
orchestration. Donc ma question de départ n'est plus « quel modèle », mais
« quel écosystème autour du modèle ».

**Deuxième invariant : calibrer à la tâche.** On n'a pas besoin d'un Opus 5 ou
d'un GPT-5.6 Sol pour extraire une date — les deux éditeurs proposent des gammes
entières pour ça. Et parfois, la bonne réponse n'est même pas un LLM (deep learning, jara ...etc) . Le réflexe
« je prends le plus gros » coûte de l'argent et du carbone pour rien.

*[Pause. Puis plus lentement pour la fin.]*

Reste la question que je ne tranche pas : jusqu'où ce paradigme peut-il aller
avant qu'une rupture soit nécessaire ? Les cas donnent des indices dans les deux
sens.

Honnêtement — on ne sait pas.

Merci. Je prends vos questions — auxquelles je ne saurai probablement pas
répondre.

⏱ **Fin de slide → 11:44**

---

## Budget temps

Mesuré sur le texte réellement prononcé : **1 486 mots** (contre 2 106 au premier
jet, soit −29 %).

**9 min 54 à 150 mots/minute · 9 min 17 à 160.** Dans le format.

Cumul calculé à 150, le débit le plus probable pour ce texte :

| Slide                      | Mots | Durée | Cumul    |
| -------------------------- | ---- | ----- | -------- |
| 1 — Couverture             | 13   | 5 s   | 0:05     |
| 2 — Rappel                 | 123  | 49 s  | 0:54     |
| 3 — Sommaire               | 77   | 31 s  | 1:25     |
| 4 — Amodei                 | 217  | 87 s  | 2:52     |
| 5 — o1-preview (cas)       | 114  | 46 s  | 3:37     |
| 6 — o1-preview (4 idées)   | 183  | 73 s  | 4:50     |
| 7 — Mythos (cas)           | 120  | 48 s  | 5:38     |
| 8 — Mythos (4 idées)       | 136  | 54 s  | 6:33     |
| 9 — Vaccination (cas)      | 96   | 38 s  | 7:11     |
| 10 — Vaccination (4 idées) | 125  | 50 s  | 8:01     |
| 11 — Ce qu'on a vu         | 123  | 49 s  | 8:50     |
| 12 — Conclusion            | 159  | 64 s  | **9:54** |

**Les deux repères à retenir par cœur** (les autres sont dans le script) :
**2:52** fin d'Amodei, **6:33** fin de Mythos. Ce sont les deux moitiés du
propos — si ces deux-là sont tenus, la fin passe toute seule.

**Ne jamais couper** : le 5,7 contre 56 (slide 6), les 354 protéines validées en
labo (slide 8), les 5-6 % (slide 10), et le « trop fort pour le titre, pas assez
faux pour le texte » (slide 5). Ce sont les quatre ancrages du propos.

## Anticipation des questions (20 min de discussion)

- **« Le modèle a-t-il vu les cas pendant son entraînement ? »** → question
  légitime, je n'ai pas la réponse dans les sources consultées. Le corpus
  d'o1 n'est pas auditable, c'est précisément une des limites que je cite.
- **« Pourquoi le mot "surhumain" a disparu du titre ? »** → je ne connais pas
  la raison officielle. Ce que je constate : il est resté dans le corps du
  texte. Hypothèse raisonnable, relecture par les pairs — mais c'est une
  hypothèse, pas un fait.
- **« Les 12 500 heures GPU, ça représente quoi en CO₂ ? »** → je n'ai pas le
  chiffre. C'est une vraie question par rapport à mon thème, et un angle à
  creuser pour une prochaine veille.
- **« Est-ce que tu vas utiliser Mythos / un agent pour QualiCheck ? »** → non,
  rien ne change côté production. Ce qui change c'est ma grille de décision,
  pas mon architecture actuelle.
- **« C'est reproductible ? »** → pour la vaccination et o1, les publications
  sont là. Pour Mythos, c'est un rapport d'entreprise sur ses propres modèles,
  avec validation par deux labos externes — c'est mieux qu'une simple annonce,
  mais ce n'est pas une publication à comité de lecture. À prendre pour ce que
  c'est.

## Sources sous la main

- Amodei, *Machines of Loving Grace* — darioamodei.com/essay/machines-of-loving-grace
- o1-preview, préprint — arxiv.org/abs/2412.10849
- o1-preview, *Science* — doi.org/10.1126/science.adz4433
- Mythos / protéines — anthropic.com/research/Claude-accelerates-protein-design
- Vaccination, ASU News + doi.org/10.1016/j.cpblue.2026.100088
