import pytest


def test_assertEqual_string(self):
    assert "foo".upper() == "FOO"
    assert "foo" == "foo"


def test_assertEqual_array(self):
    string_array = "hello world".split()
    expect_array = ["hello", "world"]

    assert string_array == expect_array
