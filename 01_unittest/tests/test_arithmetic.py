import unittest
from calculator.arithmetic import add, subtract


class TestArithmetic(unittest.TestCase):

    def test_add(self):
        print("run test_add")
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(-1, 1), 0)

    def test_subtract(self):
        print("run test_subtract")
        self.assertEqual(subtract(2, 1), 1)
        self.assertEqual(subtract(2, 2), 0)


if __name__ == "__main__":
    unittest.main()
