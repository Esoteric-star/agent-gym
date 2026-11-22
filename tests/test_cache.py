import unittest
from gym.cache import TTLCache


class Clock:
    def __init__(self):
        self.t = 0.0

    def __call__(self):
        return self.t


class TestTTLCache(unittest.TestCase):
    def setUp(self):
        self.clock = Clock()
        self.c = TTLCache(2, 10, clock=self.clock)

    def test_validation(self):
        for args in [(0, 1), (1, 0), (-1, 5), (2, -1)]:
            with self.subTest(args=args), self.assertRaises(ValueError):
                TTLCache(*args, clock=self.clock)

    def test_get_set(self):
        self.c.set("a", 1)
        self.assertEqual(self.c.get("a"), 1)
        self.assertIsNone(self.c.get("zz"))
        self.assertEqual(self.c.get("zz", 5), 5)
        self.c.set("a", 2)
        self.assertEqual(self.c.get("a"), 2)
        self.assertEqual(len(self.c), 1)

    def test_expiry_boundary(self):
        self.c.set("a", 1)
        self.clock.t = 9.999
        self.assertIn("a", self.c)
        self.clock.t = 10
        self.assertNotIn("a", self.c)
        self.assertIsNone(self.c.get("a"))
        self.assertEqual(len(self.c), 0)

    def test_get_does_not_extend_ttl(self):
        self.c.set("a", 1)
        self.clock.t = 8
        self.c.get("a")
        self.clock.t = 10
        self.assertIsNone(self.c.get("a"))

    def test_set_resets_ttl(self):
        self.c.set("a", 1)
        self.clock.t = 8
        self.c.set("a", 1)
        self.clock.t = 15
        self.assertEqual(self.c.get("a"), 1)

    def test_lru_eviction_respects_get(self):
        self.c.set("a", 1)
        self.c.set("b", 2)
        self.c.get("a")          # a is now most recent
        self.c.set("c", 3)       # evicts b
        self.assertIn("a", self.c)
        self.assertNotIn("b", self.c)
        self.assertIn("c", self.c)

    def test_contains_does_not_touch_recency(self):
        self.c.set("a", 1)
        self.c.set("b", 2)
        self.assertIn("a", self.c)
        self.c.set("c", 3)       # a still least recent -> evicted
        self.assertNotIn("a", self.c)

    def test_expired_dropped_before_lru(self):
        self.c.set("a", 1)       # expires at 10
        self.clock.t = 5
        self.c.set("b", 2)       # expires at 15
        self.c.get("a")          # a most recent but will be expired
        self.clock.t = 11
        self.c.set("c", 3)       # a expired -> dropped; b must survive
        self.assertIn("b", self.c)
        self.assertIn("c", self.c)
        self.assertEqual(len(self.c), 2)
