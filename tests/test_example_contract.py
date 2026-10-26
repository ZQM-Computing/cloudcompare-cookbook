import unittest
from pathlib import Path

ROOT = Path(__file__).parents[1]
EXAMPLE = ROOT / "examples" / "01-cli-basics"


class CloudCompareExampleContractTests(unittest.TestCase):
    def test_documentation_marks_runtime_validation_boundary(self):
        readme = (EXAMPLE / "README.md").read_text(encoding="utf-8")
        self.assertIn("does not install CloudCompare", readme)
        self.assertIn("CLOUDCOMPARE_BIN", readme)

    def test_readme_pattern_inventory_has_unique_numbers_and_no_duplicate_rows(self):
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        table_lines = [
            line for line in readme.splitlines()
            if line.startswith("| ") and line.count("|") >= 4
            and line.split("|")[1].strip().isdigit()
        ]
        numbers = [line.split("|")[1].strip() for line in table_lines]
        self.assertEqual(len(numbers), len(set(numbers)))
        self.assertEqual(len(table_lines), 4)
        self.assertEqual(sum("01-cli-basics" in line for line in table_lines), 1)
        self.assertEqual(sum("02-registration" in line for line in table_lines), 1)
        self.assertEqual(sum("03-cloud-to-cloud" in line for line in table_lines), 1)
        self.assertEqual(sum("04-rasterize" in line for line in table_lines), 1)

    def test_pattern_table_has_consistent_four_column_shape(self):
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        section = readme.split("## Patterns", 1)[1].split("## Repository layout", 1)[0]
        rows = [line for line in section.splitlines() if line.startswith("|")]
        self.assertEqual(len(rows), 6)  # header, separator, and four pattern rows
        for row in rows:
            self.assertEqual(len(row.strip("|").split("|")), 4, row)

    def test_script_checks_binary_and_nonempty_help_output(self):
        script = (EXAMPLE / "inspect-cli.sh").read_text(encoding="utf-8")
        self.assertIn('"${CLOUDCOMPARE_BIN:-CloudCompare}"', script)
        self.assertIn('"$bin" -HELP', script)
        self.assertIn('[[ ! -s "$output_path" ]]', script)
        self.assertIn("set -euo pipefail", script)
        self.assertIn("CLOUDCOMPARE_HELP_TIMEOUT_SECONDS", script)
        self.assertIn("timeout --signal=TERM --kill-after=5", script)
        self.assertIn('"$status" -eq 124 || "$status" -eq 137', script)


if __name__ == "__main__":
    unittest.main()
