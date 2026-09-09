# Bloc 4 — Ollama, conclusion et twist final

**Durée cible** : 1:25 (réparti : Ollama ~20s / conclusion générale ~30s / twist final ~40s)

*Ce bloc ne parle pas que d'Ollama : il porte aussi la conclusion générale de
toute la veille et le twist RGPD/Infomaniak. Voir `plan_slides.md` slides 19-21
pour le détail slide par slide et les visuels associés.*

---

## Partie 1 — Ollama : illustration concrète

### Constat

Ollama Cloud = catalogue exclusivement open weight + open source (zéro modèle Fermé/API).

**Trois façons d'utiliser** : local gratuit (CLI MIT) / API gratuite limitée / Cloud Pro 20 $/mois (60 $ crédits/mois).

### Exemples de modèles

- **Gemma 4** — petit, efficace
- **Llama 405B** — flagship open weight
- **OLMo** — open source pur
- **Llama 3.2 Vision** — spécialisé OCR

*Note : certains modèles ont tarifs différents selon l'heure.*

### Point clé

La plateforme Ollama est elle-même MIT. Monétisation = infrastructure cloud, pas les modèles.

Illustration concrète : l'ouverture du continuum n'est pas théorique, c'est déjà en production.

---

## Partie 2 — Conclusion générale : la réponse simple

**Mistral est-il vraiment open source ?**

Réponse directe : Non. Mistral est **open weight**. Pour être open source, il
faudrait aussi publier les données et la recette d'entraînement.

Implication technique : « Open source » n'est pas une case qu'on coche. C'est
un **continuum**, et c'est un **choix**.

---

## Partie 3 — Twist final : le vrai dilemme

**Titre** : Mais attends…

- Tu dis « Je vais utiliser Ollama Cloud, c'est open source donc indépendant ! »
- **Réalité** : Infrastructure USA (transfert de données hors UE, article 44 RGPD)
- **Alternative** : Infomaniak (Suisse) — RGPD conforme (adéquation UE), mais
  catalogue plus restreint (8 modèles, dont **Apertus** — l'open source suisse
  déjà cité en bloc 2)
- **Le vrai dilemme** : large choix (Ollama) OU souveraineté (Infomaniak) —
  rarement les deux à la fois

**Ton oral** : léger, ironique, pas cynique. Genre « Eh merde… »

**Point clé** : « Indépendance technique ≠ indépendance réelle. Il faut
regarder l'infrastructure aussi. »
