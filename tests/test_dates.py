import unittest
from datetime import date
from gym.dates import parse_uk_date


class TestParseUkDate(unittest.TestCase):
    def test_day_first(self):
        self.assertEqual(parse_uk_date("22/11/2026"), date(2026, 11, 22))

    def test_single_digits(self):
        self.assertEqual(parse_uk_date("1/2/2026"), date(2026, 2, 1))

    def test_whitespace(self):
        self.assertEqual(parse_uk_date("  05/03/2026 \n"), date(2026, 3, 5))

    def test_bad(self):
        for bad in ["2026-11-22", "31/02/2026", "", "aa/bb/cccc", "1/2/3/4"]:
            with self.subTest(bad=bad), self.assertRaises(ValueError):
                parse_uk_date(bad)
