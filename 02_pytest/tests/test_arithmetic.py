import pytest
from calculator.arithmetic import add, subtract


class TestAdd:
    def test_add_positive(self):
        assert add(1, 2) == 3

    def test_add_zero(self):
        assert add(-1, 1) == 0

    def test_add_negative(self):
        assert add(-1, -1) == -2


class TestSubtract:
    def test_subtract_positive(self):
        assert subtract(2, 1) == 1

    def test_subtract_zero(self):
        assert subtract(2, 2) == 0

    def test_subtract_negative(self):
        assert subtract(-1, -1) == 0
