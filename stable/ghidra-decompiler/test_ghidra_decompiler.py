from testing import dockertools
import pytest

SAMPLE_FILE="samples/amd64/hello_world"

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
    assert out.strip().startswith("\x1b[32mAdded 'samples/amd64/hello_world' as analysis target.")

def test_decompile_output():
    tool = dockertools.tool_with_file(__file__)
    out = tool.run_get_string(["decompile", SAMPLE_FILE])
    "__libc_start_main(main,in_stack_00000000,&stack0x00000008,__libc_csu_init,__libc_csu_fini,param_3," in out
