from testing import dockertools
import pytest
import os

SAMPLE_FILE="samples/source/lua/while.lua"
SAMPLE_BYTECODE="samples/source/lua/while.luac"

def test_tools_help(tool):
    out = tool.run_get_string([])
    assert "no input files given" in out

def test_source_decompile(tmp_path, tool):
    out = tool.run_get_string([SAMPLE_FILE])
    assert "-- Decompiled using luadec" in out
    assert "while 1 do" in out
    assert "if a then" in out

def test_bytecode(tmp_path, tool):
    out = tool.run_get_string([SAMPLE_BYTECODE])
    assert "-- Decompiled using luadec" in out
    assert "while 1 do" in out
    assert "if a then" in out

@pytest.fixture(scope='function')
def tool(request):
    tool = dockertools.tool_with_file(__file__)
    yield tool

