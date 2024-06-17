import unittest


class TestArithmetic(unittest.TestCase):

    # run once per test
    def setUp(self):
        print("\nsetUp")

    # run once per test
    def tearDown(self):
        print("tearDown\n")

    def test_first(self):
        print("first")

    def test_second(self):
        print("second")


if __name__ == "__main__":
    unittest.main()
