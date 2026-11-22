import time
import unittest
from gym.stats import moving_average


class TestMovingAverageScale(unittest.TestCase):
    def test_accepts_generator(self):
        self.assertEqual(moving_average((x for x in [1, 2, 3, 4]), 2), [1.5, 2.5, 3.5])

    def test_generator_bad_window(self):
        with self.assertRaises(ValueError):
            moving_average((x for x in [1, 2]), 3)

    def test_linear_time(self):
        values = list(range(300_000))
        start = time.perf_counter()
        out = moving_average(values, 3_000)
        elapsed = time.perf_counter() - start
        self.assertEqual(len(out), 297_001)
        self.assertAlmostEqual(out[0], 1499.5)
        self.assertAlmostEqual(out[-1], 298499.5)
        self.assertLess(elapsed, 2.0, f"took {elapsed:.2f}s; must be O(n), not O(n*window)")
