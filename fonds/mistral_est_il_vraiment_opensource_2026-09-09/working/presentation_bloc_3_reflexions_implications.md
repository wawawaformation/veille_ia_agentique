# Bloc 3 — Réflexions et implications

**Durée cible** : 1:30-2 minutes

---

## Part 1 : AI Act — ce que dit la loi

L'Union européenne, avec l'**AI Act** (2024), a dû trancher : qu'est-ce qu'un modèle « open source » pour la régulation ?

### L'exemption open source (article 2(12))

L'AI Act **exempte** les modèles open source des règles de risque systémique.

Raison : si le code et les poids sont transparents, la communauté peut auditer et corriger. Moins de risque centralisé.

### Mais il y a un seuil (article 51(2))

Exemption valide **sauf si** le modèle dépasse 10²⁵ FLOPs (environ 10 milliards de milliards de multiplications).

**Cas réel** : Llama-3 405B ≈ 3,8 × 10²⁵ FLOPs → **au-dessus du seuil**. Même open source (théoriquement), il n'échapperait pas aux règles de risque systémique.

### Les trois définitions qui ne se recouvrent pas

| Contexte | « Open source » signifie | Exigence sur les données |
|---|---|---|
| **Marketing commercial** | Poids publiés, un peu transparent | Rien |
| **AI Act (légal)** | Licence libre + paramètres/architecture publics + **non monétisé** | Un **résumé** du contenu d'entraînement (art. 53(1)(d)) |
| **OSAID (OSI)** | Utiliser / étudier / modifier / redistribuer | Infos **suffisantes pour reconstruire** |

> **Attention (vérifié le 2026-09-08)** : la définition AI Act est plus **légère**
> que l'OSAID, mais pas vide. Le régime allégé dispense de la doc technique
> (art. 53(1)(a-b)) et du représentant UE (art. 54), mais **pas** de la politique
> copyright (53(1)(c)) ni du résumé des données d'entraînement (53(1)(d)).
>
> Deux conditions souvent oubliées : **non-monétisation** (considérant 103) et
> exemption inopérante au-delà du seuil FLOPs. Ne pas affirmer à l'oral que
> « Mistral/Llama sont open source au sens AI Act » — Mistral monétise, la licence
> Llama a des restrictions d'usage : la qualification est un débat juridique, pas
> une évidence.

→ **Aucune ne recouvre exactement les autres.**

---

## Part 2 : La fausse bonne idée — local vs API distant

Intuition : « Je fais tourner un modèle chez moi, c'est forcément plus écolo et moins cher qu'une API cloud. »

**Réalité : c'est plus compliqué.**

### Le seuil magique : ~85 % d'utilisation GPU

- **En dessous** : mieux vale faire tourner en API cloud (batching, efficacité datacenter)
- **Au-dessus** : local devient compétitif

**Pourquoi ?** Le datacenter a :
- **Batching** : traiter 8-20 requêtes à la fois au lieu d'une seule
- **Taux d'utilisation** : GPU saturé 24/7, pas 2h par semaine
- **PUE** (Power Usage Effectiveness) : 1.05-1.40 (peu de surcharge)

### Le paradoxe de Jevons

Cas réel : GPT-4o, ~0,43 Wh par requête.

700M requêtes/jour → **35 000 foyers américains** alimentés par cette seule consommation.

Paradoxe : plus c'est efficace, plus on l'utilise → consommation totale monte.

### La conclusion pragmatique

- Local **pas forcément** mieux (sauf si tu as vraiment une utilisation intensive)
- API cloud **pas forcément** pire (si le fournisseur optimise)
- **Vigilance** : demander à OpenAI/Google/Anthropic leurs chiffres de PUE, pas supposer

→ C'est ce qui rend le choix open weight intéressant : **tu peux décider, au cas par cas, si tu préfères local ou cloud.**

---

## Point synthétique

La régulation (AI Act) et l'écologie (frugalité/Jevons) montrent que « open source » n'est pas qu'une question éthique.

C'est une **question d'indépendance, de transparence et de choix réel**.

Et c'est pour ça que le titre de la veille compte : **« Mistral est-il vraiment open source ? »**

Réponse honnête : non, pas au sens strict. Mais il est open weight — et ça ouvre des possibilités que Fermé/API ne permet pas.
