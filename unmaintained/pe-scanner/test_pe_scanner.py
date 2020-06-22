from testing import dockertools
import pytest

@pytest.mark.dev
def test_no_args_give_error():
    tool = dockertools.tool_with_file(__file__)
    out = tool.run_get_string([])
    assert out.startswith("give input file\n")
