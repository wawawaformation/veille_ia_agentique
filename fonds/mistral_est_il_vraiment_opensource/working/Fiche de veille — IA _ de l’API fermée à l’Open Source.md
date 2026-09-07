# IA : de l’API fermée à l’Open Source  
## Comprendre ce que signifie réellement « ouvrir » un modèle d’intelligence artificielle

### 1. Point de départ : « ouvert », mais ouvert comment ?

Dans le domaine de l’intelligence artificielle générative, les expressions *open source*, *open model*, *open weights* ou encore *modèle ouvert* sont souvent utilisées comme si elles désignaient la même chose.

Ce n’est pas le cas.

La vidéo de départ d’Anaïs permet d’introduire simplement le problème :

https://www.youtube.com/watch?v=pYGDq1st4mI

Elle distingue trois composantes fondamentales nécessaires pour comprendre la fabrication d’un modèle d’IA :

- **les poids du modèle** ;
- **le code et le processus d’entraînement** ;
- **les données d’entraînement**.

Cette distinction est essentielle, car publier uniquement les poids d’un modèle ne revient pas à publier tout ce qui a permis de le produire.

L’enjeu dépasse la simple possibilité de télécharger un modèle. Il concerne aussi :

- l’audit ;
- la recherche scientifique ;
- la reproductibilité ;
- la modification ;
- la contribution ;
- la compréhension des biais ;
- l’indépendance vis-à-vis d’un fournisseur.

L’objectif n’est pas d’établir une hiérarchie morale entre modèles fermés et ouverts. Chaque degré d’ouverture répond à des contraintes et à des choix techniques, économiques ou stratégiques différents.

---

# 2. Aux origines : Richard Stallman et le logiciel libre

Pour comprendre cette question, il est utile de revenir au mouvement du **logiciel libre**, notamment aux travaux de Richard Stallman et de la Free Software Foundation.

Le mot *free* dans *free software* renvoie à la **liberté**, et non à la gratuité.

Un logiciel libre peut parfaitement être vendu, utilisé commercialement ou intégré à une activité économique.

La question centrale est :

> **Quelles libertés possède l’utilisateur du logiciel ?**

La Free Software Foundation formalise cette idée avec quatre libertés fondamentales.

### Liberté 0 — Utiliser

Pouvoir exécuter le programme comme on le souhaite, pour n’importe quel usage.

### Liberté 1 — Étudier et modifier

Pouvoir comprendre comment fonctionne le programme et le modifier.

Cette liberté suppose l’accès au code source.

### Liberté 2 — Redistribuer

Pouvoir partager des copies du programme.

### Liberté 3 — Redistribuer ses modifications

Pouvoir modifier le programme puis partager cette nouvelle version avec d’autres.

Ces libertés introduisent une idée fondamentale :

> **L’utilisateur ne doit pas seulement pouvoir utiliser un outil. Il doit également pouvoir l’étudier, le transformer et contribuer à son évolution.**

---

# 3. Ce que le logiciel libre a apporté

L’importance du logiciel libre ne se limite pas à une question de licence.

Il a profondément influencé la manière dont l’informatique moderne est construite.

Une grande partie de l’infrastructure utilisée aujourd’hui repose sur des logiciels libres ou open source :

- GNU/Linux ;
- GCC ;
- Git ;
- Python ;
- de nombreuses bases de données ;
- les serveurs Web ;
- les bibliothèques scientifiques ;
- puis une grande partie de l’écosystème moderne de l’IA.

Dans l’IA elle-même, le développement repose largement sur des composants accessibles et modifiables : frameworks de machine learning, bibliothèques Python, outils d’inférence, notebooks, formats de modèles, outils de quantification, etc.

Mais la contribution majeure du libre est également **culturelle**.

Un logiciel peut être :

**utilisé → étudié → corrigé → adapté → forké → amélioré → redistribué.**

L’innovation ne dépend donc plus exclusivement du producteur initial.

Une communauté peut :

- corriger des bugs ;
- optimiser le logiciel ;
- le porter sur une nouvelle architecture ;
- créer des extensions ;
- l’adapter à de nouveaux usages ;
- documenter son fonctionnement ;
- produire des dérivés.

On peut résumer cette contribution par :

> **Le libre ne donne pas seulement accès à une technologie : il donne la possibilité de participer à son évolution.**

Cette idée devient particulièrement intéressante lorsqu’on l’applique à l’IA.

Si l’on peut télécharger les poids d’un modèle mais qu’on ne sait pratiquement rien de la façon dont il a été entraîné, jusqu’où peut-on réellement l’étudier, le reproduire ou contribuer à sa fabrication ?

---

# 4. Une autre contribution essentielle : les standards ouverts

Le logiciel libre n’est pas le seul élément ayant permis le développement d’écosystèmes numériques ouverts.

Les **standards ouverts** ont également joué un rôle fondamental.

Il faut distinguer les deux notions.

### Logiciel libre / open source

Ce qui est ouvert est principalement **l’implémentation**.

On peut étudier et modifier le programme.

### Standard ouvert

Ce qui est ouvert est **la spécification permettant à différents systèmes d’interagir**.

Le Web en constitue un excellent exemple.

TCP/IP, HTTP, HTML ou CSS ont permis à des implémentations très différentes de fonctionner ensemble.

Un serveur peut utiliser une technologie et le navigateur une autre. Ils peuvent néanmoins communiquer parce qu’ils utilisent des règles communes.

Les standards ouverts favorisent donc :

- l’interopérabilité ;
- la portabilité ;
- la concurrence ;
- la possibilité de changer de fournisseur ;
- la construction d’écosystèmes.

Un standard ouvert ne signifie cependant pas que toutes ses implémentations sont open source.

Et inversement, un logiciel open source peut utiliser un format ou un protocole propriétaire.

Dans l’écosystème IA, on retrouve aujourd’hui cette logique autour de formats, interfaces et protocoles permettant aux modèles, outils et applications de fonctionner ensemble.

Il est donc utile de distinguer :

| Notion | Ce qui est principalement ouvert |
|---|---|
| Logiciel libre / open source | L’implémentation |
| Standard ouvert | La spécification et les règles d’échange |
| Open weight | Les paramètres appris par le modèle |

Le logiciel libre donne principalement **la liberté de modifier**.

Les standards ouverts donnent principalement **la liberté d’interagir et de choisir**.

---

# 5. Pourquoi l’IA complique la notion d’open source

Pour un logiciel traditionnel, le code source constitue l’élément central permettant de comprendre comment le programme fonctionne.

Un modèle de machine learning est différent.

Son comportement ne provient pas uniquement du programme utilisé pour l’exécuter.

Il résulte notamment de trois éléments.

## Les poids

Les poids sont les paramètres numériques appris pendant l’entraînement.

Ils représentent en quelque sorte **le résultat de l’apprentissage**.

Ils permettent d’exécuter le modèle sans recommencer son entraînement depuis zéro.

## Le code et le processus d’entraînement

Ils décrivent comment le modèle a été produit :

- architecture ;
- prétraitement des données ;
- algorithmes ;
- hyperparamètres ;
- entraînement ;
- validation ;
- filtrage ;
- éventuellement différentes étapes de post-entraînement.

Ils permettent donc de répondre à :

> **Comment ce modèle a-t-il été fabriqué ?**

## Les données d’entraînement

Elles constituent la matière utilisée pendant l’apprentissage.

Elles permettent de répondre à une autre question :

> **À partir de quel monde informationnel ce modèle a-t-il été construit ?**

C’est pour cette raison que transposer simplement la notion traditionnelle de « code source » à l’IA ne suffit pas.

---

# 6. L’analogie culinaire

Une analogie permet de rendre immédiatement cette distinction compréhensible.

### Les poids = le plat terminé

Le produit existe et peut être consommé.

Il est possible de l’observer, de le tester et éventuellement de le transformer.

### Le code et le processus d’entraînement = la recette et le procédé de fabrication

Ils expliquent comment on est arrivé au résultat :

- étapes ;
- température ;
- temps de cuisson ;
- proportions ;
- méthodes utilisées.

### Les données d’entraînement = les ingrédients

Elles constituent la matière qui a servi à fabriquer le produit.

On obtient donc :

> **Poids = produit / plat terminé**  
> **Entraînement = recette et procédé**  
> **Données = ingrédients**

Recevoir uniquement le plat terminé n’est pas équivalent à disposer de la recette et d’informations précises sur les ingrédients ayant permis de le produire.

---

# 7. Pourquoi les données sont particulièrement importantes

La question des données dépasse largement la reproductibilité technique.

Elles permettent notamment de comprendre **ce qui a façonné les représentations apprises par le modèle**.

Il faut cependant éviter de dire littéralement que les données révèlent « ce que pense le modèle ».

Un modèle ne possède pas nécessairement des pensées ou des opinions au sens humain.

Une formulation plus rigoureuse est :

> **Les données ne nous disent pas ce que “pense” un modèle. Elles nous renseignent sur le monde qu’on lui a donné à voir.**

Connaître la provenance et la composition des données permet notamment d’interroger plusieurs dimensions.

### Les biais

Certaines cultures, langues, professions, populations ou visions du monde peuvent être surreprésentées ou sous-représentées.

### Les connaissances

De quelles sources provient l’information ?

Sur quelles périodes ?

Dans quelles langues ?

Dans quels domaines ?

### Les angles morts

Quels sujets ou populations étaient peu présents ou absents du corpus ?

### La qualité

Les données provenaient-elles :

- de publications scientifiques ?
- de médias ?
- de forums ?
- de réseaux sociaux ?
- de contenus synthétiques ?
- de données fortement dupliquées ?

### Les choix éditoriaux

Quelles données ont été volontairement sélectionnées, exclues ou filtrées ?

### Les droits

Les données peuvent également poser des questions relatives :

- au droit d’auteur ;
- aux licences ;
- aux données personnelles ;
- au consentement.

### La reproductibilité scientifique

Deux modèles utilisant une architecture et un code d’entraînement similaires mais des corpus radicalement différents peuvent apprendre des représentations et produire des comportements différents.

La transparence sur les données est donc une composante importante de l’audit d’un système d’IA.

---

# 8. Transparence sur les données ne signifie pas nécessairement publier toutes les données

Il faut apporter ici une nuance importante.

Une définition sérieuse de l’Open Source AI ne peut pas simplement exiger :

> « publier l’intégralité du dataset ».

Certaines données ne peuvent légalement ou pratiquement pas être redistribuées.

La version 1.0 de l’**Open Source AI Definition de l’OSI** demande donc des **Data Information** suffisamment détaillées pour qu’une personne compétente puisse construire un système substantiellement équivalent.

Cela inclut notamment des informations sur :

- la provenance ;
- la portée et les caractéristiques des données ;
- la méthode de sélection ;
- le traitement ;
- le filtrage ;
- l’annotation ;
- ainsi que l’identification des données publiques ou obtenues auprès de tiers.

L’objectif est donc moins :

**« avoir exactement chaque fichier original »**

que :

**« disposer de suffisamment d’informations pour comprendre et reproduire substantiellement le processus »**.

---

# 9. L’Open Source AI Definition de l’OSI

L’Open Source Initiative a cherché à transposer les principes de l’open source à l’intelligence artificielle.

L’Open Source AI Definition 1.0 repose sur quatre libertés particulièrement simples à retenir :

> **Use — Study — Modify — Share**

Autrement dit :

- utiliser ;
- étudier ;
- modifier ;
- partager.

Pour qu’un système de machine learning permette réellement ces libertés, l’OSI considère que sa forme privilégiée pour effectuer des modifications doit notamment fournir :

### Les paramètres

Les poids et autres paramètres nécessaires.

### Le code

Le code nécessaire pour entraîner et exécuter le système, y compris les éléments significatifs du pipeline.

### Les informations sur les données

Des informations suffisamment détaillées sur les données et leur traitement pour permettre la compréhension et la construction d’un système substantiellement équivalent.

Cette définition permet surtout de comprendre une chose :

> **Publier des poids n’est pas automatiquement équivalent à publier une IA open source.**

---

# 10. Un continuum d’ouverture

Plutôt que d’opposer simplement :

**fermé ↔ open source**

il est pédagogiquement plus intéressant de représenter un continuum.

## 1 — Fermé / accessible uniquement comme service ou API

L’utilisateur peut utiliser le modèle mais n’a généralement pas accès :

- aux poids ;
- au code d’entraînement ;
- aux données ;
- au processus complet ayant permis sa construction.

Il consomme essentiellement **un service**.

### Pourquoi un producteur peut-il faire ce choix ?

Ce choix peut être parfaitement rationnel.

#### Rentabiliser les coûts de R&D

Construire un modèle performant peut nécessiter des investissements importants :

- recherche ;
- collecte et préparation des données ;
- entraînement ;
- infrastructure ;
- ingénierie ;
- évaluation ;
- sécurité ;
- exploitation.

Une API permet de transformer cet investissement en revenus récurrents.

#### Protéger le savoir-faire

Le dataset, la recette d’entraînement, les optimisations ou les poids eux-mêmes peuvent constituer des actifs stratégiques.

#### Garder le contrôle

Le fournisseur peut maîtriser :

- les versions utilisées ;
- les mises à jour ;
- les mesures de sécurité ;
- les usages autorisés ;
- la disponibilité du service.

#### Simplifier l’expérience utilisateur

L’utilisateur n’a pas besoin :

- d’acheter des GPU ;
- d’installer le modèle ;
- de maintenir l’infrastructure ;
- de gérer les mises à jour.

#### Mutualiser l’infrastructure

Le fournisseur peut optimiser l’inférence pour un très grand nombre d’utilisateurs.

### Résumé

> **API fermée : privilégier le service, la simplicité, le contrôle et la rentabilisation de l’investissement.**

### Nuance importante

**API n’est pas synonyme de fermé.**

Un modèle open source peut parfaitement être exposé derrière une API.

Dans ce continuum, « Fermé / API » est utilisé comme raccourci pédagogique pour désigner **un modèle dont l’utilisateur ne peut accéder qu’au service fourni par son propriétaire**.

---

# 11. Open weight

Dans un modèle **open weight**, les poids entraînés sont disponibles.

Cela change considérablement les possibilités.

L’utilisateur peut notamment, selon la licence et les outils disponibles :

- télécharger le modèle ;
- l’exécuter localement ;
- choisir son infrastructure ;
- l’optimiser ;
- le quantifier ;
- l’adapter ;
- réaliser certaines analyses ;
- construire des dérivés.

Mais la publication des poids ne signifie pas nécessairement que sont également publiés :

- le dataset ;
- le pipeline complet d’entraînement ;
- les méthodes de filtrage ;
- tous les hyperparamètres ;
- les checkpoints ;
- le code complet ayant servi à produire le modèle.

### Pourquoi publier les poids sans tout publier ?

Là encore, plusieurs raisons peuvent expliquer ce choix.

#### Favoriser l’adoption

Un modèle téléchargeable peut être utilisé sans dépendre d’une API propriétaire.

#### Développer un écosystème

La communauté peut produire :

- quantifications ;
- fine-tunes ;
- outils ;
- intégrations ;
- optimisations ;
- applications.

#### Stimuler la recherche

Les chercheurs disposent directement des paramètres du modèle et peuvent réaliser davantage d’expérimentations.

#### Permettre l’exécution locale

Cela peut être important pour :

- la confidentialité ;
- la maîtrise de l’infrastructure ;
- le fonctionnement hors connexion ;
- la souveraineté technologique.

#### Augmenter l’influence du modèle

Un modèle très largement réutilisé peut devenir une plateforme ou un socle technologique important.

#### Conserver des actifs stratégiques

Il est possible d’ouvrir les poids tout en conservant :

- certaines données ;
- la recette complète d’entraînement ;
- certains outils ;
- certains procédés internes.

L’open weight constitue donc souvent un compromis entre diffusion et contrôle.

### Résumé

> **Open weight : favoriser l’adoption et la création d’un écosystème tout en conservant éventuellement certaines briques de fabrication comme actifs stratégiques.**

---

# 12. « Open weight ++ »

**Open weight ++ n’est pas une catégorie officielle.**

Il s’agit ici d’une catégorie pédagogique permettant de représenter les nombreux modèles situés entre :

**« les poids sont disponibles »**

et

**« l’ensemble répond réellement à une définition de l’Open Source AI »**.

Un modèle de cette catégorie pourrait fournir :

- les poids ;
- le code d’inférence ;
- une architecture documentée ;
- une partie du code d’entraînement ;
- les hyperparamètres principaux ;
- un rapport technique détaillé ;
- certains checkpoints ;
- des informations importantes sur les données ;
- les méthodes de filtrage ou de sélection.

Il offre donc davantage de possibilités :

- d’audit ;
- de compréhension ;
- d’adaptation ;
- de recherche ;
- de reproductibilité.

Mais certaines briques nécessaires à une reproduction complète ou substantiellement équivalente peuvent encore manquer.

### Résumé

> **Open weight ++ : le plat est fourni avec une partie significative de la recette et des informations sur les ingrédients, sans que tout le processus soit nécessairement ouvert.**

---

# 13. Open Source AI

À l’extrémité du continuum se trouve l’ambition d’une IA réellement open source.

Elle doit permettre les libertés de :

**utiliser → étudier → modifier → partager.**

L’ouverture ne concerne donc plus uniquement le produit final.

Elle doit également fournir suffisamment d’éléments sur sa fabrication pour permettre une véritable appropriation technique.

Les avantages recherchés sont notamment :

- l’audit indépendant ;
- la reproductibilité ;
- la recherche ;
- la contribution communautaire ;
- la création de dérivés ;
- l’amélioration collective ;
- une dépendance réduite à un fournisseur unique.

### Résumé

> **Open Source AI : donner suffisamment d’accès au produit, à sa fabrication et à son origine pour permettre une véritable étude, modification et contribution.**

---

# 14. La fresque proposée

Le continuum peut être résumé ainsi :

**Fermé / API → Open weight → Open weight ++ → Open Source**

Avec un premier axe :

### Ce qui devient progressivement accessible

**Service → poids → éléments de fabrication → capacité réelle d’étude et de modification**

Et un second axe :

### Logique du producteur

**Service et contrôle → diffusion → collaboration partielle → contribution ouverte**

Il ne faut surtout pas transformer cette fresque en échelle de valeur.

> **Une catégorie décrit un niveau d’ouverture, pas la qualité intrinsèque d’un modèle.**

Chaque position constitue un arbitrage entre :

- investissement ;
- contrôle ;
- sécurité ;
- modèle économique ;
- diffusion ;
- auditabilité ;
- reproductibilité ;
- souveraineté ;
- contribution.

---

# 15. Fine-tuning : une conséquence très concrète de l’accès aux poids

Le fine-tuning permet d’adapter un modèle préentraîné à un comportement, un domaine ou une tâche particulière.

Il faut cependant éviter l’affirmation :

> « Le fine-tuning n’est possible qu’avec un modèle open weight. »

Ce serait faux.

## Fine-tuning via API

Certains fournisseurs proposent du **fine-tuning managé**.

L’utilisateur fournit son dataset et configure l’entraînement, mais le fournisseur réalise l’opération sur son infrastructure.

L’utilisateur obtient ensuite l’accès à une version adaptée du modèle.

Il peut donc personnaliser le modèle **sans avoir accès directement aux poids**.

Le niveau de liberté reste néanmoins déterminé par ce que le fournisseur autorise.

> **Le fournisseur adapte le modèle pour moi, dans son environnement et selon les possibilités qu’il met à ma disposition.**

Les tarifs varient fortement selon les modèles et les techniques utilisées. Dans certains cas, le coût informatique de l’entraînement peut rester raisonnable.

Le coût important d’un projet de fine-tuning se trouve souvent ailleurs :

**collecter → nettoyer → sélectionner → annoter → structurer → évaluer les données.**

Un mauvais dataset produit rarement un bon fine-tuning, quel que soit le budget de calcul.

## Fine-tuning avec des poids accessibles

Avec un modèle open weight, l’utilisateur peut réaliser lui-même son adaptation.

Il peut choisir :

- son infrastructure ;
- son outil ;
- son dataset ;
- ses hyperparamètres ;
- sa stratégie d’entraînement ;
- ses méthodes d’évaluation.

Il peut utiliser différentes techniques telles que :

- full fine-tuning ;
- LoRA ;
- QLoRA ;
- autres méthodes d’adaptation paramétrique.

Le point essentiel pour cette présentation n’est donc pas :

> **« L’open weight rend le fine-tuning possible. »**

mais :

> **« L’open weight rend possible un fine-tuning autonome. »**

---

# 16. Prompting, RAG et fine-tuning : ne pas confondre

Ces trois techniques modifient le comportement d’un système de façons différentes.

### Prompting

On donne des instructions au modèle.

Les poids ne sont pas modifiés.

### RAG

On fournit au modèle, au moment de la requête, des informations provenant d’une source externe.

Les poids ne sont toujours pas modifiés.

### Fine-tuning

Une phase d’apprentissage supplémentaire modifie le comportement du modèle.

Selon la technique utilisée, tout ou partie des paramètres sont adaptés.

Cette distinction permet de montrer une conséquence concrète du continuum d’ouverture :

**API fermée**  
→ je peux utiliser et éventuellement personnaliser ce que le fournisseur m’autorise.

**Open weight**  
→ je peux exécuter et adapter moi-même le modèle.

**Ouverture plus complète**  
→ je peux également comprendre beaucoup plus profondément comment il a été produit et éventuellement reproduire ou modifier son processus de fabrication.

---

# 17. Reprise de l’analogie culinaire avec le fine-tuning

L’analogie peut continuer à fonctionner.

### API fermée

Je vais au restaurant et commande le plat.

Je peux éventuellement demander :

> « Moins épicé, sans sel, avec davantage de légumes. »

Le cuisinier adapte le plat pour moi.

C’est l’équivalent du fine-tuning proposé comme service.

### Open weight

Je dispose du plat et peux commencer à le transformer dans ma propre cuisine.

J’ai beaucoup plus de liberté sur la manière de procéder.

### Open weight ++

Je dispose également d’éléments importants de la recette et d’informations sur les ingrédients.

Je comprends mieux ce que je transforme.

### Open Source AI

Je dispose suffisamment du plat, de la recette, du procédé et des informations sur les ingrédients pour pouvoir étudier réellement sa fabrication, la modifier et transmettre ma propre version.

---

# 18. Le message essentiel

L’expression **« modèle ouvert »** est insuffisante.

La bonne question n’est pas :

> **« Ce modèle est-il ouvert ? »**

mais plutôt :

> **« Qu’est-ce qui est ouvert ? »**

Puis :

- Les poids ?
- Le code d’inférence ?
- Le code d’entraînement ?
- Le processus ?
- Les données ou les informations sur les données ?
- La licence autorise-t-elle réellement l’utilisation, la modification et la redistribution ?
- Peut-on exécuter le modèle indépendamment du fournisseur ?
- Peut-on l’adapter ?
- Peut-on comprendre suffisamment sa fabrication pour la reproduire ?

C’est cette grille qui permet de distinguer réellement :

**fermé / service → open weight → ouverture intermédiaire → Open Source AI.**

---

# 19. Fil narratif possible pour une présentation

La matière peut être présentée sous la forme d’une histoire plutôt que comme une succession de définitions.

**1. La vidéo d’Anaïs**  
Poids, entraînement et données : pourquoi « ouvert » est plus compliqué en IA.

**2. Richard Stallman**  
Retour aux origines de la liberté logicielle.

**3. Les quatre libertés**  
Utiliser, étudier, modifier, partager.

**4. La contribution du logiciel libre**  
Le droit de modifier permet également de contribuer.

**5. Les standards ouverts**  
L’interopérabilité donne la possibilité de choisir et de construire des écosystèmes.

**6. Le problème particulier de l’IA**  
Le code seul ne suffit plus : il faut considérer poids, entraînement et données.

**7. L’importance des données**  
Elles renseignent sur le monde qui a été présenté au modèle et constituent un élément majeur de transparence et d’audit.

**8. L’OSI et l’Open Source AI Definition**  
Comment transposer les libertés traditionnelles à l’IA.

**9. La fresque**  
Fermé/API → Open weight → Open weight ++ → Open Source.

**10. Pourquoi choisir l’un ou l’autre ?**  
API : service, simplicité, contrôle, protection et rentabilisation de la R&D.  
Open weight : adoption, écosystème, usage local et compromis entre ouverture et actifs stratégiques.

**11. Le fine-tuning**  
Une conséquence concrète : avec les poids, l’utilisateur gagne la possibilité d’adapter lui-même le modèle.

**12. Conclusion**

> **« Open » n’est pas binaire.  
> Ce qui importe est de savoir ce qui est réellement ouvert, sous quelles conditions, et quelles libertés cette ouverture donne à l’utilisateur.**

---

# Références principales

- Vidéo d’Anaïs utilisée comme point de départ :  
  https://www.youtube.com/watch?v=pYGDq1st4mI

- GNU / Free Software Foundation — définition du logiciel libre et quatre libertés.

- Open Source Initiative — Open Source AI Definition 1.0 :  
  https://opensource.org/ai/open-source-ai-definition

La définition 1.0 de l’OSI retient explicitement les quatre libertés **Use, Study, Modify, Share** et demande, pour les systèmes de machine learning, l’accès aux paramètres, au code nécessaire à l’entraînement et à l’exécution, ainsi qu’à des informations suffisamment détaillées sur les données utilisées.