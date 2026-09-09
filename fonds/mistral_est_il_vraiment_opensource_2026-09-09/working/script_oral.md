# Script oral — Mistral est-il vraiment open source ?

Aide-mémoire pour la présentation, slide par slide. Durée totale : 9:30.

---

## Slide 1 — Titre

**Durée** : 0s **Fin de slide** : 0:00

*(Rien à dire. L'image s'affiche, deux secondes de silence, puis
j'enchaîne directement sur l'agenda.)*

\newpage

## Slide 2 — Agenda

**Durée** : 15s **Fin de slide** : 0:15

Aujourd'hui je vous emmène dans le monde de l'open, en quatre étapes.
D'abord le logiciel libre et les standards ouverts. On continuera
ensuite sur l'ouverture en IA. Puis un détour réglementaire et
écologique. Et pour finir, si on a le temps, on évoquera Ollama.

\newpage

## Slide 3 — Bloc 1 : Logiciel libre et standards ouverts

**Durée** : 20s **Fin de slide** : 0:35

Pour comprendre ce que "open source" veut dire pour l'IA, il faut d'abord
repartir du logiciel libre classique. Trois mots à garder en tête :
libertés, standards, interopérabilité.

\newpage

## Slide 4 — Les 4 libertés (FSF, Richard Stallman)

**Durée** : 45s **Fin de slide** : 1:20

Très rapidement : on doit ça à Richard Stallman et à la Free Software
Foundation, dans les années 80.

Le logiciel libre repose sur quatre libertés, numérotées de zéro à
trois. Utiliser le programme comme on veut — quelle que soit sa
nationalité, l'usage qu'on en fait, le but qu'on poursuit, on peut
l'utiliser. L'étudier et le modifier, pour l'adapter à ses besoins — ce
qui suppose d'avoir le code source, pas juste le binaire compilé. Le
redistribuer. Et redistribuer ses propres modifications, grâce
notamment à la licence GPL, qui impose de redistribuer le code source
et les modifications.

Pour les retenir, pensez à une recette de cuisine. La liberté zéro,
c'est manger le plat, ou en faire ce qu'on veut. La un, c'est lire la
recette et la modifier — ajouter du sel, changer les quantités. La
deux, c'est donner la recette à des amis. La trois, c'est donner votre
propre version modifiée.

Une précision importante : libre ne veut pas dire gratuit. C'est une
question de libertés d'action, pas de prix.

Linux en est un exemple bien connu, mais il y en a beaucoup d'autres :
Firefox, Git, Python, GCC, et bien d'autres encore.

\newpage

## Slide 5 — Standards ouverts, différent du logiciel libre

**Durée** : 30s **Fin de slide** : 1:50

Un standard ouvert, c'est différent du logiciel libre. On en parle pour
des formats de fichiers, des protocoles de communication, des API. Un
standard ouvert est publié et disponible pour tout le monde, sans
restriction de licence ni de brevet — et il est maintenu par une
communauté, pas par une seule entreprise.

On parle souvent d'interopérabilité : la capacité de systèmes différents
à travailler ensemble. Prenez l'USB. Peu importe que vous branchiez un
iPhone, un Samsung, un PC ou un Mac : tant que l'appareil respecte le
standard, la connexion fonctionne. On se fiche du matériel derrière la
prise — on ne demande jamais "comment ça marche à l'intérieur", juste
"est-ce que ça respecte le standard".

Quelques exemples : TCP/IP pour Internet, HTML pour le web, PDF pour les
documents. Ça donne la liberté d'interagir et de changer de fournisseur
sans être bloqué. Pas forcément la liberté de modifier le code.

\newpage

## Slide 6 — Maintenant, appliquons ça à l'IA…

**Durée** : 20s **Fin de slide** : 2:10

Avec ces concepts en tête, la question devient : comment ça s'applique à
l'intelligence artificielle ? Parce qu'un modèle d'IA, ce n'est pas juste
un programme.

\newpage

## Slide 7 — Un modèle d'IA n'est pas un programme classique

**Durée** : 40s **Fin de slide** : 2:50

Pour un logiciel classique, le code source explique tout : un seul
artefact concentre toute l'information.

Un modèle d'IA, c'est radicalement différent. Son comportement vient de
trois choses indépendantes : les poids, appris pendant l'entraînement ;
le code et le processus d'entraînement ; et les données sur lesquelles
il a appris. Chacune peut être ouverte ou fermée indépendamment des
deux autres — c'est ça qui crée tout un continuum, là où le logiciel
classique ne connaît que deux cas : code disponible, ou pas.

\newpage

## Slide 8 — Comment fabrique-t-on un modèle ? (analogie du gâteau)

**Durée** : 40s **Fin de slide** : 3:30

Pour visualiser ça, pensez à un gâteau.

- Les poids, c'est le gâteau fini — le résultat qu'on peut consommer.
- Le code et le processus d'entraînement, c'est la recette — la
  température, la durée, l'ordre des étapes.
- Les données, ce sont les ingrédients — la farine, les œufs, leur
  qualité.

Si vous n'avez que le gâteau fini, vous pouvez le manger. Mais vous ne
savez ni comment il a été fait, ni comment le reproduire à l'identique.

\newpage

## Slide 9 — Open weight vs Open source : la distinction critique

**Durée** : 35s **Fin de slide** : 4:05

Open weight, c'est je vous montre le gâteau fini, avec un bel emballage.
Mais ni la recette, ni les ingrédients. Impossible de vérifier une
allergie, un biais caché. Llama, Mistral, DeepSeek sont dans ce cas.

Open source, au sens strict, c'est je vous montre tout : le gâteau, la
recette, les ingrédients. Vous pouvez utiliser, étudier, modifier,
redistribuer.

Filtre d'amour : l'open weight repose sur une confiance aveugle envers
celui qui a fabriqué le modèle. L'open source permet une confiance
vérifiée.

\newpage

## Slide 10 — Le continuum en 4 catégories

**Durée** : 40s **Fin de slide** : 4:45

Quatre catégories, de la fermeture totale à l'ouverture complète.

Fermé, API : GPT, Claude, Gemini — aucune composante accessible, juste
un accès distant payant. Un choix stratégique valide, pas une tare.

Open weight : Llama, Mistral, DeepSeek — les poids sont publics, le reste
non.

Open weight plus plus : gpt-oss, Gemma, Qwen — une documentation plus
riche, mais toujours pas de reproduction indépendante possible.

Open source, au sens strict : OLMo, Apertus, Luciole — poids, code et
données publiés, les quatre libertés s'appliquent réellement.

Et Mistral se situe ici, en open weight.

\newpage

## Slide 11 — Pourquoi la distinction importe vraiment

**Durée** : 35s **Fin de slide** : 5:20

Un exemple concret. Imaginez un modèle entraîné sur des données
contaminées par la propagande d'un régime autoritaire.

Avec l'open weight seul, vous constatez qu'une réponse est bizarre, mais
impossible d'en trouver l'origine — même pas moyen d'auditer. Avec
l'open source, vous avez accès aux données : vous voyez d'où vient le
biais, et vous pouvez le corriger.

C'est comme une eau contaminée invisible dans la préparation. L'open
weight, vous goûtez un résultat étrange sans savoir pourquoi. L'open
source, vous repérez tout de suite la source contaminée.
L'indépendance de penser dépend de la transparence de la fabrication.

\newpage

## Slide 12 — Erreurs méthodologiques révélées (cas Lucie)

**Durée** : 20s **Fin de slide** : 5:40

Janvier 2025 : Lucie, le modèle français d'OpenLLM France, est lancée en
version inachevée, avec des réponses parfois incohérentes. Parce que le
projet était ouvert, la communauté a détecté les problèmes et forcé une
correction rapide. Si Lucie avait été fermée, personne n'aurait jamais
su.

L'ouverture permet la correction communautaire.

\newpage

## Slide 13 — Comment les gouvernements définissent-ils « open source » ?

**Durée** : 15s **Fin de slide** : 5:55

Une question réglementaire se pose alors : comment les gouvernements
définissent-ils "open source" ? L'Union européenne a répondu avec l'AI
Act. Et la réponse n'est pas celle qu'on attendrait.

\newpage

## Slide 14 — Attention : 3 définitions différentes du mot « open source »

**Durée** : 25s **Fin de slide** : 6:20

En fait, le mot "open source" recouvre trois définitions différentes :
le marketing, l'AI Act, et l'OSAID. Et contrairement à ce qu'on pourrait
croire, l'AI Act est plus léger que l'OSAID — il demande seulement un
résumé des données d'entraînement, pas de les publier entièrement.

*(Regardez le schéma : aucune des trois définitions ne recouvre
exactement les deux autres.)*

\newpage

## Slide 15 — L'Union européenne exempte les modèles « open source »

**Durée** : 40s **Fin de slide** : 7:00

L'AI Act ne se contente pas de classer les systèmes par niveau de
risque : il impose aussi des obligations propres aux gros modèles
généralistes. Il y en a quatre : documenter la technique en détail,
documenter à destination des fournisseurs en aval, respecter le droit
d'auteur, et publier un résumé du contenu d'entraînement.

L'exemption pour les modèles open source ne porte que sur les deux
premières — documentation technique et documentation aval. Le droit
d'auteur et le résumé du contenu d'entraînement restent obligatoires,
même open source.

Et cette exemption saute complètement si le modèle est monétisé, ou
s'il dépasse le seuil de risque systémique : dix puissance vingt-cinq
FLOPs. Llama-3 405B le dépasse largement.

\newpage

## Slide 16 — La fausse bonne idée : local = plus écolo ?

**Durée** : 25s **Fin de slide** : 7:25

On pense souvent : faire tourner un modèle chez soi, c'est plus écolo
qu'une API cloud. C'est plus compliqué que ça.

Imaginez une mini-piscine chez vous, utilisée une heure par semaine.
Contre une piscine communautaire, utilisée par cinq cents personnes,
vingt-quatre heures sur vingt-quatre. La communautaire est bien plus
efficace.

\newpage

## Slide 17 — Quand est-ce que local devient compétitif ?

**Durée** : 20s **Fin de slide** : 7:45

En dessous de 85% d'utilisation GPU, mieux vaut le cloud — batching,
datacenter optimisé. Au-dessus, le local devient compétitif.

Il faut vérifier les chiffres réels. Pas supposer.

\newpage

## Slide 18 — Pragmatisme

**Durée** : 10s **Fin de slide** : 7:55

*(Enchaîner directement, sans pause.)*

Le local n'est pas forcément mieux. Le cloud n'est pas forcément pire.
L'intérêt de l'open weight, c'est de pouvoir décider au cas par cas.

\newpage

## Slide 19 — Ollama : comment ça fonctionne ?

**Durée** : 20s **Fin de slide** : 8:15

Ollama, c'est exclusivement de l'open weight et de l'open source — aucun
modèle fermé. Trois façons de l'utiliser : en local gratuitement, via une
API limitée, ou en Cloud Pro à vingt dollars par mois.

La monétisation, c'est l'infrastructure cloud. Pas les modèles.

\newpage

## Slide 20 — Mistral est-il vraiment open source ?

**Durée** : 20s **Fin de slide** : 8:35

Alors, la réponse directe : non. Mistral est open weight, pas open
source. Pour l'être vraiment, il faudrait publier aussi les données et
la recette d'entraînement complète.

"Open source" n'est pas une case qu'on coche. C'est un continuum. Et
c'est un choix.

\newpage

## Slide 21 — Mais attends…

**Durée** : 40s **Fin de slide** : 9:15

*(Ne pas précipiter — c'est le twist final.)*

Vous vous dites peut-être : je vais utiliser Ollama Cloud, c'est open
source, donc je suis indépendant.

*(pause)*

Sauf que l'infrastructure d'Ollama Cloud est hébergée aux États-Unis —
un transfert de données hors Union européenne.

Il existe une alternative : Infomaniak, en Suisse, conforme RGPD. Mais
son catalogue est plus restreint — huit modèles, dont Apertus, celui-là
même dont je vous ai parlé tout à l'heure.

Le vrai dilemme : large choix, ou souveraineté. Rarement les deux à la
fois.

*(ton léger, un peu ironique)* Eh merde.

L'indépendance technique, ce n'est pas la même chose que l'indépendance
réelle.

\newpage

## Slide 22 — Questions ?

**Durée** : 15s **Fin de slide** : 9:30

Voilà. Je vous laisse la parole.

\newpage

## Rappels de rythme

- **Transitions (3, 6, 13)** : dites vite, sans se précipiter au point de
  perdre l'auditoire.
- **Bloc 3 (14 à 18)** : le plus technique et le plus dense. Parler
  lentement, articuler.
- **Slide 21** : le twist final. Ne pas la bâcler — c'est elle qui laisse
  la dernière impression.
