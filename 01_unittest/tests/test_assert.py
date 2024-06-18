import unittest


# Test for assertEqual() and assertIs()
# assertIs() checks if two objects are the same object (identity check)
# assertEqual() checks if two objects have the same value (equality check)
class TestAssertEqual(unittest.TestCase):

    def test_assertEqual_string(self):
        self.assertEqual("foo".upper(), "FOO")
        self.assertIs("foo", "foo")

    def test_assertEqual_array(self):
        string_array = "hello world".split()
        expect_array = ["hello", "world"]

        self.assertEqual(string_array, expect_array)
        self.assertIsNot(string_array, expect_array)


# Test for assertIn() and assertNotIn()
# Check that a string is in another string
class TestAssertIn(unittest.TestCase):

    def test_assertIn_substring_at_start(self):
        self.assertIn("Hello", "Hello World!")

    def test_assertIn_substring_in_middle(self):
        self.assertIn("World", "Hello World!")

    def test_assertNotIn_substring_case_sensitive(self):
        self.assertNotIn("hello", "Hello World!")


# Test for assertIsNone() and assertIsNotNone()
# Check that the input value is None or not
class TestAssertNone(unittest.TestCase):

    def test_assertIsNone(self):
        self.assertIsNone(None)

    def test_assertIsNotNone(self):
        self.assertIsNotNone("")


# Test for assertIsInstance()
# Check that the given object is an instance of a given class or not
class TestAssertIsInstance(unittest.TestCase):

    def test_assertIsInstance_string(self):
        self.assertIsInstance("string", str)


# Test for assertTrue() and assertFalse()
# call assertTrue() or assertFalse() to verify a condition
class TestAssertCondition(unittest.TestCase):

    def test_assertTrue(self):
        self.assertTrue("FOO".isupper())

    def test_assertFalse(self):
        self.assertFalse("Foo".isupper())


# Tests for assertRaises() and assertRaisesRegex()
# assertRaises() checks that a specific exception is raised
# assertRaisesRegex() checks that a specific exception is raised and that the exception's message matches a given regular expression
class TestAssertRaises(unittest.TestCase):

    def test_assertRaises_TypeError(self):
        with self.assertRaises(TypeError):
            "hello world".split(2)

    def test_assertRaisesRegex_TypeError(self):
        with self.assertRaisesRegex(TypeError, "^must be str or None, not int$"):
            "hello world".split(2)


# Test for expectedFailure() decorator
# Use expectedFailure() decorator for expected failures
class TestAssertFailure(unittest.TestCase):

    @unittest.expectedFailure
    def test_expected_failure(self):
        self.fail("should fail")


if __name__ == "__main__":
    unittest.main()
