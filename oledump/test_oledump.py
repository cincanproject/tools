from metatool import dockertools

def test_help():
    tool = dockertools.tool_with_file(__file__)
    out = tool.run_get_string([])
    assert out.startswith("Usage: oledump.py [options] [file]")

def test_with_document():
    tool = dockertools.tool_with_file(__file__)
    out = tool.run_get_string([tool.file_to_copy_from_context("samples/testfile.docm"), "-S", "-s", "3"])
    assert "CinCan" in out.splitlines()[1]

