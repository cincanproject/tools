from testing import dockertools
import pytest

def test_help():
    tool = dockertools.tool_with_file(__file__)
    out = tool.run_get_string([])
    assert out.startswith("usage: analyze_parallel.py [-h] [--infile INFILE] [--injsonl INJSONL]")
