# Résumé / synthèse / à retenir — Prédiction de la réponse vaccinale

**Sources primaires** :
- Publication scientifique (*Cell Press Blue*, 20 août 2026) —
  https://doi.org/10.1016/j.cpblue.2026.100088
- ASU News (Arizona State University), *Why immune responses to vaccines vary
  from person to person* —
  https://news.asu.edu/20260820-science-and-technology-why-immune-responses-vaccines-vary-person-person

## Résumé

**Architecture** : un **modèle de deep learning spécialisé** — explicitement
**ni un LLM, ni un système agentique**. Le modèle réalise une « analyse de
motifs » à travers un panel d'anticorps : *« Their deep learning model
analyzed patterns across the antibody panel, combining many measurements into
a broader immune profile »*.

**Données biologiques en entrée** :
- 8 687 échantillons sanguins provenant de 4 089 participants
- Mesure d'anticorps contre **185 antigènes distincts** (virus courants,
  bactéries, cibles d'auto-immunité)
- Population mixte : volontaires sains **et** patients immunosupprimés (VIH,
  myélome multiple, malignités, maladies auto-immunes, transplantés)

**Prédiction exacte** : la force de la réponse immunitaire au **vaccin
COVID-19**, *avant* son administration — le modèle identifie les répondeurs
forts vs faibles à partir des signatures d'anticorps préexistants.

**Résultats chiffrés** :
- Les groupes immunosupprimés montrent des réponses vaccinales « émoussées »
  (attendu, mais désormais quantifié par le modèle)
- **5-6 % des participants sains** présentent eux aussi des réponses faibles
  — résultat moins attendu, sur une population a priori non à risque
- Certains anticorps préexistants (*Staphylococcus aureus*, VRS) corrèlent
  avec des réponses vaccinales plus fortes

## Confirmation du contre-exemple

Aucune ambiguïté dans les sources consultées : ce travail ne mobilise ni LLM,
ni RAG, ni agent — c'est un modèle d'apprentissage automatique spécialisé en
analyse de données biologiques quantitatives, sur un problème de prédiction
bien défini (force de réponse immunitaire à partir d'un profil d'anticorps).

## À retenir pour la slide 4.1

1. **Contre-exemple volontaire** : confirmé par les deux sources — ni LLM, ni
   agent, ni RAG
2. **Méthode** : profil d'anticorps (185 antigènes, 8 687 échantillons) →
   deep learning spécialisé → prédiction de la force de réponse vaccinale
3. **Message** : l'équation « IA = LLM = agent » est fausse — un problème de
   prédiction bien défini sur données biologiques structurées se prête
   naturellement à un modèle spécialisé
4. **Chiffre marquant** : même 5-6 % des personnes en bonne santé (pas
   seulement les immunosupprimés) répondent faiblement au vaccin — résultat
   contre-intuitif que le modèle permet d'anticiper avant l'injection
