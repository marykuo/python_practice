import pytest


def test_assertRaises_TypeError(self):
    with pytest.raises(TypeError):
        "hello world".split(2)


def test_assertRaises_regex(self):
    with pytest.raises(TypeError, match=r"^must be str or None, not int$"):
        "hello world".split(2)


# ExceptionInfo instance's main attributes are type, value, traceback
def test_assertRaises_exceptionInfo(self):
    with pytest.raises(TypeError) as exceptionInfo:
        "hello world".split(2)

    assert exceptionInfo.type is TypeError
    assert "must be str or None, not int" in str(exceptionInfo.value)
