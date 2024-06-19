import pytest


@pytest.mark.xfail
def test_mark_xfail():
    raise RuntimeError


@pytest.mark.xfail(raises=RuntimeError)
def test_mark_xfail_with_raises():
    raise RuntimeError


def test_call_xfail():
    if 1 == 1:
        pytest.xfail("failing configuration (but should work)")
