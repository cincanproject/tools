from metatool import dockertools
import pytest
import os
import shutil

SAMPLE_FILE="_samples/amd64/hello_world"

def test_tools_help(tool):
    out = tool.run_get_string([])
    assert "Usage: floss [options] FILEPATH" in out

def test_get_strings(tool):
    out = tool.run_get_string([SAMPLE_FILE])
    assert out.startswith("FLOSS static ASCII strings\n/lib64/ld-linux-x86-64.so.2")

@pytest.fixture(scope='function')
def tool(request):
    tool = dockertools.tool_with_file(__file__)
    yield tool

