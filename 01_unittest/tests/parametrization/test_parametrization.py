import unittest
from parameterized import parameterized, parameterized_class, param


class TestParameterizedMarkOnModule(unittest.TestCase):
    # second parameter _ defines name of test
    @parameterized.expand(
        [
            ("positive", 1, 1, 2),
            ("zero", 1, 0, 1),
            ("negitive", -1, 2, 1),
        ]
    )
    def test_listOfTuple(self, _, num1, num2, sum):
        self.assertEqual(num1 + num2, sum)

    @parameterized.expand(
        [
            param(num1=1, num2=1, sum=2),
            param(1, 0, 1),
            param(-1, 2, 1),
        ]
    )
    def test_listOfParam(self, num1, num2, sum):
        self.assertEqual(num1 + num2, sum)


@parameterized_class(
    ("num1", "num2", "sum"),
    [
        (1, 2, 3),
        (5, 0, 5),
    ],
)
class TestParameterizedMarkOnClassWithListOfTuple(unittest.TestCase):
    def test_add(self):
        self.assertEqual(self.num1 + self.num2, self.sum)


@parameterized_class(
    [
        {"num1": 3, "sum": 4},
        {"num1": 0, "sum": 1},
        {"sum": 2},
    ]
)
class TestParameterizedMarkOnClassWithListOfObject(unittest.TestCase):
    num1 = 1
    num2 = 1

    def test_subtract(self):
        self.assertEqual(self.num1 + self.num2, self.sum)
