import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

class RulesetConfigTests(unittest.TestCase):
    def test_safe_initial_ruleset(self):
        payload = json.loads((ROOT / "setup/main-ruleset.json").read_text(encoding="utf-8"))
        self.assertEqual(payload["name"], "LAB — main protected")
        self.assertEqual(payload["target"], "branch")
        self.assertEqual(payload["enforcement"], "disabled")
        self.assertEqual(payload["conditions"]["ref_name"]["include"], ["~DEFAULT_BRANCH"])
        rules = {rule["type"]: rule for rule in payload["rules"]}
        self.assertIn("deletion", rules)
        self.assertIn("non_fast_forward", rules)
        self.assertEqual(rules["pull_request"]["parameters"]["required_approving_review_count"], 0)
        contexts = {x["context"] for x in rules["required_status_checks"]["parameters"]["required_status_checks"]}
        self.assertEqual(contexts, {"validate", "policy", "scan", "secret-guard", "public-lab"})
