import sys
import pytest
from .. import dockertools


def test_image():
    tool = dockertools.ToolImage("xmldump")
    tool.run(["text", "samples/simple.xml"])
