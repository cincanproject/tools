from testing import dockertools
import pytest

SAMPLE_FILE="samples/image/post-scam-sms.png"

def test_entrypoint():
    tool = dockertools.tool_with_file(__file__)
    out = tool.run_get_string([])
    assert "File to OCR" in out

def test_sms_ocr():
    tool = dockertools.tool_with_file(__file__)
    out = tool.run_get_string([SAMPLE_FILE])
    assert "perjantai 6. syyskuuta 2019" in out
    assert "Hyva asiakas, pakettiasi ei" in out
    assert "voitu toimittaa 3.9.2019" in out
    assert "koska tullimaksuja ei ole" in out
    assert "http://v6f.us/Z9zmo" in out

def test_finnish_ocr():
    tool = dockertools.tool_with_file(__file__)
    out = tool.run_get_string([SAMPLE_FILE, "-l", "fin"])
    assert "Hyvä asiakas, pakettiasi ei" in out
    assert "voitu toimittaa 3.9.2019" in out
    assert "koska tullimaksuja ei ole" in out
    assert "http://v6f.us/Z9zmo" in out

