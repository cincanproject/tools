from metatool import dockertools
import pytest

SAMPLE = '_samples/msdos/suspicious_dos_sample.exe'
def test_help():
    tool = dockertools.tool_with_file(__file__)
    out = tool.run_get_string([])
    assert out.startswith("Usage:")

def test_pe_sample():
    tool = dockertools.tool_with_file(__file__)
    out = tool.run_get_string(args=['--pe', SAMPLE])
    assert out.startswith('* Manalyze 0.9 *')