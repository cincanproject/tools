from testing import dockertools
import pytest

SAMPLE_FILE="samples/msoffice/very_suspicious.doc"

def test_help(tool):
    out = tool.run_get_string([])
    assert "Usage: vmonkey.py [options] <filename> [filename2 ...]" in out

def test_ioc_extraction(tool):
    out = tool.run_get_string(["-c", SAMPLE_FILE])
    assert "powershell -ExecutionPolicy Bypass -NoProfile -WindowStyle Hidden -NoExit" in out
    assert "TVqQAAMAAAAAAAAAAACAAAGAucnNyYwAAAPwQAAAAYAAAABIAA" in out

@pytest.fixture(scope='function')
def tool(request):
    tool = dockertools.tool_with_file(__file__)
    yield tool

