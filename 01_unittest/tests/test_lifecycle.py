import unittest


class TestLifecycle(unittest.TestCase):

    # run once before all tests
    @classmethod
    def setUpClass(self):
        print("\nsetUpClass")

    # run once after all tests
    @classmethod
    def tearDownClass(self):
        print("tearDownClass")

    # run once before each test
    def setUp(self):
        print("\nsetUp")

    # run once after each test
    def tearDown(self):
        print("tearDown")

    def test_first(self):
        print("first")

    def test_second(self):
        print("second")


if __name__ == "__main__":
    unittest.main()
