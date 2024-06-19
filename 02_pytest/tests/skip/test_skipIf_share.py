import sys
import pytest

# You also can import the marker from another test module and reuse it
minversion = pytest.mark.skipif(
    sys.version_info < (3, 10), reason="requires python3.10 or higher"
)


@minversion
def test_share_skipIf_1():
    pass


@minversion
def test_share_skipIf_2():
    pass
