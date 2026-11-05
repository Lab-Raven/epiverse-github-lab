import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from check_pull_request import validate, LAB_REPO

class PullRequestTests(unittest.TestCase):
    def test_valid_lab_pull_request(self):
        self.assertEqual(validate("[LAB] Non officiel. Closes #1", "main", LAB_REPO), [])

    def test_missing_issue_is_rejected(self):
        self.assertIn("Aucun lien Issue dans la PR", validate("[LAB] Non officiel", "main", LAB_REPO))

    def test_reject_official_repo(self):
        self.assertIn("Workflow interdit hors du LAB", validate("[LAB] Non officiel Closes #1", "main", "epiverse-epitech/epiverse"))

    def test_empty_body(self):
        self.assertIn("Corps PR absent", validate("", "main", LAB_REPO))

    def test_dependabot_verified_automatic_update(self):
        result = validate("Bumps [actions/checkout](https://github.com/actions/checkout) from 4 to 7.",
                          "main", LAB_REPO, "dependabot[bot]",
                          "chore(deps): bump actions/checkout from 4 to 7")
        self.assertEqual(result, [])

    def test_dependabot_name_cannot_be_impersonated_by_title(self):
        result = validate("Bumps a dependency.", "main", LAB_REPO,
                          "untrusted-user", "chore(deps): bump tool from 1 to 2")
        self.assertIn("Aucun lien Issue dans la PR", result)

    def test_dependabot_still_scoped_to_lab(self):
        result = validate("Bumps a dependency.", "main", "epiverse-epitech/epiverse",
                          "dependabot[bot]", "chore(deps): bump tool from 1 to 2")
        self.assertIn("Workflow interdit hors du LAB", result)

    def test_wrong_base_is_rejected(self):
        self.assertIn("Branche cible inattendue", validate("[LAB] Refs #1", "develop", LAB_REPO))
