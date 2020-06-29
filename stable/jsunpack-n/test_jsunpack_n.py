from testing import dockertools
import pytest

SAMPLE_FILE="samples/pdf/javascript_test.pdf"

def test_help():
    tool = dockertools.tool_with_file(__file__)
    out = tool.run_get_string([])
    assert out.startswith("Usage: \n\t./jsunpackn.py [fileName")

def test_with_pdf():
    tool = dockertools.tool_with_file(__file__)
    out = tool.run_get_string([SAMPLE_FILE, "-V"])
    assert "decoding_530752faa103f6929a7f067eee4088517970e6a9" in out.splitlines()[3]

