from metatool import dockertools
import pytest

def test_entrypoint():
    tool = dockertools.tool_with_file(__file__)
    out = tool.run_get_string([])
    assert out.startswith("\n  This is shell script wrapper for radare2.\n")

def test_help():
    tool = dockertools.tool_with_file(__file__)
    out = tool.run_get_string(["--help"])
    assert out.startswith("\n  This is shell script wrapper for radare2.\n")

def test_r2():
    tool = dockertools.tool_with_file(__file__)
    out = tool.run_get_string(["r2", "-h"])
    assert out.startswith("Usage: r2 [-ACdfLMnNqStuvwzX] [-P patch] ")  

def test_grapscript_no_args_error():
    tool = dockertools.tool_with_file(__file__)
    out = tool.run_get_string(["script", "r2_callgraph.sh"])
    assert out.startswith("No sample directory provided. ")