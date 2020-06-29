from testing import dockertools
import pytest

SAMPLE_FILE="samples/pdf/ioc_test.pdf"

def test_help():
    tool = dockertools.tool_with_file(__file__)
    out = tool.run_get_string([])
    assert out.startswith("usage: iocstrings")

def test_ioc():
    tool = dockertools.tool_with_file(__file__)
    out = tool.run_get_string([SAMPLE_FILE])
    assert "UWk.TbOF" in out

