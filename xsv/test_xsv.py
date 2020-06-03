from metatool import dockertools
import pytest


def test_count(tool):
    out = tool.run_get_string(["frequency", "_samples/test.csv"])
    assert "foo,42,1" in out

@pytest.fixture(scope='function')
def tool(request):
    tool = dockertools.tool_with_file(__file__)
    yield tool

