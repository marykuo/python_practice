import unittest
from calculator.arithmetic import add, subtract


class TestAdd(unittest.TestCase):

    def test_add_positive(self):
        self.assertEqual(add(1, 2), 3)

    def test_add_zero(self):
        self.assertEqual(add(-1, 1), 0)

    def test_add_negative(self):
        self.assertEqual(add(-1, -1), -2)


class TestSubtract(unittest.TestCase):

    def test_subtract_positive(self):
        self.assertEqual(subtract(2, 1), 1)

    def test_subtract_zero(self):
        self.assertEqual(subtract(2, 2), 0)

    def test_subtract_negative(self):
        self.assertEqual(subtract(-1, -1), 0)


if __name__ == "__main__":
    unittest.main()
