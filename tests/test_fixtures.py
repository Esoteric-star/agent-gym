import itertools
import unittest
from gym.fixtures import round_robin


class TestRoundRobin(unittest.TestCase):
    def check(self, n):
        teams = [f"T{i}" for i in range(n)]
        rounds = round_robin(teams)
        self.assertEqual(len(rounds), n - 1 if n % 2 == 0 else n, f"rounds for n={n}")
        seen = []
        for r in rounds:
            in_round = [x for pair in r for x in pair]
            self.assertEqual(len(in_round), len(set(in_round)), f"team twice in a round, n={n}")
            self.assertEqual(len(r), n // 2)
            seen += [frozenset(p) for p in r]
        want = {frozenset(p) for p in itertools.combinations(teams, 2)}
        self.assertEqual(len(seen), len(want), f"pair count n={n}")
        self.assertEqual(set(seen), want, f"pairs n={n}")

    def test_sizes(self):
        for n in range(2, 12):
            with self.subTest(n=n):
                self.check(n)

    def test_small(self):
        self.assertEqual(round_robin([]), [])
        self.assertEqual(round_robin(["A"]), [])
        self.assertEqual(round_robin(["A", "B"]), [[("A", "B")]])
