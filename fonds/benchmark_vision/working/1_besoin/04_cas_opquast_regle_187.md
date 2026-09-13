---
title: "Cas d'usage Vision — Opquast règle 187"
status: "cas concret pour QualiCheck US2"
source: "https://checklists.opquast.com/fr/qualite-numerique/les-textes-pouvant-etre-mis-en-forme-via-des-styles-ne-sont-pas-remplaces-par-des-images"
---

# Cas d'usage Vision — règle Opquast 187

## Règle

**Les textes pouvant être mis en forme via des styles ne sont pas remplacés par des
images.**

Cette règle constitue un cas particulièrement intéressant pour la future brique
Vision de QualiCheck.

---

## Pourquoi cette règle est intéressante

Le contrôle ne consiste pas uniquement à lire du texte.

Il faut repérer des images contenant du texte et déterminer si ce contenu aurait pu
être présenté sous forme de texte HTML mis en forme par CSS.

On se trouve donc à l'intersection de plusieurs types d'analyse :

```text
DOM / HTML
+
détection d'images
+
OCR
+
compréhension visuelle
+
jugement assisté
```

C'est précisément le type de contrôle pour lequel un VLM peut apporter quelque chose
qu'un moteur OCR classique ne fournit pas.

---

## Ce que la Vision peut apporter

Une fois une image identifiée dans la page, un VLM peut aider à déterminer :

- si l'image contient du texte ;
- si le texte est l'élément principal de l'image ;
- s'il s'agit plutôt d'un logo ;
- s'il s'agit d'une publicité ;
- s'il s'agit d'un élément graphique de promotion ;
- si la composition paraît suffisamment simple pour être probablement reproduite avec
  du texte HTML et des styles CSS.

Exemple de chaîne :

```text
image extraite de la page
        ↓
VLM
        ↓
texte présent ?
        ↓
texte dominant ?
        ↓
logo / publicité / promotion ?
        ↓
mise en forme potentiellement reproductible en HTML/CSS ?
        ↓
signal proposé à l'auditeur
```

---

## Pourquoi une simple capture d'écran complète ne suffit pas

À partir d'une capture globale, un VLM voit uniquement le rendu final.

Il ne peut pas déterminer de manière fiable si un texte visible provient :

```text
d'un élément HTML + CSS
```

ou :

```text
d'une image contenant du texte
```

Les deux peuvent produire exactement le même rendu visuel.

La règle ne doit donc pas être confiée à la Vision seule à partir d'une capture
d'écran complète.

---

## Pipeline QualiCheck plus pertinent

QualiCheck dispose justement d'autres moyens d'extraction.

Une stratégie hybride paraît plus adaptée :

```text
page web
   ↓
HTML / DOM / CSS
   ↓
repérage des <img>
+ images d'arrière-plan pertinentes
   ↓
extraction des images concernées
   ↓
VLM
   ↓
analyse visuelle
   ├── contient du texte ?
   ├── texte dominant ?
   ├── logo ?
   ├── publicité ?
   ├── promotion ?
   └── complexité graphique ?
   ↓
constat proposé
   ↓
validation humaine
```

Le DOM répond à la question :

> Est-ce réellement une image ?

Le VLM aide à répondre à :

> Que contient cette image et quelle semble être sa fonction ?

---

## Limite : « pouvait être mis en forme via CSS »

Cette partie reste délicate.

Déterminer qu'un rendu **aurait pu** être réalisé avec du texte HTML et CSS comporte
une part de jugement.

Le VLM peut fournir une indication, mais il ne devrait pas transformer cette
appréciation en verdict automatique.

Exemple de résultat exploitable :

```yaml
rule: 187

image_contains_text: true
text_is_primary_content: true

probable_exclusion:
  logo: false
  advertising: false
  promotional_graphic: false

css_reproduction:
  assessment: "probable"
  confidence: 0.78

decision: "manual_review"
```

Le résultat final reste soumis à l'auditeur.

---

## Intérêt pour la veille OCR / VLM

Ce cas montre que les travaux menés pour la numérisation de livres peuvent être
réutilisés dans QualiCheck, mais avec un rôle plus riche.

Pour un livre :

```text
image
  ↓
transcription
```

Pour ce type de règle Opquast :

```text
image
  ↓
transcription
+
compréhension visuelle
+
classification de la fonction de l'image
```

La qualité OCR reste nécessaire, mais elle ne suffit plus.

C'est précisément le type de cas où un VLM devient plus intéressant qu'un moteur OCR
classique.

---

## Conséquence pour US2

Ce cas renforce l'idée que la future couche Vision de QualiCheck ne doit pas être
conçue comme un simple « OCR de capture d'écran ».

Elle pourra devenir un outil complémentaire capable d'analyser certaines propriétés
visuelles que le DOM seul décrit mal, tout en laissant au HTML, au CSS et aux outils
de navigation les informations qu'une image ne peut pas révéler.
