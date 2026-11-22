import unittest
from gym.textutil import slugify


class TestSlugify(unittest.TestCase):
    def test_cases(self):
        cases = {
            "Hello World": "hello-world",
            "  Leeds United -- 2026! ": "leeds-united-2026",
            "Café Crème": "cafe-creme",
            "already-a-slug": "already-a-slug",
            "!!!": "",
            "": "",
            "A_B.C": "a-b-c",
        }
        for text, want in cases.items():
            with self.subTest(text=text):
                self.assertEqual(slugify(text), want)
