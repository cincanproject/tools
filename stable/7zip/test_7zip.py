from os import path, getcwd
import shutil
import pytest
from testing import dockertools
from pathlib import Path

SAMPLE_FILE="samples/msoffice/very_suspicious.doc"

def test_help():
    tool = dockertools.tool_with_file(__file__)
    out = tool.run_get_string(["-h"])
    assert "7-Zip [64]" in out

def test_extract(tmp_path):
    d = tmp_path / "7zip_tool"
    d.mkdir()
    tool = dockertools.tool_with_file(__file__)
    tool.output_dirs = [d.relative_to(getcwd())]
    out = tool.run_get_string(["l", SAMPLE_FILE])
    assert "Macros" in out
