import io
import os
import tempfile
import unittest
from contextlib import redirect_stdout
from gym import cli

CSV = "home,home_goals,away_goals,away\nA,2,0,B\nC,1,1,D\nB,3,0,D\n"


class TestCli(unittest.TestCase):
    def setUp(self):
        fd, self.path = tempfile.mkstemp(suffix=".csv")
        with os.fdopen(fd, "w") as f:
            f.write(CSV)

    def tearDown(self):
        os.unlink(self.path)

    def run_cli(self, *args):
        buf = io.StringIO()
        with redirect_stdout(buf):
            code = cli.main(["table", self.path, *args])
        return code, buf.getvalue().strip().splitlines()

    def test_full_table(self):
        code, lines = self.run_cli()
        self.assertEqual(code, 0)
        self.assertEqual(len(lines), 5)  # header + 4 teams

    def test_top(self):
        code, lines = self.run_cli("--top", "2")
        self.assertEqual(code, 0)
        self.assertEqual(len(lines), 3)
        self.assertIn("A", lines[1])

    def test_top_must_be_positive(self):
        with self.assertRaises(SystemExit) as cm, redirect_stdout(io.StringIO()):
            import contextlib
            with contextlib.redirect_stderr(io.StringIO()):
                cli.main(["table", self.path, "--top", "0"])
        self.assertEqual(cm.exception.code, 2)
