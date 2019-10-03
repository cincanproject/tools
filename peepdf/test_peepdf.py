from metatool import dockertools


def test_help():
    tool = dockertools.tool_with_file(__file__)
    out = tool.run_get_string([])
    assert out.startswith("Usage: peepdf.py [options] PDF_file")
