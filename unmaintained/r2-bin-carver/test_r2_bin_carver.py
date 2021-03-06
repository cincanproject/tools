from testing import dockertools
import pytest

@pytest.mark.dev

def test_help():
    tool = dockertools.tool_with_file(__file__)
    out = tool.run_get_string([])
    assert out.startswith("usage: r2_bin_carver.py [-h] [-b B] [-p] dmp offset size")
