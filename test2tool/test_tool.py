import os
import tarfile

from metatool import dockertools


def test_echo():
    tool = dockertools.tool_with_file(__file__)
    out = tool.run_get_string(["echo HelloWorld"])
    assert out == "HelloWorld\n"
