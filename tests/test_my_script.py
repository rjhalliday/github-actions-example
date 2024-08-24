import unittest
from my_module.my_script import add_numbers

class TestAddNumbers(unittest.TestCase):
    def test_add_numbers(self):
        self.assertEqual(add_numbers(2, 3), 5)
        self.assertEqual(add_numbers(-1, 1), 0)
        self.assertEqual(add_numbers(-5, -5), -10)

if __name__ == '__main__':
    unittest.main()
