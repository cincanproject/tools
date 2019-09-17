from metatool import dockertools


def test_no_args_no_output():
    tool = dockertools.tool_with_file(__file__)
    out = tool.run_get_string([])
    assert out == ""
