from metatool import dockertools
import pytest

SAMPLE = '_samples/msdos/suspicious_dos_sample.exe'

def test_entrypoint():
    tool = dockertools.tool_with_file(__file__)
    out = tool.run_get_string([])
    assert out.startswith("Usage:")

def test_help():
    tool = dockertools.tool_with_file(__file__)
    out = tool.run_get_string(["--help"])
    assert out.startswith("Usage:")

def test_pe_sample():
    tool = dockertools.tool_with_file(__file__)
    out = tool.run_get_string(args=['--pe', SAMPLE])
    for i, line in enumerate(out.splitlines()):
        if i == 9:
            assert line.endswith("IMAGE_FILE_MACHINE_I386\n")

    assert out.startswith('* Manalyze 0.9 *')