# AI Act et open source — l'exemption qui ne dit pas son nom

## Le principe : une exemption partielle pour les modèles ouverts

L'**AI Act** (règlement UE 2024/1689) reconnaît explicitement la valeur de l'open source pour
la recherche, l'innovation et la croissance économique. Concrètement :

- **Article 2(12)** : le règlement ne s'applique pas aux systèmes d'IA publiés sous licence
  libre et open source, **sauf** s'ils sont mis sur le marché comme systèmes à haut risque, ou
  s'ils relèvent des articles 5 (pratiques interdites) ou 50 (transparence).
- Pour les modèles d'IA à usage général (**GPAI**), les fournisseurs publiés sous licence
  libre/open source bénéficient d'un **régime allégé** sur certaines obligations de l'article 53
  (documentation technique détaillée, information aux fournisseurs en aval).

Toutes les obligations GPAI de base restent dues par tous : documentation technique, respect
du droit d'auteur (directive 2019/790), publication d'un résumé du contenu d'entraînement.
L'exemption ne porte que sur une partie de ces obligations, pas sur leur totalité.

## La limite cruciale : le risque systémique

**L'exemption s'arrête net dès qu'un modèle est classé « à risque systémique »** — et cette
classification ne fait aucune exception pour l'open source.

- **Seuil de présomption** (art. 51(2)) : un GPAI est présumé à risque systémique si la
  puissance de calcul cumulée pour son entraînement dépasse **10²⁵ FLOPs**.
- Ce seuil n'est pas figé : la Commission européenne peut l'ajuster pour suivre l'évolution
  technologique.
- Un modèle peut aussi être désigné à risque systémique par décision de la Commission,
  indépendamment du seuil, s'il présente des « capacités à fort impact » comparables aux
  modèles les plus avancés du marché.
- Conséquences pour un modèle classé ainsi : évaluations adverses (red teaming), suivi des
  incidents graves, cybersécurité renforcée — qu'il soit open source ou non.

## Le paradoxe concret : Llama-3 405B

**Cas d'école** qui illustre parfaitement la limite de l'exemption :

- Llama-3 405B (Meta, publié juillet 2024) a été entraîné avec environ **3,8 × 10²⁵ FLOPs** —
  au-dessus du seuil de présomption.
- Résultat : bien que publié comme « open source » (au sens marketing de Meta), **ce modèle
  ne bénéficie pas de l'exemption open source** de l'AI Act et reste soumis à l'intégralité
  des obligations de risque systémique.

> **Publier ses poids ne suffit pas à échapper à la régulation dès qu'on dépasse un certain
> seuil de puissance de calcul d'entraînement.**

## Application aux modèles de cette veille (à vérifier au cas par cas)

Sur la base des ordres de grandeur de paramètres cités dans les fiches — **et sans connaître
les FLOPs d'entraînement réels, qui dépendent aussi du nombre de tokens et de l'efficacité de
l'entraînement** — plusieurs modèles du tableau pourraient dépasser ou approcher le seuil :

| Modèle | Paramètres | Risque systémique plausible ? |
| --- | --- | --- |
| Llama 4 Maverick | ~400B total | Probable, à vérifier |
| DeepSeek-R1 | 671B total | Probable, à vérifier |
| Qwen3-235B-A22B | 235B total | Possible |
| Mistral Small 4 | 119B total | Moins probable |
| Luciole-23B | 23B | Peu probable |

**Réserve méthodologique** : le nombre de paramètres seul ne détermine pas les FLOPs
d'entraînement (qui dépend aussi du volume de tokens ingérés) — ce tableau est indicatif,
pas une classification officielle. Aucune de ces classifications n'a été confirmée par une
décision de la Commission au moment de la rédaction.

## Trois définitions d'« open source » qui ne se recouvrent pas

C'est le point de jonction avec le reste de la veille (`Fiche de veille — IA : de l'API
fermée à l'Open Source.md`) :

1. **Sens marketing / communication** — ce que Meta, Mistral ou Alibaba appellent
   « open source » dans leurs annonces.
2. **Sens AI Act (art. 2(12))** — accès aux poids/paramètres/architecture/usage, sans
   exigence sur les données d'entraînement, et de toute façon inopérant si risque systémique.
3. **Sens OSAID (OSI)** — Use/Study/Modify/Share, avec exigence de Data Information
   suffisamment détaillées pour reconstruire un système substantiellement équivalent.

Un modèle peut satisfaire la définition 1 sans satisfaire la 2 (s'il dépasse le seuil FLOPs),
et satisfaire la 2 sans jamais satisfaire la 3 (aucune obligation sur les données dans l'AI
Act). **C'est cet écart entre les trois grilles qui rend le titre de la veille — « Mistral
est-il vraiment open source ? » — une vraie question à trois niveaux de réponse, pas une
question rhétorique.**

## Calendrier

- **2 août 2025** : entrée en application des obligations GPAI (documentation, gouvernance).
- **27 juillet 2026** : entrée en vigueur du règlement 2026/1744 (« AI Omnibus »).
- **20 juillet 2026** : publication par la Commission de lignes directrices sur la
  transparence, applicables au 2 août 2026.
- Jusqu'à **2030** : montée en charge progressive des obligations restantes, actes délégués
  possibles pendant 5 ans à partir du 1er août 2024 (reconduction tacite sauf opposition du
  Parlement ou du Conseil).

## Message à retenir

> **L'AI Act ne définit pas l'open source de la même manière que l'OSI, et son exemption
> pour les modèles ouverts a un plafond — le risque systémique. Un modèle massivement
> entraîné peut être « open source » au sens commercial et pleinement régulé au sens
> juridique, au même titre qu'un modèle fermé.**

---

## Sources

- [What Open Source Developers Need to Know about the EU AI Act](https://linuxfoundation.eu/newsroom/ai-act-explainer)
- [EU AI Act: Risk Tiers, GPAI, Timeline — CASRAI](https://casrai.org/dictionary/term/eu-ai-act)
- [AI Act 2024/1689 : texte, calendrier 2025-2027, lecture CNIL](https://reglementation-ia.fr/reglement-2024-1689-ai-act-explique)
- [The 10^25 FLOPs Threshold: GPAI Systemic Risk Classification (2026)](https://mmoww.net/ai/laws/gpai-10-25-flops-threshold/)
- [La Commission publie ses lignes directrices sur la transparence des systèmes d'IA (20/07/2026)](https://france.representation.ec.europa.eu/informations-et-evenements/informations/la-commission-publie-ses-lignes-directrices-sur-la-transparence-des-systemes-dia-2026-07-20_fr)

**Vérification faite le 2026-09-07** via WebSearch/WebFetch — à recontrôler si la veille est
restituée après une évolution réglementaire ultérieure (actes délégués en cours jusqu'en 2030).
