# Checklist images — Veille Mistral est-il vraiment open source ?

Basé sur `plan_slides.md`. Deux types : **photos** (banque d'images / captures) et **schémas** (à produire en drawio, cf. `~/.claude/skills/schemas-drawio/`).

---

## Photos à récupérer

- [x] **Slide 1** — `photos/slide1.jpg` — chat + Pinocchio (image générée par IA, Gemini), le nez allongé fait écho au « vraiment » du titre
- [x] **Slide 4** — `photos/slide4_recette.jpg` — carnet manuscrit ouvert
- [x] **Slide 5** — `photos/slide5_usb_patchwork.jpg` — grille 2×2 : sigle USB stylisé + souris filaire + manettes filaires + disque dur externe (clipart), titre « Universal Serial Bus » en haut (montre l'interopérabilité : appareils différents, même standard)
- [x] **Slide 8 (gauche)** — `photos/slide8_ingredients.jpg` (farine+œuf) + `photos/slide8_gateau_fini.jpg` (gâteau fini)
- [x] **Slide 9** — `photos/slide9_gateau_emballe.jpg` (brioche tressée) + réutilise `slide8_gateau_fini.jpg` côté ouvert
- [x] **Slide 11** — `photos/slide11_eau_trouble.jpg` + `photos/slide11_eau_claire.jpg`
- [x] **Slide 12** — `photos/slide12_ferme.jpg` — panneau CLOSED
- [x] **Slide 16** — `photos/slide16_piscine_privee.jpg` + `photos/slide16_piscine_publique.jpg`
- [ ] **Slide 19** — Capture d'écran interface Ollama (catalogue + 3 modes d'accès) — à faire par David lui-même (abonnement Pro)

Crédits détaillés : voir `photos/credits.md`.

---

## Schémas à produire (drawio)

- [x] **Slide 7** — `slide7_code_vs_composantes.drawio` — Comparatif code Python vs 3 boîtes séparées, contrôlé visuellement
- [x] **Slide 8 (droite)** — `slide8_gateau_composantes.drawio` — 3 boîtes labellisées Poids/Recette/Données, contrôlé visuellement
- [x] **Slide 10** — `slide10_continuum_gradient.drawio` — Gradient 4 zones, Mistral positionné, contrôlé visuellement
- [x] **Slide 14 (droite)** — `slide14_venn_definitions.drawio` — Venn 3 cercles partiellement chevauchés, contrôlé visuellement
- [x] **Slide 15** — `slide15_seuil_flops.drawio` — Jauge seuil FLOPs, Llama-3 405B au-dessus, contrôlé visuellement
- [x] **Slide 17** — `slide17_seuil_gpu.drawio` — Jauge 85 % GPU, bascule cloud/local, contrôlé visuellement
- [x] **Slide 20** — Réutilise `slide10_continuum_gradient.drawio` (pas de fichier séparé)
- [x] **Slide 21** — `slide21_carte_rgpd.drawio` — Carte UE→USA, alerte RGPD, contrôlé visuellement

---

## Slides sans visuel (rappel, rien à faire)

Slides 2, 3, 6, 13, 18, 22 — transitions et synthèses orales, texte seul.

---

## Notes de production

- **Photos** : privilégier des sources libres de droits (Unsplash, Pexels) ou prises perso si plus simple/rapide.
- **Schémas** : cohérence visuelle entre eux (mêmes couleurs, même police) — surtout slides 7, 8, 10/20 qui se répondent dans le même bloc.
- **Slide 10 et 20 partagent le même schéma** — le produire une seule fois, le réutiliser.
- Format des schémas : voir convention `X_reel.drawio` si applicable, sinon nommage libre dans ce dossier `images/`.
