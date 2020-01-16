from metatool import dockertools
import pytest

SAMPLE_FILE="_samples/txt/base64.txt"

def test_tools_help(tool):
    out = tool.run_get_string(["-h"])
    assert "pastelyzer" in out

def test_nested_base64_gzip(tool):
    out = tool.run_get_string([SAMPLE_FILE])
    assert "IP-ADDRESS: 8.8.8.8" in out
    assert "IP-ADDRESS: 1.1.1.1" in out
    assert "DOMAIN: google.com" in out
    assert "DOMAIN: bing.com" in out
 
@pytest.fixture(scope='function')
def tool(request):
    tool = dockertools.tool_with_file(__file__)
    yield tool

