from metatool import dockertools
import re
import pytest

SAMPLE_FILE="_samples/pdf/text_text.pdf"

pattern = re.compile("^\\s*(\\S+)\\s+(\\S.*)$")

@pytest.mark.dev
def test_help():
    tool = dockertools.tool_with_file(__file__)
    out = tool.run_get_string([])
    assert out.startswith("Usage: pdfid.py [options] [pdf-file|zip-file|url|@file] ...")

@pytest.mark.dev
def test_with_pdf():
    tool = dockertools.tool_with_file(__file__)
    out = tool.run_get_string([SAMPLE_FILE])
    values = {}
    for line in out.splitlines():
        m = re.match(pattern, line)
        if m is not None:
            print("X: {}({})".format(m.group(1), m.group(2)))
            values[m.group(1)] = m.group(2)
    assert values['obj'] == '13'
    assert values['endobj'] == '13'
    assert values['stream'] == '2'
    assert values['xref'] == '1'
