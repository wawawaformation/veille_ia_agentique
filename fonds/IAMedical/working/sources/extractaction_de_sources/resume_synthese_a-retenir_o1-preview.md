# Résumé / synthèse / à retenir — o1-preview et le raisonnement clinique

**Sources primaires** :
- Préprint (décembre 2024) : https://arxiv.org/abs/2412.10849 — titre initial
  *« Superhuman performance of a large language model on the reasoning tasks
  of a physician »*
- Publication *Science* (30 avril 2026) : https://doi.org/10.1126/science.adz4433
  — titre final *« Performance of a large language model on the reasoning
  tasks of a physician »*
- Auteurs affiliés Harvard Medical School / Beth Israel Deaconess Medical
  Center (Boston)
- **Extraits chiffrés obtenus par copie-colle manuelle du PDF** (David,
  2026-08-25) — figures 6-7 et tableaux 1-3, l'extraction automatique ayant
  échoué sur l'encodage du fichier

## Précision importante sur le modèle testé

Deux modèles apparaissent selon les expériences, à ne pas confondre à l'oral :

- **o1-preview** : testé sur les vignettes cliniques (génération de
  diagnostic, raisonnement probabiliste, plans d'examens) — comparé à GPT-4
  et à des cliniciens humains
- **o1** (nom court, sans « -preview ») : testé dans l'étude en conditions
  réelles aux urgences, comparé à **GPT-4o** et à deux médecins seniors
  (attendings) de médecine interne

## Étude en conditions réelles (Figure 7)

**79 cas cliniques réels**, aux urgences d'un grand centre hospitalo-universitaire
de Boston. Comparaison en aveugle entre **deux médecins seniors de médecine
interne, o1, et GPT-4o**, à trois points de diagnostic prédéfinis : triage aux
urgences, évaluation initiale par un médecin, admission à l'hôpital ou en
soins intensifs. Diagnostics différentiels plafonnés à 5 propositions pour
tous les participants. Notation en aveugle par deux médecins seniors
indépendants sur l'échelle de Bond (0 à 5) ; le graphique montre la
proportion de réponses notées 4 ou 5 (diagnostic exact ou très proche).

## Table 1 — trois cas complexes où o1-preview a réussi là où GPT-4 a échoué

| Cas | Diagnostic final | Score Bond GPT-4 | Score Bond o1-preview |
| --- | --- | --- | --- |
| 26-2022 | Histiocytose langerhansienne pulmonaire et hépatique | **0** | **5** |
| 37-2021 | Dermatomyosite anti-MDA5 | **0** | **5** |
| 36-2021 | Infection à *Erysipelothrix rhusiopathiae* | **3** | **5** |

Dans les trois cas, GPT-4 proposait des diagnostics différentiels plausibles
mais ne faisait jamais figurer le bon diagnostic en tête (voire pas du tout) ;
o1-preview le plaçait systématiquement en première position.

## Table 2 — o1-preview propose un plan d'examens : nuance importante

Trois exemples comparant le plan d'examens suggéré par o1-preview au plan
réellement suivi dans le dossier :

- Cas d'hypophosphatémie tumorale (FGF23) : **score 2 — complètement correct**
- Cas de suspicion de maladie de Crohn : **score 1** — les examens auraient
  été utiles ou auraient permis d'arriver au diagnostic par une autre voie
- Cas d'hyperammoniémie / malnutrition : **score 0 — incorrect**, le plan
  suggéré (17 tests dont scintigraphie, lymphangiographie...) n'aurait pas
  été utile

**Ce tableau nuance fortement le mot « superhuman »** : sur la génération de
plans d'examens, o1-preview n'est pas uniforme — un tiers des exemples publiés
comme illustration est un échec net. Point à ne pas passer sous silence à
l'oral.

## Table 3 — raisonnement probabiliste : le résultat le plus quantifié

Comparaison de la probabilité prédite avant/après un test diagnostique, sur 4
scénarios cliniques (pneumonie, cancer du sein, ischémie cardiaque, infection
urinaire), avec l'**erreur absolue moyenne (MAE)** par rapport à la fourchette
de référence établie dans la littérature :

- **o1-preview** : n = 100 prédictions par question
- **GPT-4** : n = 100 prédictions par question
- **Cliniciens humains** : n = 553 (290 internes, 202 médecins seniors, 61
  infirmiers/PA en pratique avancée)

Exemples marquants (MAE, plus bas = meilleur) :
- Ischémie cardiaque, après test positif : **o1-preview 5,7** vs GPT-4 **56,5**
  vs cliniciens **56,3** — écart considérable
- Infection urinaire, avant test : o1-preview **13,8** vs GPT-4 **26,2** vs
  cliniciens **32,4**
- Pneumonie, avant test : o1-preview **31,6** vs GPT-4 **39,5** vs cliniciens
  **47,7**

Sur plusieurs scénarios, **o1-preview est mieux calibré que les cliniciens
humains eux-mêmes** dans l'estimation de probabilités diagnostiques — pas
seulement meilleur que GPT-4. C'est le résultat le plus solide et le plus
chiffrable de l'étude pour justifier le mot « superhuman ».

## Ce qui reste incertain malgré ces chiffres

- Comparaison en vignettes (Tables 1-3, o1-preview) et comparaison en
  conditions réelles (Figure 7, o1) utilisent **deux versions différentes du
  modèle** — à ne pas fusionner dans le discours
- Étude américaine (Boston), hors cadre RGPD
- Aucune précision sur RAG/outils/fine-tuning trouvée dans les parties
  consultées — cohérent avec l'hypothèse « modèle seul » du brief, mais reste
  une inférence par absence de mention, pas une confirmation explicite
- Les auteurs eux-mêmes appellent à des **essais prospectifs** en conclusion
  (réserve assumée)

## Nuance éditoriale à noter

Le mot **« Superhuman »** figurait dans le titre du préprint (2024), disparu
du titre final publié dans *Science* (2026) — mais il survit dans le corps du
texte (*« superhuman diagnostic and reasoning abilities »*) et se justifie
concrètement par la Table 3 (ischémie cardiaque, MAE 5,7 vs ~56 pour GPT-4 et
les cliniciens).

## À retenir pour la slide 2.1

1. **Résultat chiffré** : sur le raisonnement probabiliste (Table 3),
   o1-preview bat GPT-4 **et** les cliniciens humains (n=553) — écart
   spectaculaire sur l'ischémie cardiaque (MAE 5,7 vs ~56)
2. **Architecture** : aucune mention de RAG/outils/agent dans les sources
   consultées — cohérent avec « modèle seul », par absence de mention plutôt
   que confirmation explicite
3. **Limites** : le résultat n'est pas uniforme — sur la génération de plans
   d'examens (Table 2), un exemple sur trois publié est un échec net (score
   0/2) ; deux modèles différents (o1-preview vs o1) selon les expériences ;
   étude américaine, hors RGPD ; les auteurs appellent eux-mêmes à des essais
   prospectifs
4. **Question** : si le modèle seul dépasse déjà les cliniciens sur le
   raisonnement probabiliste, à quel moment le harness/RAG/agent devient-il
   nécessaire — et sur quelles tâches précisément (le plan d'examens semble
   rester un point faible) ?
