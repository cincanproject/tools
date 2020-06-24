from testing import dockertools


SAMPLE_FILE = "samples/pdf/general_test_file.pdf"


def test_entrypoint():
    tool = dockertools.tool_with_file(__file__)
    out = tool.run_get_string([])
    assert out.startswith("Usage: pdfxray_lite.py [options]")

def test_help():
    tool = dockertools.tool_with_file(__file__)
    out = tool.run_get_string(["--help"])
    assert out.startswith("Usage: pdfxray_lite.py [options]")

def test_with_pdf():
    tool = dockertools.tool_with_file(__file__)
    out = tool.run_get_string(["-f", SAMPLE_FILE, "-r", "output"])
    # md5 is calculated to stdout
    assert "78f981873db5f6b9a4051c81e8ab7788" in out
