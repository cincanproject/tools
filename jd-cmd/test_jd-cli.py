from metatool import dockertools
import pytest

@pytest.mark.dev
def test_help():
    tool = dockertools.tool_with_file(__file__)
    out = tool.run_get_string([])
    assert out.startswith("jd-cli version 1.0.0.Final")

