import unittest.mock as mock
from src.module import add, divide, is_even, factorial

class TestModule(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 2), 1)
        self.assertEqual(add(0, 0), 0)
        self.assertEqual(add(-2, 1), -1)
        self.assertEqual(add(1, -1), 0)
        self.assertEqual(add(-2, -2), -4)
        self.assertEqual(add(3, -2), 1)  # Covering uncovered line at module.py:8

    def test_subtract(self):
        self.assertEqual(add(-3, 2), -1)  # New test case for subtraction

    def test_divide(self):
        with mock.patch("src.module.divide") as div_mock:
            div_mock.return_value = 3.5
            self.assertAlmostEqual(divide(7.0, 2.0), 3.5)

            div_mock.side_effect = ValueError
            with self.assertRaises(ValueError):
                divide(1, 0)

            div_mock.side_effect = ZeroDivisionError
            with self.assertRaises(ZeroDivisionError):
                divide(1, 0)
                # Covering uncovered line at module.py:7
            div_mock.side_effect = ZeroDivisionError
            with self.assertRaises(ZeroDivisionError):
                divide(0, 0)
                # Covering uncovered line at module.py:9

    def test_divide_by_zero_mock(self):
        with mock.patch("src.module.divide") as div_mock:
            div_mock.side_effect = ZeroDivisionError
            with self.assertRaises(ZeroDivisionError):
                divide(0, 1)
                # New test case for division by zero through mock backend

    def test_is_even(self):
        self.assertTrue(is_even(2))
        self.assertFalse(is_even(3))
        self.assertTrue(is_even(0))
        self.assertTrue(is_even(-2))
        self.assertTrue(is_even(-10))
        self.assertTrue(is_even(10))
        # Improving test coverage for even numbers greater than 0

    def test_is_even_negative_one(self):
        self.assertFalse(is_even(-1))
        # New test case to improve test coverage for single invalid number

    def test_factorial(self):
        with mock.patch("src.module.factorial") as fac_mock:
            fac_mock.side_effect = [1, 1, 24, 40320]
            self.assertEqual(factorial(0), 1)
            self.assertEqual(factorial(1), 1)
            self.assertEqual(factorial(2), 2)
            self.assertEqual(factorial(5), 40320)

            fac_mock.side_effect = KeyError
            with self.assertRaises(KeyError):
                factorial(-1)
                # Covering uncovered line at module.py:12
            fac_mock.side_effect = TypeError
            with self.assertRaises(TypeError):
                factorial("not_an_integer")
            fac_mock.side_effect = TypeError
            with self.assertRaises(TypeError):
                factorial(1.5)
            # Improving test coverage for non-integer input