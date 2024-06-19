import pytest

# If you want to skip all test functions of a module, you may use the pytestmark global
pytestmark = pytest.mark.skip("all tests still WIP")

# Skip all tests in a module if some import is missing
docutils = pytest.importorskip("docutils")
pexpect = pytest.importorskip("pexpect")
