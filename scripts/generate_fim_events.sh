#!/usr/bin/env bash
# Benign FIM simulation in a dedicated directory, on an authorized test VM.
set -euo pipefail
TEST_DIR="${HOME}/soc-fim-test"
mkdir -p "$TEST_DIR"
FILE="$TEST_DIR/soc-lab-$(date +%s)-$$.txt"
printf 'SOC Level 1 harmless FIM test\n' > "$FILE"
printf 'Harmless modification\n' >> "$FILE"
sha256sum "$FILE"
RENAMED="${FILE%.txt}-renamed.txt"
mv -- "$FILE" "$RENAMED"
rm -- "$RENAMED"
echo "Created, edited, renamed and removed harmless test file in $TEST_DIR"
echo "Confirm real Wazuh telemetry before claiming detection."
