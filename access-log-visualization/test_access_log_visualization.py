import dockertools


def test_help():
    tool = dockertools.tool_with_file(__file__)
    out = tool.run_get_string([])
    assert out.startswith("[NbConvertApp] WARNING | pattern '/samples/access-log.ipynb' matched no files")
