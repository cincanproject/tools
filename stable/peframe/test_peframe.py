from testing import dockertools
import pytest

SAMPLE = 'samples/msdos/suspicious_dos_sample.exe'
def test_help():
    tool = dockertools.tool_with_file(__file__)
    out = tool.run_get_string([])
    assert out.startswith("usage: peframe [-h] [-v] [-i] [-x XORSEARCH] [-j] [-s] file")

def test_pe_sample():
    tool = dockertools.tool_with_file(__file__)
    out = tool.run_get_string(args=['-j', SAMPLE])
    assert out.startswith('{\n    "docinfo": {},\n')
