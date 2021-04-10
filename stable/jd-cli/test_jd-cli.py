from testing import dockertools
import pytest

SAMPLE_FILE="samples/java/HexDump.class"

def test_help():
    tool = dockertools.tool_with_file(__file__)
    out = tool.run_get_string([])
    assert out.startswith("jd-cli version 1.2.0 - Copyrigh")

def test_decompile():
    tool = dockertools.tool_with_file(__file__)
    out = tool.run_get_string([SAMPLE_FILE])
    assert "public class HexDump" in out
