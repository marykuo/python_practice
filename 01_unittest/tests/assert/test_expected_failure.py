import unittest


# Test for expectedFailure() decorator
# Use expectedFailure() decorator for expected failures
class TestAssertFailure(unittest.TestCase):

    @unittest.expectedFailure
    def test_expected_failure(self):
        self.fail("should fail")
