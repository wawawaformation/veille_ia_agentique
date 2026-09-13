---
document:
  title: "Claude Code Docs"
  page: null
  header: "Claude Code Docs"
  page_number_position: null

source:
  file: "5_code.claude.com.png"
  format: "png"

ocr:
  provider: "ollama"
  model: "glm-5.3-flash"
  prompt_tokens: 3672
  completion_tokens: 1515
  total_tokens: 5187
  finish_reason: "stop"

analysis:
  dehyphenation_applied: false
  uncertain_reading: false
  omission_suspected: false
  reconstruction_detected: false

quality:
  status: "pending"
  controller: null
  fallback_used: false
---

# Référence CLI

Référence complète pour l'interface de ligne de commande Claude Code, incluant les commandes et les drapeaux.

## Commandes CLI

Vous pouvez démarrer des sessions, traiter du contenu, reprendre des conversations et gérer les mises à jour avec ces commandes :

| Commande | Description | Exemple |
| --- | --- | --- |
| `claude` | Démarrer une session interactive | `claude` |
| `claude "query"` | Démarrer une session interactive avec une invite initiale | `claude "explain this project"` |
| `claude -p "query"` | Interroger via SDK, puis quitter | `claude -p "explain this function"` |
| `cat file \| claude -p "query"` | Traiter le contenu canalisé | `cat logs.txt \| claude -p "explain"` |
| `claude -c` | Continuer la conversation la plus récente dans le répertoire courant | `claude -c` |
| `claude -c -p "query"` | Continuer via SDK | `claude -c -p "Check for type errors"` |
| `claude -r "<session>" "query"` | Reprendre une session par ID ou nom | `claude -r "auth-refactor" "Finish this PR"` |
| `claude update` | Mettre à jour vers la dernière version | `claude update` |
| `claude gateway` | Démarrer le serveur **passerelle d'applications Claude** auto-hébergé, pour les administrateurs déployant SSO et la politique devenant Claude Code sur Amazon Bedrock, Google Cloud's Agent Platform, ou Microsoft Foundry. Nécessite `--config` pointant vers un `gateway.yaml`. Disponible dans Claude Code v2.1.195 et ultérieur. | `claude gateway --config gateway.yaml` |
| `claude install [version]` | Installer ou réinstaller le binaire natif. Accepte une version comme `2.1.118`, ou `stable` ou `latest`. Voir [Installer une version spécifique](#) | `claude install stable` |
| `claude auth login` | Se connecter à votre compte Anthropic. Utilisez `--email` pour pré-remplir votre adresse e-mail, `--sso` pour forcer l'authentification SSO, et `--console` pour vous connecter avec Anthropic Console pour la facturation de l'utilisation de l'API au lieu d'un abonnement Claude | `claude auth login --console` |
| `claude auth logout` | Se déconnecter de votre compte Anthropic | `claude auth logout` |
| `claude auth status` | Afficher l'état d'authentification en JSON. Utilisez `--text` pour une sortie lisible par l'homme. Quitte avec le code 0 si connecté, 1 sinon | `claude auth status` |
