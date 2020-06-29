from testing import dockertools
import pytest

SAMPLE_FILE="samples/html/pdfxray_lite_report.html"

def test_help():
    tool = dockertools.tool_with_file(__file__)
    out = tool.run_get_string([])
    assert "usage: standardizer <command> [<args>]" in out

def test_pdxraylite_report():
    tool = dockertools.tool_with_file(__file__)
    out = tool.run_get_string(["json", "-q", "-i", SAMPLE_FILE, "-o test", "-t", "pdfxray_lite"])
    assert "Standardizing outputs: 100%" in out


