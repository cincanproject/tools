from metatool import dockertools
import pytest

@pytest.mark.dev
def test_help():
    tool = dockertools.tool_with_file(__file__)
    out = tool.run_get_string([])
    assert out.startswith("usage: /usr/local/bin/ssdc [-h] [-v] [-r] [-o [output]] [-s] [-d]")

