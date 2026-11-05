import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from check_pull_request import validate

class PullRequestTests(unittest.TestCase):
    def test_valid(self):
        self.assertEqual(validate("[LAB] Non officiel. Closes #1", "main", "estellegiroud/epiverse-github-lab"), [])

    def test_missing_issue(self):
        self.assertIn("Aucun lien Issue dans la PR", validate("[LAB] Non officiel", "main", "estellegiroud/epiverse-github-lab"))

    def test_reject_official_repo(self):
        self.assertIn("Workflow interdit hors du LAB", validate("[LAB] Non officiel Closes #1", "main", "epiverse-epitech/epiverse"))

    def test_empty(self):
        self.assertIn("Corps PR absent", validate("", "main", "estellegiroud/epiverse-github-lab"))
