import sys
import pytest
from .. import dockertools


def test_image():
    dockertools.ToolImage("xmldump", ["samples/simple.xml"])
