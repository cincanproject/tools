import os
from testing import dockertools
import pytest

SAMPLE_FILE = "samples/compressed/tampered_sample.bin"

def test_help():
    tool = dockertools.tool_with_file(__file__)
    out = tool.run_get_string([])
    assert out.startswith("\nBinwalk")

def test_with_sample():
    tool = dockertools.tool_with_file(__file__)
    tool_output = tool.run_get_string([SAMPLE_FILE])
    right_answer = "15            0xF             gzip compressed data, from Unix, last modified:"
    assert right_answer in tool_output
