import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parent.parent
WF = ROOT / ".github" / "workflows" / "tests.yml"


class TestCiWorkflow(unittest.TestCase):
    def test_workflow(self):
        self.assertTrue(WF.exists(), "missing .github/workflows/tests.yml")
        text = WF.read_text()
        for needle in ["pull_request", "actions/checkout", "actions/setup-python",
                       "python3 -m unittest discover -s tests"]:
            with self.subTest(needle=needle):
                self.assertIn(needle, text)
