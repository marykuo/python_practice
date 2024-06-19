import unittest


# Tests for assertRaises() and assertRaisesRegex()
# assertRaises() checks that a specific exception is raised
# assertRaisesRegex() checks that a specific exception is raised and that the exception's message matches a given regular expression
class TestAssertRaises(unittest.TestCase):

    def test_assertRaises_TypeError(self):
        with self.assertRaises(TypeError):
            "hello world".split(2)

    def test_assertRaisesRegex_TypeError(self):
        with self.assertRaisesRegex(TypeError, r"^must be str or None, not int$"):
            "hello world".split(2)
