#!/usr/bin/env bash
set -euo pipefail

output_path="${1:-build/cloudcompare-cli-help.txt}"
bin="${CLOUDCOMPARE_BIN:-CloudCompare}"
timeout_seconds="${CLOUDCOMPARE_HELP_TIMEOUT_SECONDS:-30}"

if ! command -v "$bin" >/dev/null 2>&1 && [[ ! -x "$bin" ]]; then
  echo "ERROR: CloudCompare executable not found: $bin" >&2
  echo "Set CLOUDCOMPARE_BIN or add CloudCompare to PATH." >&2
  exit 127
fi
if ! [[ "$timeout_seconds" =~ ^[1-9][0-9]*$ ]]; then
  echo "ERROR: CLOUDCOMPARE_HELP_TIMEOUT_SECONDS must be a positive integer" >&2
  exit 2
fi
if ! command -v timeout >/dev/null 2>&1; then
  echo "ERROR: GNU timeout is required to bound CloudCompare CLI startup" >&2
  exit 127
fi

mkdir -p "$(dirname "$output_path")"
# Some builds return non-zero for help. Preserve output and validate it below,
# but bound execution so a GUI/session startup cannot hang automation.
set +e
timeout --signal=TERM --kill-after=5 "$timeout_seconds" "$bin" -HELP >"$output_path" 2>&1
status=$?
set -e

if [[ "$status" -eq 124 || "$status" -eq 137 ]]; then
  echo "ERROR: CloudCompare CLI help exceeded ${timeout_seconds}s timeout" >&2
  exit 124
fi
if [[ ! -s "$output_path" ]]; then
  echo "ERROR: CloudCompare produced no CLI help output (exit $status)" >&2
  exit 1
fi
printf 'Captured CloudCompare CLI output to %s (exit status %s)
' "$output_path" "$status"
