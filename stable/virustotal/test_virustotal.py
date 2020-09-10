from testing import dockertools
import pytest


def test_entrypoint():
    tool = dockertools.tool_with_file(__file__)
    out = tool.run_get_string([])
    assert out.startswith("A command-line tool for interacting with VirusTotal.")

def test_help():
    tool = dockertools.tool_with_file(__file__)
    out = tool.run_get_string(["--help"])
    assert out.startswith("A command-line tool for interacting with VirusTotal.")
