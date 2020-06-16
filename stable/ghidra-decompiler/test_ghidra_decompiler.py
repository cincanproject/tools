from metatool import dockertools
import pytest

SAMPLE_FILE="_samples/amd64/hello_world"

def test_entrypoint():
    tool = dockertools.tool_with_file(__file__)
    out = tool.run_get_string([])
    assert out.strip().startswith("\x1b[93mThis is shell script wrapper around 'Ghidra Headless Analyzer'.")

def test_help():
    tool = dockertools.tool_with_file(__file__)
    out = tool.run_get_string(["--help"])
    assert out.strip().startswith("\x1b[93mThis is shell script wrapper around 'Ghidra Headless Analyzer'.")


def test_auto_decompile():
    tool = dockertools.tool_with_file(__file__)
    out = tool.run_get_string(["decompile", SAMPLE_FILE])
    assert out.strip().startswith("\x1b[32mAdded '_samples/amd64/hello_world' as analysis target.")