from testing import dockertools
import pytest
# Filepath relative to project root directory (expected location to call pytest)
SAMPLE_FILE="samples/msdos/suspicious_dos_sample.exe"

# Should be identical for testing '--help' argument
def test_entry_point():
    tool = dockertools.tool_with_file(__file__)
    out = tool.run_get_string([])
    assert "Usage: yara [OPTION]." in out

def test_help():
    tool = dockertools.tool_with_file(__file__)
    out = tool.run_get_string(["--help"])
    assert "Usage: yara [OPTION]." in out


def test_scan_all_rules():
    tool = dockertools.tool_with_file(__file__)
    out = tool.run_get_string(["-w", "/rules/index.yar", SAMPLE_FILE])
    assert "IsPE32" in out
    assert "IsNET_EXE" in out
    assert "Microsoft_Visual_Studio_NET" in out
