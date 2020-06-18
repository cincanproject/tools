from testing import dockertools

SAMPLE_FILE="samples/pdf/general_test_file.pdf"

def test_help():
    tool = dockertools.tool_with_file(__file__)
    out = tool.run_get_string([])
    assert out.startswith("Usage: peepdf.py [options] PDF_file")

def test_with_pdf():
    tool = dockertools.tool_with_file(__file__)
    out = tool.run_get_string([SAMPLE_FILE, "-f", "-C", "js_beautify object 7"])
    assert "CinCan" in out.splitlines()[10]

