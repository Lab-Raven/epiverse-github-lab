import json
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from generate_report import LAB_REPO, build_report
from verify_lab import check

class LabTests(unittest.TestCase):
    def test_repo_pinned_to_personal_lab(self):
        self.assertEqual(LAB_REPO, "estellegiroud/epiverse-github-lab")

    def test_no_missing_files_or_secrets(self):
        missing, leaked, warnings = check()
        self.assertEqual((missing, leaked, warnings), ([], [], []))

    def test_demo_report_explicitly_fictitious(self):
        data = json.loads((ROOT / "data/demo_issues.json").read_text(encoding="utf-8"))
        result = build_report(data["issues"], data["pulls"], demo=True)
        self.assertIn("DONNÉES FICTIVES", result)
        self.assertIn("Issues ouvertes | 2", result)
        self.assertIn("PR fusionnées | 1", result)

    def test_no_project_metrics_in_sample(self):
        data = json.loads((ROOT / "data/demo_issues.json").read_text(encoding="utf-8"))
        report = build_report(data["issues"], data["pulls"], demo=True)
        self.assertNotIn("taux de réalisation EpiVerse", report.lower())

if __name__ == "__main__":
    unittest.main()
