from metatool import dockertools
from pathlib import Path
import pytest
import os

# Filepath relative to project root directory (expected location to call pytest)
SAMPLE_FILE="virustotal-api/samples/url_sample.txt"


def test_entry_point():
    tool = dockertools.tool_with_file(__file__)
    out = tool.run_get_string([])
    assert out.startswith("usage: vt.py")

