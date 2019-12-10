from metatool import dockertools
import re
import pytest

SAMPLE_FILE = "_samples/pdf/pdf_parser_test.pdf"
pattern = re.compile("^\\s*(\\S+)\\s+(\\S.*)$")

def test_help():
    tool = dockertools.tool_with_file(__file__)
    out = tool.run_get_string([])
    assert out.startswith("Usage: pdf-parser.py [options] pdf-file|zip-file|url")

def test_with_pdf():
    tool = dockertools.tool_with_file(__file__)
    out = tool.run_get_string([SAMPLE_FILE])
    values = {}
    for line in out.splitlines():
        m = re.match(pattern, line)
        if m is not None:
            print("X: {}({})".format(m.group(1), m.group(2)))
            values[m.group(1)] = m.group(2)
    title = bytearray.fromhex(values['/Title'][5:][:-1].replace('00','').lower()).decode()
    assert title == "CinCan"
