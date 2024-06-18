import unittest


class TestSkip(unittest.TestCase):

    # skip() decorator can use on class or method
    @unittest.skip("deprecated requirement")
    def test_skip_decorator(self):
        print("shouldn't happen")

    # skip the decorated test if condition is true
    @unittest.skipIf(1 == 1, "reason")
    def test_skipIf(self):
        print("shouldn't happen")

    # call TestCase.skipTest() directly
    def test_skip(self):
        if 1 == 1:
            self.skipTest("external resource not available")
        print("shouldn't happen")


if __name__ == "__main__":
    unittest.main()
