import unittest
from gym.league import build_table


class TestLeague(unittest.TestCase):
    def test_counts(self):
        t = {r["team"]: r for r in build_table([("A", 2, 1, "B"), ("B", 0, 0, "C")])}
        self.assertEqual(t["A"]["points"], 3)
        self.assertEqual(t["B"]["played"], 2)
        self.assertEqual(t["C"]["drawn"], 1)

    def test_tiebreakers(self):
        results = [
            ("Alpha", 3, 0, "Delta"),   # Alpha 3pts gd+3 gf3
            ("Bravo", 1, 0, "Delta"),   # Bravo 3pts gd+1 gf1
            ("Charlie", 3, 2, "Delta"), # Charlie 3pts gd+1 gf3
            ("Echo", 3, 2, "Delta"),    # Echo 3pts gd+1 gf3 -> name after Charlie
        ]
        order = [r["team"] for r in build_table(results)]
        self.assertEqual(order, ["Alpha", "Charlie", "Echo", "Bravo", "Delta"])
