# correction du script oral

## les slides 

1 page par slide

## Slide 2

Aujourd’hui je vous emmène dnas le monde de l'openen quatre étapes. 
D’abord le logiciel libre et les standards ouverts. 
On continuera ensuite  sur l'ouverture en IA. 
Puis un détour réglementaire et écologique. 
Et pour finir, si on a le tems on évoquera Ollama

## Slide 4

Très Rapidement, on évoque richard Stallman et la Free Software Foundation dans les années 80.

Le logiciel libre repose sur quatre libertés, numérotées de zéro à trois.

- Utiliser le programme comme on veut. ex : quelque soit sa nationnalité, l'usage qu'on en fait, le but qu'on poursuit, on peut l'utiliser.
- L’étudier et le modifier — pour l'adapter à ses besoins, ce qui suppose d’avoir le code source, pas juste le binaire compilé.
- Le redistribuer. 
- Et redistribuer ses propres modifications. (grace par à la licence GPL, qui impose de redistribuer le code source et les modifications)

Pour les retenir, pensez à une recette de cuisine. La liberté zéro, c’est manger le plat ou en faire ce qu'on veut. La un, c’est lire la recette et la modifier — ajouter du sel, changer les quantités. La deux, c’est donner la recette à des amis.  La
trois, c’est donner votre propre version modifiée.

Une précision importante : libre ne veut pas dire gratuit. C’est une
question de libertés d’action, pas de prix

Linux est un exemple de logiciel libre, mais il y en a beaucoup d'autres. Firefox, Git, Python, GCC et bien d'autres encore.

## Slide 5

on parle de standards ouverts quand on parle de formats de fichiers, de protocoles de communication, d'API, etc.
Un standard ouvert est un standard qui est publié et disponible pour tout le monde, sans restriction de licence ou de brevet. Il est maintenu par une communauté et non par une seule entreprise.

Parle souvent d'interopérabilité, c'est-à-dire la capacité de différents systèmes à travailler ensemble.

 Prenez l’USB. Peu importe que
vous branchiez un iPhone, un Samsung, un PC ou un Mac : tant que
l’appareil respecte le standard, la connexion fonctionne. On se fiche
du matériel derrière la prise — on ne demande jamais “comment ça
marche à l’intérieur”, juste “est-ce que ça respecte le standard”.

Cela donne par exemple TCP/IP pour Internet, HTML pour le web, PDF pour les documents.

## Slide 8

> Juste de la mise en page 

Pour visualiser ça, pensez à un gâteau. 

- Les poids, c’est le gâteau fini — le résultat qu’on peut consommer. 
- Le code et le processus d’entraînement, c’est la recette — la température, la durée, l’ordre des étapes.
- Les données, ce sont les ingrédients — la farine, les œufs, leur qualité.

Si vous n’avez que le gâteau fini, vous pouvez le manger. Mais vous ne savez ni comment il a été fait, ni comment le reproduire à l’identique

## Slide 15

AI Act en plus de documenter les niveaux de risque, impose des obligations :

- la documentation technique détaillée
- la documentation pour les fournisseurs en aval 
- une politique de respect du droit d'auteur
- un résumé du contenu d'entraînement 

Elle exempte des 2 premières obligations les modèles open source, mais seulement si le modèle est open source (selon sa définition) et qu'il n'est pas monétisé.

Et cette exemption saute complètement si le modèle est monétisé, ou s'il dépasse le seuil de risque systémique de 10^25 FLOPs — Llama-3 405B le dépasse largement.


## Slide 16
> on enleve Jevons