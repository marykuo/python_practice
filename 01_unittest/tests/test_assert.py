import unittest


class TestArithmetic(unittest.TestCase):

    def test_assertEqual(self):
        # string
        self.assertEqual("foo".upper(), "FOO")

        # array
        string_array = "hello world".split()
        self.assertEqual(string_array, ["hello", "world"])

    def test_assertTrueOrFalse(self):
        self.assertTrue("FOO".isupper())
        self.assertFalse("Foo".isupper())

    def test_assertRaises(self):
        s = "hello world"
        with self.assertRaises(TypeError):
            s.split(2)


if __name__ == "__main__":
    unittest.main()
