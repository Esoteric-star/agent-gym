import io
import os
import tempfile
import unittest
from contextlib import redirect_stdout
from gym import cli
from gym.league import build_table

RESULTS = [
    ("A", 1, 0, "B"), ("C", 2, 2, "A"), ("A", 0, 3, "D"), ("B", 1, 1, "C"),
    ("A", 2, 1, "C"), ("D", 0, 1, "A"), ("A", 4, 0, "B"),
]


class TestForm(unittest.TestCase):
    def test_form_last_five_most_recent_last(self):
        t = {r["team"]: r for r in build_table(RESULTS)}
        self.assertEqual(t["A"]["form"], "DLWWW")   # 6 games: W D L W W W -> last 5
        self.assertEqual(t["B"]["form"], "LDL")
        self.assertEqual(t["C"]["form"], "DDL")
        self.assertEqual(t["D"]["form"], "WL")

    def test_existing_keys_unchanged(self):
        row = build_table(RESULTS)[0]
        for k in ["team", "played", "won", "drawn", "lost", "gf", "ga", "gd", "points"]:
            self.assertIn(k, row)

    def test_cli_shows_form_column(self):
        fd, path = tempfile.mkstemp(suffix=".csv")
        with os.fdopen(fd, "w") as f:
            f.write("home,home_goals,away_goals,away\n")
            for h, hg, ag, a in RESULTS:
                f.write(f"{h},{hg},{ag},{a}\n")
        try:
            buf = io.StringIO()
            with redirect_stdout(buf):
                cli.main(["table", path])
            lines = buf.getvalue().splitlines()
        finally:
            os.unlink(path)
        self.assertIn("Form", lines[0])
        a_line = next(l for l in lines[1:] if " A " in l)
        self.assertTrue(a_line.rstrip().endswith("DLWWW"), a_line)
