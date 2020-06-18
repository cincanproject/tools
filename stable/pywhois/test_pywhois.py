import json

from testing import dockertools
import pytest

def test_help():
    tool = dockertools.tool_with_file(__file__)
    out = tool.run_get_string([])
    assert out.startswith("usage: query.py [-h] [-f FILE] [ip]")


def test_localhost():
    tool = dockertools.tool_with_file(__file__)
    out = tool.run_get_string(['127.0.0.1'])
    r = json.loads(out)
    assert r['org'] is None
    assert r['domain_name'] is None
    assert r['address'] is None
