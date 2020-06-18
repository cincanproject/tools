from metatool import dockertools
import pytest

SAMPLE_FILE="_samples/msdos/suspicious_dos_sample.exe"

def test_help():
    tool = dockertools.tool_with_file(__file__)
    out = tool.run_get_string([])
    assert out.startswith("Usage: nocode [options] [--] file...")

def test_auto_decompile():
    tool = dockertools.tool_with_file(__file__)
    out = tool.run_get_string([SAMPLE_FILE])
    assert out.strip().startswith("struct s0")