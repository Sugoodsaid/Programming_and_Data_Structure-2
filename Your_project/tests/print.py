import unittest
from print import say_my_name
import io
import sys

class TestSayMyName(unittest.TestCase):
    def test_full_name(self):
        with io.StringIO() as buf, redirect_stdout(buf):
            say_my_name("John", "Doe")
            output = buf.getvalue().strip()
        self.assertEqual(output, "My name is John Doe")

    def test_first_name_only(self):
        with io.StringIO() as buf, redirect_stdout(buf):
            say_my_name("John")
            output = buf.getvalue().strip()
        self.assertEqual(output, "My name is John")

    def test_type_error_first_name(self):
        with self.assertRaises(TypeError):
            say_my_name(123, "Doe")

    def test_type_error_last_name(self):
        with self.assertRaises(TypeError):
            say_my_name("John", 456)

if __name__ == '__main__':
    unittest.main()
