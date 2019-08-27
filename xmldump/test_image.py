import sys
import pytest
from .. import dockertools


def test_image():
    dockertools.ToolImage(".", "samples/simple.xml")
