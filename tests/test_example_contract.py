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


    def test_readme_pattern_table_has_consistent_columns(self):
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        section = readme.split("## Patterns", 1)[1].split("## Repository layout", 1)[0]
        rows = [line for line in section.splitlines() if line.startswith("|")]
        self.assertEqual(len(rows), 6)
        self.assertTrue(all(len(row.strip("|").split("|")) == 4 for row in rows))

if __name__ == "__main__":
    unittest.main()
