import sys
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from security_guard import BAD_FILE, PATTERNS

class SecurityGuardTests(unittest.TestCase):
    def test_sensitive_paths(self):
        self.assertIsNotNone(BAD_FILE.search(".env.production"))
        self.assertIsNotNone(BAD_FILE.search("keys/id_ed25519"))
        self.assertIsNone(BAD_FILE.search(".env.example"))

    def test_private_key_marker_detected(self):
        marker = ("-" * 5) + "BEGIN PRIVATE KEY" + ("-" * 5)
        self.assertIsNotNone(PATTERNS[2].search(marker))

    def test_normal_text_ok(self):
        self.assertTrue(all(x.search("Ce texte ne contient pas de secret") is None for x in PATTERNS))
