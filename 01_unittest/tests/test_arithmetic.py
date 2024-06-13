import unittest
import calculator


class TestArithmetic(unittest.TestCase):

    def test_add(self):
        print("run test_add")
        self.assertEqual(calculator.add(1, 2), 3)
        self.assertEqual(calculator.add(-1, 1), 0)

    def test_subtract(self):
        print("run test_subtract")
        self.assertEqual(calculator.subtract(2, 1), 1)
        self.assertEqual(calculator.subtract(2, 2), 0)


if __name__ == "__main__":
    unittest.main()
