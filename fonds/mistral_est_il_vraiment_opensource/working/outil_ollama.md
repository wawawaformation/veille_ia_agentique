# Ollama — l'outil, pas les modèles

## Pourquoi une fiche à part

Le catalogue de modèles Ollama Pro a déjà été classifié (`catalogue_ollama_pro_classification.md`).
Mais Ollama est lui-même un logiciel, avec sa propre licence et son propre modèle
économique — **une question distincte de l'ouverture des modèles qu'il fait tourner.**

## Ce qu'est Ollama

- **CLI** (ligne de commande) : licence **MIT**, gratuit, sans compte requis.
- **Application desktop** (interface graphique, sortie 2025) : **statut de licence séparé**
  du CLI — à vérifier précisément avant restitution, la distinction CLI/app n'est pas
  anodine.
- **Backend** : s'appuie sur `llama.cpp` pour l'exécution des modèles.
- **Fonctionnalités** : CLI, API REST, bibliothèques Python/JS, intégrations tierces
  (éditeurs de code, frameworks d'agents, outils RAG).
- **Communauté** : ~180k stars / 17,7k forks sur GitHub — adoption large.

## Qui est derrière

- **Ollama Inc.** — startup privée (Delaware, siège Palo Alto), pas une filiale d'un grand
  acteur (Google, Meta...).
- Fondée par **Jeffrey Morgan** (CEO, ex-Docker) et **Michael Chiang**.
- Financée par capital-risque, dont **Y Combinator**.

## Modèle économique

- Le logiciel local (CLI + exécution locale) reste **gratuit et open source**.
- **Ollama Cloud** est un service payant séparé — hébergement distant pour faire tourner des
  modèles trop gros pour le matériel de l'utilisateur.
- Structure classique d'« **open core** » : le cœur du logiciel est ouvert, le service
  d'infrastructure autour est le produit commercial.
- Facturation récemment passée d'un modèle **au temps GPU** à un modèle **au token**,
  standard désormais dans l'industrie (alignement avec les API OpenAI/Anthropic/Mistral...).

### Détail des offres (relevé 2026-09-07)

| Plan | Prix | Crédits inclus | Requêtes simultanées | Accès modèles |
| --- | --- | --- | --- | --- |
| **Free** | 0 $ | Crédits de démarrage | 1 | Modèles starter seulement — « ajouter des crédits pour débloquer tous les modèles » |
| **Pro** | 20 $/mois (ou 200 $/an ≈ 16,67 $/mois) | 60 $/mois | 3 | Catalogue complet, y compris les « pro models » plus lourds |
| **Max** | 100 $/mois | 300 $/mois | 10 | Tout Pro + accès anticipé aux modèles les plus récents |
| **Team** | 500 $/mois (accès anticipé) | 1 000 $/mois partagés | 10 | Utilisateurs illimités, facturation centralisée, support prioritaire |
| **Enterprise** | Sur devis | — | — | Contrôle d'accès par modèle, budgets par utilisateur, support Slack dédié, questionnaires sécurité |

**Deux lectures possibles de cette structure de prix** :

1. **Lecture favorable** : les crédits couvrent une part significative du prix de
   l'abonnement (60 $ de crédits pour 20 $ payés en Pro) — le tarif n'est pas qu'un droit
   d'accès, il inclut de la consommation réelle.
2. **Point de vigilance** : le plan Free limite explicitement l'accès aux modèles
   « starter » — **la plupart des modèles réellement ouverts de ce catalogue (poids
   publiés, licence permissive) ne sont donc utilisables via Ollama Cloud qu'en payant**,
   alors même que leurs poids sont, eux, gratuits et téléchargeables ailleurs (Hugging
   Face). Ollama Cloud vend l'infrastructure d'exécution, pas l'accès aux poids — mais la
   frontière peut être facilement confondue par un utilisateur pressé.

## Clé pédagogique

Ollama est lui-même une bonne illustration de la distinction posée dans le document
principal de cette veille (section 4, standards ouverts vs logiciel libre) :

> **Ollama est un logiciel libre (MIT) qui sert de plateforme neutre pour exécuter des
> modèles open weight produits par d'autres (DeepSeek, Meta, Google, Mistral, Zhipu,
> Moonshot, NVIDIA, Alibaba...).** Le fait qu'un outil soit lui-même open source ne dit rien
> de l'ouverture des modèles qu'il exécute — ce sont deux questions indépendantes, même si
> Ollama, de fait, ne propose que des modèles ouverts à un degré ou un autre (cf. constat
> déjà noté : jamais de modèle Fermé/API dans son catalogue).

Le financement VC pose aussi une question ouverte, pas tranchée ici : un outil MIT financé
par capital-risque a une pression à monétiser (ici via le Cloud payant) qui peut, à terme,
influencer ce qui reste gratuit dans le CLI — point de vigilance pour une veille future,
pas un fait établi aujourd'hui.

---

## Sources

- [Ollama — Wikipedia](https://en.wikipedia.org/wiki/Ollama)
- [Who Owns Ollama? Founders, Funding, and MIT License — LegalClarity](https://legalclarity.org/who-owns-ollama-founders-funding-and-mit-license/)
- [GitHub — ollama/ollama](https://github.com/ollama/ollama)
- [Ollama Pricing — page officielle](https://ollama.com/pricing) (source primaire, détail des offres)
- [Ollama Pricing 2026 — AISO Tools](https://aisotools.com/pricing/ollama)

**Vérification faite le 2026-09-07** via WebSearch/WebFetch. Le statut de licence exact de
l'application desktop (distinct du CLI MIT) n'a pas été confirmé précisément — **à vérifier
avant restitution** si ce point est mentionné à l'oral.
