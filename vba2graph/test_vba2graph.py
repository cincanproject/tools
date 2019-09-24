from metatool import dockertools


def test_help():
    tool = dockertools.tool_with_file(__file__)
    out = tool.run_get_string([])
    assert out.startswith("usage: vba2graph.py [-h] [-o OUTPUT] [-c {0,1,2,3}]")
