import json
import os
import tarfile

from metatool import dockertools


def test_help():
    tool = dockertools.tool_with_file(__file__)
    out = tool.run_get_string([])
    assert out.startswith("Usage: xmldump.py [options] command [[@]file ...]")


def test_xml_to_text():
    tool = dockertools.tool_with_file(__file__)
    out = tool.run_get_string(["text", tool.file_to_copy_from_context("samples/simple.xml")])
    assert out == 'Hello World\n'
