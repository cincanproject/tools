from metatool import dockertools

def test_help():
    tool = dockertools.tool_with_file(__file__)
    out = tool.run_get_string([])
    assert out.startswith("Usage: pdf-parser.py [options] pdf-file|zip-file|url")

