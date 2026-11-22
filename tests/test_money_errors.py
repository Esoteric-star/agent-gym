import unittest
from decimal import Decimal
from gym.money import format_gbp


class TestFormatGbpErrors(unittest.TestCase):
    def test_nan_string(self):
        with self.assertRaises(ValueError) as cm:
            format_gbp("nan")
        self.assertIn("Invalid amount", str(cm.exception))

    def test_infinity_string(self):
        with self.assertRaises(ValueError) as cm:
            format_gbp("infinity")
        self.assertIn("Invalid amount", str(cm.exception))

    def test_negative_infinity_string(self):
        with self.assertRaises(ValueError) as cm:
            format_gbp("-infinity")
        self.assertIn("Invalid amount", str(cm.exception))

    def test_non_numeric_string(self):
        with self.assertRaises(ValueError) as cm:
            format_gbp("non-numeric")
        self.assertIn("Invalid amount", str(cm.exception))

    def test_empty_string(self):
        with self.assertRaises(ValueError) as cm:
            format_gbp("")
        self.assertIn("Invalid amount", str(cm.exception))

    def test_nan_float(self):
        with self.assertRaises(ValueError) as cm:
            format_gbp(float("nan"))
        self.assertIn("Invalid amount", str(cm.exception))

    def test_infinity_float(self):
        with self.assertRaises(ValueError) as cm:
            format_gbp(float("inf"))
        self.assertIn("Invalid amount", str(cm.exception))

    def test_negative_infinity_float(self):
        with self.assertRaises(ValueError) as cm:
            format_gbp(float("-inf"))
        self.assertIn("Invalid amount", str(cm.exception))

    def test_decimal_nan(self):
        with self.assertRaises(ValueError) as cm:
            format_gbp(Decimal("nan"))
        self.assertIn("Invalid amount", str(cm.exception))

    def test_decimal_infinity(self):
        with self.assertRaises(ValueError) as cm:
            format_gbp(Decimal("infinity"))
        self.assertIn("Invalid amount", str(cm.exception))


if __name__ == "__main__":
    unittest.main()
