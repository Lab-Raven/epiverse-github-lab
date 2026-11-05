import sys
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from public_lab_guard import check, SENSITIVE_PATH, SECRET_PATTERNS

class PublicLabGuardTests(unittest.TestCase):
    def test_path_detection(self):
        self.assertIsNotNone(SENSITIVE_PATH.search(".env.production"))
        self.assertIsNotNone(SENSITIVE_PATH.search("keys/id_ed25519"))
        self.assertIsNone(SENSITIVE_PATH.search(".env.example"))
    def test_safe_text(self):
        self.assertTrue(all(x.search("Exemple fictif sans jeton") is None for x in SECRET_PATTERNS))
    def test_public_classification(self):
        self.assertEqual(check([]), [])
