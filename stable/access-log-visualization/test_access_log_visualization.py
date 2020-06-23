from testing import dockertools
import pytest

SAMPLE_FILE="samples/log/access.log"

def test_help():
    tool = dockertools.tool_with_file(__file__)
    out = tool.run_get_string([])
    assert out.startswith("usage: entrypoint.py [-h] -i INPUT [-o OUTPUT]")

def test_with_log():
    tool = dockertools.tool_with_file(__file__)
    out = tool.run_get_string(["-i", SAMPLE_FILE])
    print(out)
    for line in out.splitlines():
        if line.startswith("[NbConvertApp] Writing"):
            return
    assert False
