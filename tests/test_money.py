import unittest
from decimal import Decimal
from gym.money import format_gbp


class TestFormatGbp(unittest.TestCase):
    def test_cases(self):
        cases = [
            (1234.5, "£1,234.50"),
            (0, "£0.00"),
            (-1234.5, "-£1,234.50"),
            (2.675, "£2.68"),
            ("1000000", "£1,000,000.00"),
            (Decimal("0.005"), "£0.01"),
            (-0.001, "£0.00"),
        ]
        for amount, want in cases:
            with self.subTest(amount=amount):
                self.assertEqual(format_gbp(amount), want)
