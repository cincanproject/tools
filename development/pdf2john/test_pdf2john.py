from metatool import dockertools
import pytest

@pytest.mark.dev
def test_help():
    tool = dockertools.tool_with_file(__file__)
    out = tool.run_get_string([])
    assert out.startswith("Syntax:  pdf2john.pl <.pdf file(s)>")
