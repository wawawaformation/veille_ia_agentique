---
title: "Besoin 2 — Vision dans QualiCheck US2"
status: "piste d'intégration"
---

# QualiCheck US2 : capture d'écran et vision

QualiCheck est une plateforme d'aide à l'audit qualité web fondée sur les règles
Opquast.

Dans la conception actuelle, US2 permet à un professionnel du web de soumettre une
URL **ou une capture d'écran**, puis de poser une question libre. Le RAG sémantique
cherche les règles Opquast pertinentes.

La vision doit donc pouvoir transformer une image en contexte exploitable.

## Ce qu'une capture peut apporter

Un VLM peut potentiellement extraire :

- le texte visible ;
- les titres et la hiérarchie visuelle ;
- la navigation ;
- le contenu principal ;
- les zones secondaires ;
- des composants ou regroupements visuels ;
- l'ordre de lecture apparent ;
- certains signaux perceptibles sur l'image.

## Limite fondamentale

Une capture ne donne accès qu'à ce qui est observable visuellement.

Exemples :

```text
contraste apparent        → observable
présence d'un libellé     → partiellement observable
ordre visuel              → observable

type="email"               → non vérifiable sur l'image
attribut alt               → non vérifiable sur l'image
focus clavier              → non vérifiable sur l'image statique
interaction au clic       → non vérifiable sur l'image statique
```

La future conception de la vision dans US2 devra donc rester complémentaire du DOM,
du HTML et des tests interactifs.

## Données personnelles et information utilisateur

Une capture d'écran peut contenir des données personnelles ou confidentielles :
nom, photo, adresse e-mail, interface connectée, messages, identifiants visibles,
etc.

Si le provider retenu effectue l'inférence dans une juridiction ou une infrastructure
qui ne convient pas au traitement de ces données, l'utilisateur doit être **informé
au moment où il utilise l'outil vision**, avant l'envoi de l'image.

Piste d'interface :

> L'image va être transmise à un service externe d'intelligence artificielle.
> N'envoyez pas de capture contenant des données personnelles, confidentielles ou
> sensibles sans les avoir masquées au préalable.

Cette formulation devra être adaptée aux caractéristiques réelles du provider
finalement retenu et validée dans la conception détaillée.
