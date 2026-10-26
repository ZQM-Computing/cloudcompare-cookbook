# Inspect the CloudCompare command-line interface

This first pattern captures CloudCompare's command-line help so an operator can confirm that the installed build exposes its CLI options before attempting batch workflows. It does not open, transform, or export a point cloud.

## Prerequisites

- CloudCompare 2.13.2 or a compatible build
- Bash (for example, Git Bash on Windows)
- CloudCompare executable available as `CloudCompare` on `PATH`, or set `CLOUDCOMPARE_BIN` to its path

## Run

```bash
bash examples/01-cli-basics/inspect-cli.sh build/cloudcompare-cli-help.txt
```

The script fails if the executable cannot be found or the help command produces an empty output file. Some Windows installations launch the GUI even when command-line options are supplied; run this from a terminal on the target host and verify the captured output before building automated pipelines on top of it.

## Validation boundary

CI tests the script contract and Bash syntax only. It does not install CloudCompare or certify command-line behavior on Windows. A fleet run against the actual 2.13.2 executable remains required.
