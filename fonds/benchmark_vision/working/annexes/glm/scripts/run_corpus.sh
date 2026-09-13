#!/usr/bin/env bash

set -u

CORPUS="${1:-}"

if [[ -z "$CORPUS" ]]; then
    echo "Usage : $0 <corpus>"
    echo "Exemple : $0 cuisine"
    exit 1
fi

SOURCE_DIR="sources/$CORPUS"
OUTPUT_DIR="output/$CORPUS"
LOG_DIR="logs/$CORPUS"

if [[ ! -d "$SOURCE_DIR" ]]; then
    echo "Erreur : dossier introuvable : $SOURCE_DIR"
    exit 1
fi

mkdir -p "$OUTPUT_DIR" "$LOG_DIR"

shopt -s nullglob
images=("$SOURCE_DIR"/*.png)

if (( ${#images[@]} == 0 )); then
    echo "Erreur : aucune image PNG dans $SOURCE_DIR"
    exit 1
fi

echo "Corpus : $CORPUS"
echo "Images : ${#images[@]}"
echo "Output : $OUTPUT_DIR"
echo "Logs   : $LOG_DIR"
echo

success=0
errors=0

for image in "${images[@]}"; do
    echo "============================================================"
    echo "Traitement : $image"
    echo "============================================================"

    if uv run python test_glm_vision.py "$image" \
        --output "$OUTPUT_DIR" \
        --logs "$LOG_DIR"
    then
        ((success++))
    else
        echo "ERREUR : $image" >&2
        ((errors++))
    fi

    echo
done

echo "============================================================"
echo "TERMINÉ"
echo "============================================================"
echo "Succès  : $success"
echo "Erreurs : $errors"

if (( errors > 0 )); then
    exit 1
fi
