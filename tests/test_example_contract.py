import unittest
from pathlib import Path

ROOT = Path(__file__).parents[1]
EXAMPLE = ROOT / "examples" / "01-cli-basics"


class CloudCompareExampleContractTests(unittest.TestCase):
    def test_documentation_marks_runtime_validation_boundary(self):
        readme = (EXAMPLE / "README.md").read_text(encoding="utf-8")
        self.assertIn("does not install CloudCompare", readme)
        self.assertIn("CLOUDCOMPARE_BIN", readme)

    def test_script_checks_binary_and_nonempty_help_output(self):
        script = (EXAMPLE / "inspect-cli.sh").read_text(encoding="utf-8")
        self.assertIn('"${CLOUDCOMPARE_BIN:-CloudCompare}"', script)
        self.assertIn('"$bin" -HELP', script)
        self.assertIn('[[ ! -s "$output_path" ]]', script)
        self.assertIn("set -euo pipefail", script)
        self.assertIn("CLOUDCOMPARE_HELP_TIMEOUT_SECONDS", script)
        self.assertIn("timeout --signal=TERM --kill-after=5", script)
        self.assertIn('status -eq 124 || status -eq 137', script)


if __name__ == "__main__":
    unittest.main()
