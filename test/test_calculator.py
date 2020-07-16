import unittest
from example_pkg_kh.calculator import Calculator
class TestCalculator(unittest.TestCase):
    def test_returns_0_for_empty_arguments(self):
        calc = Calculator()
        self.assertEqual(0, calc.sum())
    def test_returns_sum(self):
        calc = Calculator()
        self.assertEqual(3, calc.sum(1, 2))
