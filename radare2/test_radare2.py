from metatool import dockertools
import pytest

SAMPLE_FILE = "_samples/amd64/hello_world_r2 "

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

def test_radare2():
    tool = dockertools.tool_with_file(__file__)
    out = tool.run_get_string(["radare2", "-h"])
    assert out.startswith("Usage: r2 [-ACdfLMnNqStuvwzX] [-P patch] ")  

def test_r2pm():
    tool = dockertools.tool_with_file(__file__)
    out = tool.run_get_string(["r2pm", "-h"])
    assert out.startswith("Usage: r2pm [init|update|cmd] [...]")  

def test_rabin2():
    tool = dockertools.tool_with_file(__file__)
    out = tool.run_get_string(["rabin2", "-h"])
    assert out.startswith("Usage: rabin2 [-AcdeEghHiIjlLMqrRsSUvVxzZ]")

def test_radiff2():
    tool = dockertools.tool_with_file(__file__)
    out = tool.run_get_string(["radiff2", "-h"])
    assert out.startswith("Usage: radiff2 [-abBcCdjrspOxuUvV] ")

def test_rafind2():
    tool = dockertools.tool_with_file(__file__)
    out = tool.run_get_string(["rafind2", "-h"])
    assert out.startswith("Usage: rafind2 [-mXnzZhqv] ")

def test_ragg2():
    tool = dockertools.tool_with_file(__file__)
    out = tool.run_get_string(["ragg2", "-h"])
    assert out.startswith("Usage: ragg2 [-FOLsrxhvz] ")

def test_rahash2():
    tool = dockertools.tool_with_file(__file__)
    out = tool.run_get_string(["rahash2", "-h"])
    assert out.startswith("Usage: rahash2 [-rBhLkv] [")

def test_rarun2():
    tool = dockertools.tool_with_file(__file__)
    out = tool.run_get_string(["rarun2", "-h"])
    assert out.startswith("Usage: rarun2 -v|-t|script.rr2 [directive ..]")

def test_rasm2():
    tool = dockertools.tool_with_file(__file__)
    out = tool.run_get_string(["rasm2", "-h"])
    assert out.startswith("Usage: rasm2 [-ACdDehLBvw] [-a arch] ")

def test_rax2():
    tool = dockertools.tool_with_file(__file__)
    out = tool.run_get_string(["rax2", "-h"])
    assert out.startswith("Usage: rax2 [options] [expr ...]")

def test_simple_inline_analysis():
    tool = dockertools.tool_with_file(__file__)
    out = tool.run_get_string(["r2", "-Aqc", "'pdf @main'", SAMPLE_FILE])
    assert out.startswith("            ; DATA XREF from entry0 @ 0x1061")

def test_grapscript_no_args_error():
    tool = dockertools.tool_with_file(__file__)
    out = tool.run_get_string(["script", "r2_callgraph.sh"])
    assert out.startswith("No sample directory provided. ")