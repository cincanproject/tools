from testing import dockertools
import pytest
import json

SAMPLE_FILE = "https://github.com/dxa4481/truffleHog.git"

def test_help():
    tool = dockertools.tool_with_file(__file__)
    out = tool.run_get_string([])
    assert out.startswith("usage: trufflehog")

def test_git_url():
    """Test that trufflehog gives any output from given url"""
    tool = dockertools.tool_with_file(__file__)
    out = tool.run_get_string([SAMPLE_FILE])
    if not (out is None):
        assert True
    else:
        assert False
