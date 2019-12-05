from metatool import dockertools

SAMPLE_FILE="_samples/msoffice/testfile.docm"

def test_help():
    tool = dockertools.tool_with_file(__file__)
    out = tool.run_get_string([])
    assert out.startswith("Usage: oledump.py [options] [file]")

def test_with_document():
    tool = dockertools.tool_with_file(__file__)
    out = tool.run_get_string([SAMPLE_FILE, "-S", "-s", "3"])
    assert "CinCan" in out.splitlines()[1]

