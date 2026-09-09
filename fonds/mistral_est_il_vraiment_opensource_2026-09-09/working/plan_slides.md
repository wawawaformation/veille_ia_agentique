# Plan des slides — Veille Mistral est-il vraiment open source ?

**Durée cible initiale** : 10 minutes
**Durée réelle calculée** : 9:30 (voir décompte slide par slide ci-dessous) — 30s de marge sous la cible de 10:00
**Format** : ODP (LibreOffice Impress) ou slides simples (HTML/Markdown)  
**Public** : Mini Manifest (mixte : tech/non-tech)

---

## INTRO & CONTEXTE (0:15 réel)

### Slide 1 : Titre
- **Titre** : « Mistral est-il vraiment open source ? »
- **Sous-titre** : Décortiquer le continuum d'ouverture en IA
- **Visuel : image générée par IA** (`photos/slide1.jpg`) — un chat roux assis à côté d'une marionnette Pinocchio, le nez qui s'allonge en écho direct au « *vraiment* » du titre (mensonge/exagération). Accroche visuelle forte, se lit sans un mot, pas de contenu à expliquer à l'oral
- **Timing** : 0:00
- **Durée** : 0s — slide de garde, affichée en fond pendant que l'oral démarre directement sur l'agenda (slide 2)

### Slide 2 : Agenda
- **Texte** :
  - 📚 Bloc 1 : Logiciel libre et standards ouverts
  - 🤖 Bloc 2 : Le continuum d'ouverture en IA
  - ⚖️ Bloc 3 : Réglementaire + frugalité
  - 🔧 Bloc 4 : Ollama, conclusion et twist final
- **Visuel : aucun (emojis suffisent)** — repère visuel léger, pas besoin de plus pour un sommaire
- **Timing** : 0:00
- **Durée** : 15s

---

## BLOC 1 — LOGICIEL LIBRE ET STANDARDS OUVERTS (1:55 réel, cible initiale 3-3:30 min)

### Slide 3 : Intro Bloc 1
- **Texte** :
  - Pour comprendre « open source » en IA, il faut d'abord comprendre le logiciel libre traditionnel
  - Trois concepts clés : **libertés**, **standards**, **interopérabilité**
- **Visuel : aucun** — slide de transition orale, texte minimal suffit
- **Timing** : 0:15
- **Durée** : 20s

### Slide 4 : Les 4 libertés du logiciel libre
- **Titre** : Les 4 libertés (FSF, Richard Stallman)
- **Contenu** (avec blocs distincts) :
  - Liberté 0 : Utiliser
  - Liberté 1 : Étudier et modifier
  - Liberté 2 : Redistribuer
  - Liberté 3 : Redistribuer modifiée
- **Analogie à dire** : « C'est comme une recette de cuisine : tu peux la faire, la modifier (ajouter du sel), la donner à tes amis, et partager ta version améliorée. »
- **Point clé oral** : « L'important n'est pas juste pouvoir utiliser — c'est aussi pouvoir modifier et partager. »
- **Visuel : photo (recette de cuisine annotée)** — ancre concrètement l'analogie dite à voix haute, évite que ça reste abstrait dans l'esprit de l'audience
- **Timing** : 0:35
- **Durée** : 45s

### Slide 5 : Standards ouverts
- **Titre** : Standards ouverts ≠ Logiciel libre
- **Contenu** :
  - Un standard ouvert = une spécification commune que tout le monde peut respecter
  - USB, TCP/IP, HTTP, HTML
- **Analogie à dire** : « USB : peu importe si tu as un iPhone, un Samsung, un Windows ou un Mac. Tant qu'on respecte le standard USB, ça communique. On s'en fout du matériel derrière. »
- **Point clé oral** : « Standard ouvert = liberté d'interagir et de changer de prestataire sans verrouillage. Pas forcément liberté de modifier le code. »
- **Visuel : patchwork 2×2** (`photos/slide5_usb_patchwork.jpg`) — titre « Universal Serial Bus » en haut, puis sigle USB stylisé / souris filaire / manettes filaires / disque dur externe (clipart) — montre 4 appareils très différents reliés au même standard
- **Timing** : 1:20
- **Durée** : 30s

### Slide 6 : Transition vers IA
- **Texte** :
  - Maintenant qu'on a ces concepts clés…
  - La question : « Comment appliquer ça à l'IA ? »
  - Parce qu'un modèle d'IA n'est pas qu'un programme.
- **Visuel : aucun** — transition orale, pas de nouveau concept à ancrer visuellement
- **Timing** : 1:50
- **Durée** : 20s

---

## BLOC 2 — LE CONTINUUM D'OUVERTURE EN IA (3:45 réel, cible initiale 4 min)

### Slide 7 : Pourquoi IA complique la notion
- **Titre** : Un modèle d'IA ≠ Un programme classique
- **Contenu** :
  - Logiciel : le code source explique tout
  - IA : son comportement vient de **3 composantes indépendantes** :
    - Les **poids** (paramètres appris)
    - La **recette d'entraînement** (code + hyperparamètres)
    - Les **données** (le matériau brut)
- **Visuel : côte à côte (schéma comparatif)**
  - **Gauche** : fichier Python/code source (icône + quelques lignes lisibles) — « 1 truc = le code »
  - **Droite** : 3 boîtes séparées — « 3 composantes indépendantes »
- **Justif** : C'est le pivot conceptuel du bloc 2. Le visuel concret (code Python reconnaissable) vs abstrait (3 boîtes) rend le saut évident sans dépendre de l'oral seul. Robuste pour mixte tech/non-tech.
- **Timing** : 2:10
- **Durée** : 40s

### Slide 8 : Les 3 composantes — Analogie gâteau
- **Titre** : Comment fabrique-t-on un modèle ? (analogie du gâteau)
- **Point clé oral** : « Si tu as juste le gâteau fini, tu peux le manger, mais tu ne sais pas comment il a été fait, et tu ne peux pas le reproduire. »
- **Visuel : côte à côte**
  - **Gauche** : 2 photos (`photos/slide8_ingredients.jpg` farine+œuf, `photos/slide8_gateau_fini.jpg` gâteau fini) — l'analogie concrète en 2 volets (pas 3 : le volet « recette/processus » n'a pas de photo dédiée, seulement le schéma labellisé à droite le couvre)
  - **Droite** : schéma labellisé (`slide8_gateau_composantes.drawio` : 3 boîtes Poids = gâteau | Recette = processus | Données = ingrédients) — la correspondance IA explicite, y compris pour la recette absente en photo
- **Justif** : La photo ancre le concret, le schéma labellisé élimine l'ambiguïté « c'est quoi dans le modèle d'IA ? ». Slide précédente a posé le problème (code ≠ 3 boîtes), celle-ci propose la solution avec les deux registres (concret+abstrait).
- **Timing** : 2:50
- **Durée** : 40s

### Slide 9 : OSAID — Distinction open weight vs open source
- **Titre** : Open weight vs Open source : la distinction critique
- **Contenu** (tableau 2×3) :
  |  | Open weight | Open source |
  | --- | --- | --- |
  | **Poids** | ✓ Public | ✓ Public |
  | **Recette + données** | ✗ Fermé | ✓ Public |
  | **Libertés FSF** | Liberté 0 seule | Libertés 0-3 ✓✓✓ |

- **Analogie à dire** : « Open weight = je te montre le gâteau fini et l'emballage fantastique, mais pas la recette ni les ingrédients. Tu ne peux pas vérifier les allergies, les biais... Open source = je te montre tout. C'est la différence entre confiance aveugle et confiance vérifiée. »
- **Point clé oral (texte sur slide)** : « Filtre d'amour » : open weight te fait confiance au vendeur. Open source te permet d'auditer toi-même.
- **Visuel : 2 photos côte à côte** — `photos/slide9_gateau_emballe.jpg` (brioche tressée dorée présentée dans un linge, symbolise « tu vois le résultat mais pas comment c'est fait ») et `photos/slide8_gateau_fini.jpg` réutilisée (gâteau en parts visibles, symbolise « transparence »). Aucune des deux photos ne montre littéralement un emballage fermé ni une recette écrite — la distinction se fait à l'oral avec l'analogie, pas par le contenu visuel des photos elles-mêmes
- **Timing** : 3:30
- **Durée** : 35s

### Slide 10 : Exemples concrets — Continuum
- **Titre** : Le continuum en 4 catégories
- **Contenu** (4 boîtes avec exemples, PAS tous les 27 modèles) :
  1. **Fermé/API** : GPT, Claude, Gemini (accès distant seulement)
  2. **Open weight** : Llama, Mistral, DeepSeek (poids publics)
  3. **Open weight++** : gpt-oss, Gemma, Qwen (poids + doc partielle)
  4. **Open source** : OLMo, Apertus, Luciole (poids + recette + données)
- **Note** : « Fichier détaillé en annexe avec les 27 modèles analysés. »
- **Visuel : schéma (gradient/spectre en 4 zones, positionnant Mistral)** — c'est le diagramme le plus réutilisable de toute la présentation (repris slide 20), mérite d'être produit proprement une fois (drawio) plutôt qu'en tableau texte
- **Timing** : 4:05
- **Durée** : 40s

### Slide 11 : Exemple 1 — Biais invisibles
- **Titre** : Pourquoi la distinction importe vraiment
- **Sous-titre** : Exemple 1 : Les données cachées
- **Contenu** :
  - Imagine : un modèle entraîné sur des données contaminées par la propagande d'un dictateur.
  - **Open weight seul** : tu goûtes le gâteau, c'est bizarre, mais tu ne sais pas d'où ça vient.
  - **Open source** : tu vois la recette et les ingrédients. Tu repères : « Ah, c'est cette source contaminée ! »
- **Analogie déjà dite** : « Eau contaminée invisible dans le gâteau. »
- **Point clé oral** : « L'indépendance de penser dépend de la transparence de la fabrication. »
- **Visuel : photo (eau trouble vs eau claire)** — rend visible un danger normalement invisible (le biais), c'est tout l'argument de la slide en une image
- **Timing** : 4:45
- **Durée** : 35s

### Slide 12 : Exemple 2 — Cas Lucie
- **Titre** : Exemple 2 : Erreurs méthodologiques révélées
- **Contexte** : OpenLLM France, janvier 2025
- **Contenu** :
  - Lucie lancée en version inachevée, non censurée
  - Communauté a vu les erreurs et dénoncé
  - Forcé de corriger
  - **Si Lucie était fermée** : personne n'aurait jamais su
- **Analogie à dire** : « Restaurant qui ferme pour refaire la cuisine après avoir eu des bactéries. »
- **Point clé oral** : « L'ouverture permet la correction communautaire. »
- **Visuel : photo (panneau « fermé pour travaux » sur une devanture)** — c'est un cas réel (Lucie), l'image ancre que ce n'est pas de la théorie
- **Timing** : 5:20
- **Durée** : 20s

### Slide 13 : Transition vers Bloc 3
- **Texte** :
  - Maintenant, une question surgit : comment **les gouvernements** définissent-ils « open source » ?
  - L'UE a répondu avec l'**AI Act**. Et la réponse n'est pas celle qu'on attendrait…
- **Visuel : aucun** — transition orale
- **Timing** : 5:40
- **Durée** : 15s

---

## BLOC 3 — RÉFLEXIONS ET IMPLICATIONS (2:00 réel, cible initiale 1:30-2 min)

### Slide 14 : Les 3 définitions qui ne se recouvrent pas
- **Titre** : Attention : 3 définitions différentes du mot « open source »
- **Point clé oral** : « Aucune ne recouvre exactement les autres. D'où la confusion. »
- **Visuel : côte à côte**
  - **Gauche** : tableau 3×3 (contexte/définition/exemple) — la clarté textuelle
  - **Droite** : schéma Venn à 3 cercles (partiellement chevauchés) — montre physiquement le non-recouvrement
- **Justif** : Le tableau dit QUOI (définitions précises). Le Venn dit COMMENT (visuellement, ce n'est pas des zones isolées, c'est pas complètement fusionnées). Ensemble = complet.
- **Timing** : 5:55
- **Durée** : 25s

### Slide 15 : AI Act — Exemption et seuil
- **Titre** : L'Union européenne exempt les modèles « open source »
- **Contenu** :
  - Article 2(12) : exemption pour open source (risque systémique allégé)
  - **Mais** : seuil à 10²⁵ FLOPs (article 51(2))
  - **Paradoxe** : Llama-3 405B ≈ 3,8 × 10²⁵ FLOPs → **au-dessus du seuil**
  - Même si open source (théoriquement), il subirait les règles de risque systémique

- **Point clé oral** : « La loi dit que l'open source c'est moins risqué. Mais si c'est trop puissant, même open source, tu dois te conformer. »
- **Visuel : schéma (jauge/règle avec seuil 10²⁵ FLOPs, Llama-3 405B positionné au-dessus)** — un seuil numérique abstrait devient concret quand on voit visuellement que le modèle le dépasse
- **Timing** : 6:20
- **Durée** : 40s

### Slide 16 : Frugalité — Local vs cloud
- **Titre** : La fausse bonne idée : local = plus écolo ?
- **Texte clé** :
  - Intuition : faire tourner un modèle chez moi, c'est plus écolo qu'une API cloud.
  - **Réalité : c'est plus compliqué.**
- **Analogie à dire** : « Avoir une mini-piscine chez toi vs piscine communautaire. Si tu l'utilises 1h/semaine, c'est énorme gaspillage d'eau. La communautaire, 500 personnes 24/7 = beaucoup plus efficace. »
- **Point clé oral** : « Paradoxe de Jevons : plus c'est efficace, plus on l'utilise. Consommation totale monte quand même. »
- **Visuel : photo (mini-piscine privée vs piscine communautaire bondée)** — c'est l'analogie centrale du bloc, une image comparative fait ressentir le contre-intuitif immédiatement
- **Timing** : 7:00
- **Durée** : 25s

### Slide 17 : Le seuil magique : 85 % d'utilisation GPU
- **Titre** : Quand est-ce que local devient compétitif ?
- **Contenu** :
  - **En dessous 85 % d'utilisation GPU** : mieux vaut cloud (batching, efficacité datacenter)
  - **Au-dessus 85 %** : local devient compétitif
  - Datacenter a : batching, 24/7 saturé, PUE efficace (1.05-1.40)
- **Point clé oral** : « Il faut vérifier les chiffres. Pas supposer. »
- **Visuel : schéma (jauge/curseur à 85 % avec bascule cloud/local)** — prolonge visuellement la piscine de la slide précédente avec le chiffre précis, évite de juste balancer un pourcentage à l'oral sans support
- **Timing** : 7:25
- **Durée** : 20s

### Slide 18 : Conclusion Bloc 3
- **Titre** : Pragmatisme
- **Contenu** (bullet points) :
  - Local **pas forcément** mieux
  - API cloud **pas forcément** pire
  - **L'intérêt de open weight** : tu peux décider au cas par cas
- **Visuel : aucun** — slide de synthèse orale, le texte fait le travail
- **Note oral** : quasi fusionnée avec S17 — enchaîner directement en fin de S17 sans marquer de pause, cette slide n'est qu'un rappel visuel de la conclusion déjà dite
- **Timing** : 7:45
- **Durée** : 10s

---

## BLOC 4 — OLLAMA, CONCLUSION ET TWIST FINAL (1:20 réel)

*Renommé : cette section ne parle pas que d'Ollama (slide 19), elle porte aussi
la conclusion générale de toute la veille (slide 20) et le twist RGPD/Infomaniak
(slide 21). L'ancien intitulé « BLOC 4 — OLLAMA » était trompeur.*

### Slide 19 : Ollama — Illustration concrète
- **Titre** : Ollama : comment ça fonctionne ?
- **Contenu** :
  - Plateforme MIT (code ouvert)
  - Catalogue : **exclusivement open weight + open source** (zéro fermé/API)
  - 3 modes d'accès :
    1. **Local** (CLI gratuit) → données chez toi
    2. **API** (gratuit, limité)
    3. **Cloud Pro** (20 $/mois, peak hours variable) → infrastructure USA
  - Exemples : Llama, OLMo, Gemma, Llama Vision
- **Point clé oral** : « La monétisation ? Infrastructure cloud, pas les modèles. »
- **Visuel : capture d'écran (interface Ollama, catalogue + les 3 modes)** — c'est du concret/vécu (l'utilisateur a l'abonnement Pro), une vraie capture vaut mieux qu'une reconstitution
- **Timing** : 7:55
- **Durée** : 20s

### Slide 20 : Conclusion générale — La réponse simple
- **Titre** : Mistral est-il vraiment open source ?
- **Réponse directe** :
  - Non. Mistral est **open weight**.
  - Pour être open source, il faudrait aussi publier les données et la recette d'entraînement.
- **Implication technique** :
  - « Open source » n'est pas une case qu'on coche.
  - C'est un **continuum**, et c'est un **choix**.
- **Visuel : schéma (reprise du gradient de la slide 10, Mistral repositionné)** — boucler sur le même visuel que le bloc 2 crée une cohérence mémorable, pas besoin d'un nouveau schéma
- **Timing** : 8:15
- **Durée** : 20s

### Slide 21 : Twist final — Le vrai dilemme
- **Titre** : Mais attends…
- **Contenu** (impact, pas trop de texte) :
  - Tu dis « Je vais utiliser Ollama Cloud, c'est open source donc indépendant ! »
  - **Réalité** : Infrastructure USA (transfert de données hors UE, article 44 RGPD)
  - **Alternative** : Infomaniak (Suisse) — RGPD conforme (adéquation UE), mais catalogue plus restreint (8 modèles, dont **Apertus** — l'open source suisse déjà cité en bloc 2)
  - **Le vrai dilemme** : large choix (Ollama) OU souveraineté (Infomaniak) — rarement les deux à la fois
- **Ton oral** : Léger, ironique, pas cynique. Genre « Eh merde… »
- **Point clé** : « Indépendance technique ≠ Indépendance réelle. Il faut regarder l'infrastructure aussi. »
- **Visuel : schéma (2 colonnes Ollama USA vs Infomaniak Suisse, avantages/inconvénients de chaque)** — le twist n'est plus juste « y'a un problème », c'est un vrai compromis à deux faces, plus honnête et plus riche pédagogiquement
- **Timing** : 8:35
- **Durée** : 40s — slide dense avec 4 points + ton particulier à installer, ne pas la précipiter

---

## FERMETURE (15 sec)

### Slide 22 : Questions
- **Texte** : Questions ?
- **Contact** : [email ou infos si pertinent]
- **Visuel : aucun** — pas besoin, l'audience est déjà sur l'image forte de la slide précédente
- **Timing** : 9:15
- **Durée** : 15s (fin de présentation : 9:30)

---

## Notes de mise en pratique

### Design visuel
- Fond clair (blanc ou gris très léger) — accessibilité
- Polices sans-serif (Helvetica, Arial, Roboto) — lisibilité à distance
- Couleurs : max 3 couleurs + noir/gris (pas arc-en-ciel)
- Texte gros : min 28pt pour les titres, 18pt pour le contenu

### Rythme oral
- **Diapositives de contenu dense** (slides 4, 8, 10, 14, 15) : pauser 10-15 sec, laisser lire
- **Analogies** (slides 4, 5, 8, 9, 16) : les dire oralement avec intonation, pas lire la slide
- **Bloc 3 (casse-gueule)** : parler lentement, articulation claire (AI Act + physique = dense)

### Transitions
- Toujours annoncer oralement la transition (slide 6 → Bloc 2, slide 13 → Bloc 3)
- Pause de 2-3 sec entre les blocs (respiration de l'audience)

### Timing critique
- **Bloc 1** : 1:55 réel (comprimé — transitions S3/S6 resserrées, attention à ne pas les précipiter à l'oral au point de perdre l'auditoire)
- **Bloc 2** : 3:45 réel (S8 et S11 resserrées, mais restent les slides de contenu les plus longues — ne pas couper davantage sans relire l'oral)
- **Bloc 3** : 2:00 réel (S14 allégée à l'oral — commenter surtout le Venn — et S18 quasi fusionnée dans S17 ; reste le bloc le plus technique, bien préparer la voix)
- **Bloc 4** : 1:20 réel (S20 resserrée sur la réponse directe ; le twist S21 garde toute sa durée — c'est lui qui porte l'impact, ne pas le précipiter)
- **Total réel : 9:30**, contre une cible initiale de 10:00 — **30s de marge**, confortable

### Annexes (fichiers à disposition, pas sur slides)
- `presentation_bloc_1_logiciel_libre.md` (complet)
- `presentation_bloc_2_ia_ouverture.md` (27 modèles en annexe)
- `presentation_bloc_3_reflexions_implications.md` (sources détaillées)
- `analogies_metaphores.md` (notes d'orateur)
- `bibliographie.md` (sources vérifiées)
 