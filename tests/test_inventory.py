import unittest
from gym.inventory import Inventory


class TestInventory(unittest.TestCase):
    def setUp(self):
        self.inv = Inventory()
        self.inv.add("ABC", 5)

    def test_add_remove(self):
        self.inv.remove("ABC", 2)
        self.assertEqual(self.inv.count("ABC"), 3)

    def test_unknown_sku(self):
        with self.assertRaises(KeyError):
            self.inv.remove("ZZZ", 1)

    def test_insufficient_stock_unchanged(self):
        with self.assertRaises(ValueError):
            self.inv.remove("ABC", 6)
        self.assertEqual(self.inv.count("ABC"), 5)

    def test_non_positive_qty(self):
        for qty in (0, -1):
            with self.subTest(qty=qty):
                with self.assertRaises(ValueError):
                    self.inv.add("ABC", qty)
                with self.assertRaises(ValueError):
                    self.inv.remove("ABC", qty)
        self.assertEqual(self.inv.count("ABC"), 5)

    def test_remove_to_zero_drops_sku(self):
        self.inv.remove("ABC", 5)
        self.assertEqual(self.inv.count("ABC"), 0)
        self.assertNotIn("ABC", self.inv.skus())
