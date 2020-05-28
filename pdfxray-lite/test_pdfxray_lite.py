from metatool import dockertools
import pytest

#@pytest.mark.dev

SAMPLE_FILE="_samples/pdf/general_test_file.pdf"


def test_help():
    tool = dockertools.tool_with_file(__file__)
    out = tool.run_get_string([])
    assert out.startswith("Usage: pdfxray_lite.py [options]")

def test_with_pdf():
    tool = dockertools.tool_with_file(__file__)
    out = tool.run_get_string(["-f", SAMPLE_FILE, "-r", "."])
    assert "report.html" in out.splitlines()[-1]