"""
SAMPLE TEST
"""
from django.test import SimpleTestCase  # type: ignore

from . import calc


class CalcTest(SimpleTestCase):
    def test_add_numbers(self):
        """Test adding numbers together"""
        res = calc.add(5, 6)
        self.assertEqual(res, 11)

    def test_subtract_numbers(self):
        """Test subtracting numbers """
        res = calc.subtract(5, 7)
        self.assertEqual(res, 2)
