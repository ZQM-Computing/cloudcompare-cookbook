#!/usr/bin/env bash
set -euo pipefail

output_path="${1:-build/cloudcompare-cli-help.txt}"
bin="${CLOUDCOMPARE_BIN:-CloudCompare}"
if ! command -v "$bin" >/dev/null 2>&1 && [[ ! -x "$bin" ]]; then
  echo "ERROR: CloudCompare executable not found: $bin" >&2
  echo "Set CLOUDCOMPARE_BIN or add CloudCompare to PATH." >&2
  exit 127
fi

mkdir -p "$(dirname "$output_path")"
# CloudCompare builds may return a non-zero status for help; validate the output.
if ! "$bin" -HELP >"$output_path" 2>&1; then
  :
fi
if [[ ! -s "$output_path" ]]; then
  echo "ERROR: CloudCompare produced no CLI help output" >&2
  exit 1
fi
printf 'Captured CloudCompare CLI output to %s\n' "$output_path"
