"""Standard library tests: simulation must never perform response actions."""
import importlib.util
from pathlib import Path
import unittest

source = Path(__file__).resolve().parents[1] / "scripts" / "simulate_response.py"
spec = importlib.util.spec_from_file_location("safe_demo", source)
demo = importlib.util.module_from_spec(spec)
spec.loader.exec_module(demo)

class TestDecisions(unittest.TestCase):
    def test_benign(self):
        result = demo.decide({"approved_lab_test": True, "rule": {"level": 12}})
        self.assertEqual(result["recommended_action"], "document_approved_benign_test")
        self.assertEqual(result["action_performed"], "none")

    def test_escalate(self):
        self.assertEqual(demo.decide({"rule": {"level": 12}})["recommended_action"],
                         "escalate_for_human_review")

    def test_review(self):
        self.assertEqual(demo.decide({"rule": {"level": 3}})["recommended_action"],
                         "investigate_and_document")

    def test_input_validation(self):
        with self.assertRaises(TypeError):
            demo.decide([])

if __name__ == "__main__":
    unittest.main()
