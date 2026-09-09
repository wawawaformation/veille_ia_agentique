# Journal de veille

Sessions de veille technique et réglementaire. Entrées les plus récentes en premier.

Les sources suivies et la justification de leur fiabilité sont dans `sources.md`.

## Pourquoi ce journal existe

La compétence C6 exige des « temps de veille planifiés régulièrement (minimum
1h/semaine) ». C'est la seule exigence du référentiel qui ne peut pas être produite
après coup : on ne fabrique pas rétroactivement la preuve d'une régularité.

La veille est pratiquée en dehors de ce projet ; ce journal sert à en conserver la
trace datée, pas à la créer.

## Format d'une entrée

Volontairement léger — un journal qui demande vingt minutes de rédaction par semaine
est un journal abandonné au bout d'un mois.

```markdown
## AAAA-MM-JJ — durée

**Parcouru** : sources consultées

**Retenu** :
- ce qui change quelque chose pour le projet, ou pour la compréhension du domaine

**À creuser** : pistes ouvertes, sans engagement
```

Trois précisions sur le contenu :

- **« Retenu » n'est pas un résumé.** L'intérêt est ce qu'on en fait, pas ce qu'on a
  lu. Une session qui n'a rien donné se note telle quelle : c'est une information.
- **Ce qui contredit un choix du projet mérite d'être noté**, même — surtout — si on
  ne change rien. C'est la trace d'une veille réellement exercée plutôt que d'une
  collecte de confirmations.
- **Le réglementaire compte autant que le technique** (RGPD, accessibilité RGAA,
  AI Act), et il est plus facile à oublier.

---

## 2026-09-09 — Restitution Mini Manifest : Mistral est-il vraiment open source ?

**Parcouru** : vidéo YouTube d'Anaïs (point de départ, distinction
poids/code d'entraînement/données), Free Software Definition et Open
Source AI Definition (OSI), texte de l'AI Act (règlement 2024/1689,
articles 2(12), 51, 53, 54), documentation Ollama et Infomaniak (appel
direct à l'API de liste des modèles) — sources vérifiées par récupération
réelle, listées dans `fonds/mistral_est_il_vraiment_opensource_2026-09-09/working/bibliographie.md`.

**Retenu** :

- Le vocabulaire « open source » recouvre en réalité trois définitions
  distinctes (marketing, AI Act, OSAID) qui ne se recouvrent pas — l'AI
  Act est en fait plus léger que l'OSAID sur les données d'entraînement
  (un résumé suffit, pas la publication complète)
- Llama, Mistral, DeepSeek sont *open weight*, pas *open source* au sens
  strict : les poids sont publiés, mais pas les données ni le code
  d'entraînement complet — ce qui bloque les libertés 1 à 3 du logiciel
  libre
- L'exemption AI Act pour les modèles open source est partielle (deux
  obligations sur quatre seulement) et saute si le modèle est monétisé ou
  dépasse le seuil de risque systémique (10²⁵ FLOPs)
- Twist retenu pour la restitution : un modèle ouvert (Ollama) n'implique
  pas une indépendance réelle si l'infrastructure d'exécution est hébergée
  hors UE (RGPD) — l'alternative souveraine (Infomaniak, Suisse) a un
  catalogue plus restreint. L'indépendance technique n'est pas
  l'indépendance réelle.

**À creuser** : capture d'écran de l'interface Ollama toujours manquante
(`images/photos/slide19_ollama_screenshot.png`) — l'ODP affiche un
placeholder en attendant ; voix haute du bloc 3 (réglementaire/frugalité,
le plus dense) pas encore répétée.

**Format** : trois livrables distincts pour trois usages — `final/*.odp`
(support de présentation live), `final/script_oral.pdf` (aide-mémoire
personnel pour l'oral, gros caractères, une slide par page, minutage
complet), `final/mistral_est_il_vraiment_opensource.pdf` (document de
partage pour lecture asynchrone par les autres apprenants, prose complète
et sourcée) — voir
`fonds/mistral_est_il_vraiment_opensource_2026-09-09/CLAUDE.md` pour le
détail de chaque fichier.

---

## 2026-08-26 — Restitution Mini Manifest : IA, médecine et évolution des paradigmes

**Parcouru** : Dario Amodei (*Machines of Loving Grace*), préprint et publication
*Science* sur o1-preview (raisonnement clinique), rapport Anthropic sur
Claude/Mythos (conception de protéines), étude ASU/Cell Press Blue sur la
prédiction de réponse vaccinale — remontée depuis 4 articles Les Numériques.

**Retenu** :

- La médecine comme terrain d'observation d'un fil rouge plus large : jusqu'où
  va le paradigme LLM actuel, et quelle place reste-t-il aux autres formes
  d'IA — plutôt qu'une succession, une coexistence de familles (modèle seul,
  système agentique, IA spécialisée non-LLM)
- Chiffres extraits directement du préprint o1-preview (copié-collé manuel,
  extraction automatique du PDF ayant échoué) : sur le raisonnement
  probabiliste, o1-preview bat les 553 cliniciens humains eux-mêmes (erreur
  moyenne 5,7 vs 56,3 sur l'ischémie cardiaque) — mais irrégulier sur d'autres
  tâches (échec net sur 1 exemple sur 3 en génération de plans d'examens)
- Apport pratique retenu pour QualiCheck : le choix du paradigme (LLM vs
  modèle spécialisé) devient une décision à justifier, pas un réflexe — un
  modèle spécialisé sur un problème bien défini consomme moins qu'un LLM
  généraliste, ce qui referme la boucle sur l'axe développement durable x IA

**À creuser** : le support de présentation (ODP) reste à finaliser à partir du
plan écrit ; la fresque visuelle timeline (4 miniatures) évoquée en amont n'a
pas été construite, faute de temps.

**Format** : document de partage en Markdown, structure sémantique (titres
`##`/`###`, alt-text sur les 5 images), exporté en PDF via un nouveau style
Pandoc dédié à la veille (`veille.tex`, vert nature `#2E6B3E`,
distinct des styles conception/formation en bleu) — voir
`fonds/IAMedical_2026-08-26/working/ia-medecine-evolution-paradigmes.md`.

## 2026-07-29 — Restitution Mini Manifest (durée non renseignée)

**Parcouru** : OpenLLM France, Lucie (lancement janvier 2025), Luciole (juin 2026), architecture Mamba/State Space Models, ecosystème LLM souverain européen

**Retenu** :

- OpenLLM France pose **l'écologie comme critère de conception**, pas marketing ajouté après coup — analyse de cycle de vie AFNOR pour l'IA frugale, consortium de 300+ orgs, financement BPI France France 2030
- Lucie (janvier 2025) : lancement chahuté pour 5 raisons concrètes (erreurs basiques, pas d'alignement RLHF, infrastructure sous-dimensionnée, communication décalée, timing mauvais)
- Luciole (juin 2026) : répond explicitement à chacun des reproches, trois tailles (1B edge, 8B contexte long, 23B raisonnement), poids/scripts/corpus publiés séparément sous trois licences
- **Essai RAG personnel** : déploiement Ollama/Luciole-8B sur 32 Go RAM — limitation mesurée : prefill lent (134 ms/token vs 32 ms/token Mistral), explication technique : architecture Mamba gain linéaire à l'inférence mais coût au prefill (parallel scan mal implémenté ou absent dans llama.cpp CPU)
- Conclusion pour QualiCheck : **pas d'adoption** (essai démo Mini Manifest, pas décision architecture) — Luciole pertinent pour RAG en production *si* problème latence prefill résolu ; actuellement pipeline existing suffit

**À creuser** : vérifier support parallel scan dans llama.cpp, comparaison latence Mistral vs Luciole en conditions réelles GPU (pas CPU), écosystème Mamba hors Luciole

**Thème** : couvert (souveraineté + frugalité + écologie = trois piliers développement durable x IA)

## 2026-07-15 — durée non renseignée

**Parcouru** : métiers du web à l'ère de l'IA — support
`fonds/metiers_web_ia_2026-07-15/final/veille-metiers-web-ia-202.odp` (13
diapositives) : robots IA sur le web, ralentissement des embauches juniors
(dev, cadres IT), grilles d'analyse REAC (DWWM, CDA, CDUI) face à l'IA,
rédacteur web (métier le plus exposé, 57 % automatisable), community
management et gestion de projet, chiffres macro France.

**Retenu** :

- Le bouleversement documenté n'est pas l'emploi existant mais l'**accès** au
  métier — ralentissement des embauches juniors, pas de vague de licenciements
- Lecture transversale des grilles REAC : plus une compétence est procédurale et
  normée, plus elle est absorbée par l'IA ; plus elle exige un jugement
  contextuel, plus elle résiste
- Tension de fond : la rupture du pipeline de formation — les tâches juniors qui
  formaient les seniors de demain sont les premières automatisées

**À creuser** : recouper les sources macro (Numeum, CREDOC/Arcep, compilation
OCDE/McKinsey/FMI) avant citation formelle — signalé comme non fait dans la
bibliographie d'origine.

**Format — résolu (2026-07-23)** : document de lecture généré
(`fonds/metiers_web_ia_2026-07-15/final/script.md`), reconstruit depuis le texte
des diapositives et les tableaux de compétences. Support live converti en
`.odp` (LibreOffice Impress), conforme à la convention — l'original `.pptx`
supprimé, un seul exemplaire fait foi. Reste un écart mineur : les légendes
visuelles des grilles (couleurs) n'ont pas pu être extraites du texte brut.

**Thème** : couvert par l'axe assigné (développement durable x IA — volet
sociétal/économique) — le thème est large par construction, pas besoin de
vérifier le rattachement veille par veille.

## 2026-05-13 — cybersécurité x IA — durée non renseignée

**Parcouru** : actualité cybersécurité x IA (armement de l'IA) — premier exploit
zero-day dont le code semble généré par une IA (Google Threat Intelligence Group),
malware Android PromptSpy pilotant l'écran de la victime en temps réel, usage des
LLM par des groupes APT étatiques (APT45 Corée du Nord, APT27/UNC2814 Chine,
groupes russes), « Shadow APIs » donnant un accès non officiel à des modèles
comme Gemini ou Claude (étude CISPA).

**Retenu** :

- L'IA réduit fortement le délai entre découverte d'une vulnérabilité et son
  exploitation — glissement vers des agents semi-autonomes qui automatisent des
  phases entières de reconnaissance et d'attaque
- Deux sources citées explicitement en fin de rapport : TheHackerNews et Korben —
  Korben figure déjà dans le dossier FreshRSS « IA — vulgarisation et outils »
  (cf. `sources.md`), cohérence confirmée entre veille et outillage

**À creuser** : —

**Écart avec le thème assigné, résolu** : ce rapport porte sur la cybersécurité,
pas sur le développement durable x IA. Explication confirmée par David : le
collectif **Mini Manifest a été lancé le 13 mai** — cette pièce, datée du jour
même, est antérieure à l'attribution du thème (cf. `README.md` §Dispositif). Pas
un écart à corriger, un repère temporel sur le début du dispositif.

Document source : `veille_13_mai_David.pdf`.

## 2026-05-13 — mise en place FreshRSS — durée non renseignée

**Parcouru** : mise en place de l'instance FreshRSS personnelle (Docker + Caddy,
domaine `rss.david-legrand.fr`) — rédaction d'un article de synthèse sur la
démarche et les choix techniques.

**Retenu** :

- Choix FreshRSS confirmé pour trois raisons — libre (pas de dépendance à un
  service pouvant fermer ou devenir payant), sobre (pas de push permanent),
  organisation par catégories — cohérent avec la justification déjà donnée dans
  `sources.md`
- SQLite retenu plutôt que MariaDB/PostgreSQL pour un usage personnel : évite un
  conteneur de base de données supplémentaire, suffisant à cette échelle
- Piège identifié dès la mise en place, à ne pas reproduire : ne pas ajouter tous
  les flux d'un coup — « 500 articles non lus » devient aussi décourageant qu'une
  boîte mail pleine. Démarrer petit, ajuster au fil de l'eau, supprimer les flux
  qui ne servent jamais
- Catégories envisagées dès le départ : IA, Python, Développement web, Linux,
  RGPD/CNIL/AI Act, Pédagogie, Cybersécurité — périmètre plus large que le seul
  thème Mini Manifest, cohérent avec la collecte étendue déjà notée dans
  `sources.md`

**À creuser** : —

Document source : `12_mai_article-freshrss-docker_.pdf`. C'est littéralement le
document d'origine de l'outillage décrit dans `sources.md` §Outils d'agrégation —
à citer depuis là plutôt que dupliquer son contenu.

<!-- Les entrées commencent ici, la plus récente en premier. -->
