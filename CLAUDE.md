# Veille (David) — dépôt autonome

Veille technique et réglementaire de David — compétence C6 de la certification
RNCP37827, dans le cadre du collectif de formation **Mini Manifest**.

Ce dépôt a été séparé de `QualiCheck` (`docs/jury/veille/`) le 2026-08-28 : la
veille, pratique personnelle C6 sans rapport avec le produit, n'avait
structurellement rien à faire dans le dépôt fil rouge. Voir la section
« Pièges déjà rencontrés » ci-dessous pour le détail de la séparation.

## Contexte à ne pas oublier

- **Thème assigné à David** : « Développement durable x IA » (sociétal,
  environnemental, économique) — voir `README.md`. **Ce thème est volontairement
  large : ne pas vérifier le rattachement thème par thème pour chaque veille**,
  ce n'est plus une question à se poser.
- **Un second axe existe**, plus personnel et plus technique : développement IA
  agentique (frameworks, agents, outillage) — voir `candidats-sources.md`. Ne pas
  le confondre avec le thème Mini Manifest ci-dessus.

## Où lire quoi

- `README.md` — dispositif Mini Manifest (objectif, format de session, thèmes des
  participants), convention de dossier, inventaire du fonds
- `journal.md` — entrées datées, format volontairement léger. **Seule preuve de
  régularité exigée par C6** : impossible à produire rétroactivement, donc écrire
  les entrées vraiment au moment de la veille, pas après coup
- `sources.md` — sources réellement suivies + justification de fiabilité (auteur
  identifié, compétences confirmées, contenu daté et sourcé)
- `candidats-sources.md` — sources vérifiées (flux RSS récupérés et validés) mais
  pas encore adoptées dans `sources.md`
- `fonds/` — le matériau lui-même (documents, présentations, PDF, notes)
- `accessibilite-formats.md` — aide-mémoire PDF/ODP/MD/ODT pour produire un
  format accessible (critère C6, renvoie à Valentin Haüy / AcceDe)
- `referentiel-c6.md` — extrait du référentiel officiel (compétence, savoir-faire,
  critères de performance/réussite) tel qu'il figure dans
  `/projets/formation_dev_ia_agentique/référentiel/`

## Convention de dossier dans `fonds/`

Chaque veille est un dossier `nom_snake_case_AAAA-MM-JJ/`, avec :

- `working/` — brouillons, matériaux de travail (montage vidéo, extraction brute,
  sources non retravaillées)
- `final/` — le livrable achevé

Le suffixe de date ne dépend pas d'avoir une paire cible/réel : il marque un
contenu **constaté** après coup plutôt qu'une **intention**. Même logique que la
convention `X_reel.drawio` du skill `~/.claude/skills/schemas-drawio/SKILL.md`.

## Format des restitutions — deux rôles distincts

- **ODP** (LibreOffice Impress) : support de présentation live, pas le document
  diffusé.
- **MD ou ODT** : le document de partage réel, structure sémantique rigoureuse
  (styles de titre, pas de mise en forme manuelle) — c'est lui qui porte la
  charge d'accessibilité, pas l'ODP.

## Pièges déjà rencontrés — à ne pas répéter

- **Ne pas dupliquer le fonds ailleurs.** Un renvoi externe
  (`formation_dev_ia_agentique/veille/`) a existé puis a été abandonné le
  2026-07-23 au profit d'une centralisation complète dans `fonds/` — un seul
  exemplaire de chaque fichier fait foi.
- **Vérifier toute URL de flux RSS par récupération réelle** avant de la lister
  dans `sources.md` ou `candidats-sources.md` — jamais reconstituée de mémoire.
- **Un PPTX n'est pas un ODP.** Convertir réellement (`soffice --headless
  --convert-to odp`), pas seulement renommer l'extension.
- **Un dossier déplacé peut être un dépôt git imbriqué** (gitlink vide au commit
  si on ne fait pas attention) — c'est arrivé avec `LLM-Engineers-Handbook`, qui
  n'est d'ailleurs pas de la veille et ne doit pas vivre ici.
- **`git add -A` peut re-suivre un dossier volontairement exclu** (ex.
  `dev_durable_.../working/videos/`, ~180 Mo, laissé non suivi) s'il change de
  chemin entre deux commits — vérifier `git status` avant de committer plutôt
  que de faire confiance à un exclude précédent.
- **Séparation d'avec `QualiCheck` (2026-08-28).** Le dossier vivait dans
  `docs/jury/veille/` du dépôt produit ; décision actée dans le `TODO.md` de
  `QualiCheck` le 2026-08-25 (mélange produit/veille/jury dans un même dépôt,
  la veille n'ayant structurellement aucun rapport avec le produit). Historique
  git récupéré via `git subtree split --prefix=docs/jury/veille` depuis
  `QualiCheck` (aucune réécriture de l'historique de `QualiCheck` lui-même,
  juste un commit de suppression par-dessus `dev`, non poussé pour l'instant).
  `accessibilite-formats.md` copié ici (n'était référencé que par la veille) ;
  le reste de `docs/jury/` (décisions, RGPD, livrets) reste dans `QualiCheck`.

## Changelog

Ce dépôt est désormais autonome : plus de `CHANGELOG.md` ni `CLAUDE.md` racine
partagé avec `QualiCheck` à référencer. Il n'existe pas encore de
`CHANGELOG.md` propre à ce dépôt — à créer si un suivi horodaté séparé de
l'historique git est souhaité.
