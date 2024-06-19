import pytest


@pytest.mark.parametrize("x", [0, 1])
@pytest.mark.parametrize("y", [2, 3])
def test_foo(x, y):
    # run the test with the arguments set to x=0/y=2, x=1/y=2, x=0/y=3, and x=1/y=3
    pass
