import sys
import unittest
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[3]
SOURCE_DIRECTORY = PROJECT_ROOT / "src" / "main" / "python"
sys.path.insert(0, str(SOURCE_DIRECTORY))


from calculator_Yehia_Afesh import (
    add,
    subtract,
    multiply,
    divide,
    modulus,
    power,
    square_root,
)


class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(-1, 1), 0)

    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(3, 5), -2)

    def test_multiply(self):
        self.assertEqual(multiply(3, 4), 12)
        self.assertEqual(multiply(5, 0), 0)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)
        self.assertAlmostEqual(divide(7, 2), 3.5)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            divide(10, 0)

    def test_modulus(self):
        self.assertEqual(modulus(10, 3), 1)
        self.assertEqual(modulus(12, 4), 0)

    def test_modulus_by_zero(self):
        with self.assertRaises(ValueError):
            modulus(10, 0)

    def test_modulus_negative_number(self):
        self.assertEqual(modulus(-10, 3), 2)

    def test_power(self):
        self.assertEqual(power(2, 3), 8)
        self.assertEqual(power(-2, 3), -8)

    def test_power_zero_exponent(self):
        self.assertEqual(power(5, 0), 1)

    def test_power_negative_exponent(self):
        self.assertAlmostEqual(power(2, -2), 0.25)

    def test_square_root(self):
        self.assertEqual(square_root(25), 5)
        self.assertEqual(square_root(81), 9)

    def test_square_root_zero(self):
        self.assertEqual(square_root(0), 0)

    def test_square_root_nonperfect_square(self):
        self.assertAlmostEqual(
            square_root(2),
            1.4142135623730951,
        )

    def test_square_root_negative_number(self):
        with self.assertRaises(ValueError):
            square_root(-9)


if __name__ == "__main__":
    unittest.main()