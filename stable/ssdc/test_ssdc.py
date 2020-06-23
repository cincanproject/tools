from testing import dockertools
import pytest

SAMPLE_FILE="samples/disks/"

def test_help():
    tool = dockertools.tool_with_file(__file__)
    out = tool.run_get_string([])
    assert out.startswith("usage: /usr/local/bin/ssdc [-h] [-v] [-r] [-o [output]] [-s] [-d]")

def test_hash():
    tool = dockertools.tool_with_file(__file__)
    out = tool.run_get_string([SAMPLE_FILE])
    assert "SHA256" in out
