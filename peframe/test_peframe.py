from metatool import dockertools


def test_help():
    tool = dockertools.tool_with_file(__file__)
    out = tool.run_get_string([])
    assert out.startswith("usage: peframe [-h] [-v] [-i] [-x XORSEARCH] [-j] [-s] file")
