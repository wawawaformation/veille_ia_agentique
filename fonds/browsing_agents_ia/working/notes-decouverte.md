# Browsing pour agents IA — notes de découverte

Matériau de travail (démarré le 2026-08-02). Axe : développement IA agentique
(outillage), distinct du thème Mini Manifest — déclenché par une question de
conception concrète sur US2 (QualiCheck), pas par une lecture externe au départ.

## Point de départ

US2 (question libre, `conception/5_us2_question_libre/`) accepte une URL ou
une capture d'écran en entrée. Outils envisagés pour l'agent : Playwright
(rendu + extraction), BeautifulSoup (analyse statique du DOM), et un point
resté ouvert sur l'analyse d'image.

## Vision native vs outil séparé

Les LLM récents (GPT-4o et suivants, Claude 3+, Gemini) lisent une image
nativement — pas d'étape de captioning séparée, l'image est encodée par un
vision encoder puis injectée dans le même Transformer que le texte. Reste un
vrai travail d'intégration même sans « outil » dédié : format de message
multimodal (LangChain `HumanMessage` avec des blocs `image_url`), encodage
base64, limites de taille/résolution côté fournisseur à vérifier.

## Playwright vs Puppeteer

- **Puppeteer** : Google, natif Node.js, Chrome/Chromium d'abord (Firefox
  expérimental depuis), portage Python (`Pyppeteer`) peu maintenu.
- **Playwright** : Microsoft, par une partie de l'ancienne équipe Puppeteer —
  Chromium, Firefox et WebKit nativement, bindings officiels multi-langages
  dont Python. Avantage direct pour une stack FastAPI/Python comme QualiCheck.

## Piste retenue pour la veille : le browsing agentique

Distinction à creuser : **scraping classique** (un humain pilote Playwright
ligne à ligne, déterministe) vs **browsing agentique** (le LLM décide
lui-même où cliquer, quoi lire, quand s'arrêter). Pistes identifiées :
serveurs MCP dédiés au navigateur (Playwright MCP officiel, Browserbase...),
approches « computer use ».

## À faire

- Explorer concrètement un serveur MCP de navigateur (Playwright MCP ?).
- Comparer à l'usage « outil classique » (Playwright appelé directement par
  le code applicatif, pas par l'agent lui-même).
- Voir si `gpt-5.4` (LLM retenu pour US2, cf. `annexes/F_choix_llm.md`)
  supporte nativement le multimodal — point resté ouvert côté conception US2
  aussi.
