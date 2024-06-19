import sys
import pytest


@pytest.mark.skipif(sys.version_info < (3, 10), reason="requires python3.10 or higher")
def test_mark_skipif_on_function():
    pass

@pytest.mark.skipif(sys.version_info < (3, 10), reason="requires python3.10 or higher")
class TestSkipIf:
    def test_mark_skipif_on_module(self):
        "will not be setup or run under 'win32' platform"
