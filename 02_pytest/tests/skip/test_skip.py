import pytest


@pytest.mark.skip(reason="no way of currently testing this")
def test_mark_skip():
    pass


def test_call_skip():
    if 1 == 1:
        pytest.skip("unsupported configuration")
