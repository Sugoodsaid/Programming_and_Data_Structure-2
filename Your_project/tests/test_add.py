import unittest
from add import add_integer

class TestAddInteger(unittest.TestCase):
    def test_addition_integers(self):
        self.assertEqual(add_integer(2, 3), 5)

    def test_addition_floats(self):
        self.assertEqual(add_integer(2.5, 3.5), 6)

    def test_addition_integer_and_float(self):
        self.assertEqual(add_integer(2, 3.5), 5)

    def test_addition_negative_integers(self):
        self.assertEqual(add_integer(-2, -3), -5)

    def test_addition_negative_floats(self):
        self.assertEqual(add_integer(-2.5, -3.5), -6)

    def test_addition_integer_and_negative_float(self):
        self.assertEqual(add_integer(2, -3.5), -1.5)

    def test_type_error_with_string(self):
        with self.assertRaises(TypeError):
            add_integer(2, "3")

    def test_type_error_with_none(self):
        with self.assertRaises(TypeError):
            add_integer(None, 3)

if __name__ == '__main__':
    unittest.main()
