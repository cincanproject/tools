from metatool import dockertools
import pytest

def test_headers(tool):
    out = tool.run_get_string(["headers", "_samples/txt/test.csv"])
    assert "1   foo" in out
    assert "2   bar" in out

def test_count(tool):
    out = tool.run_get_string(["frequency", "_samples/txt/test.csv"])
    assert "foo,42,1" in out

@pytest.fixture(scope='function')
def tool(request):
    tool = dockertools.tool_with_file(__file__)
    yield tool

