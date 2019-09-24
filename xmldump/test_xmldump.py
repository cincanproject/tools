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


def test_do_run():
    tool = dockertools.tool_with_file(__file__)
    tool.upload_tar = tool.file_to_copy_from_context("samples/simple.tar", prefix=False)
    tool.output_tar = "/tmp" + __file__ + ".tar"
    tool.do_run()
    with tarfile.open(tool.output_tar) as tar:
       meta = json.load(tar.extractfile(tool.metadata_file))
       out = tar.extractfile("output").read()
    os.unlink(tool.output_tar)
    assert meta['files'][0]['name'] == "output"
    assert meta['files'][0]['type'] == "text/plain"
    assert out == b'Hello World\n'


def test_do_run_read_file():
    tool = dockertools.tool_with_file(__file__)
    tool.output_tar = "/tmp" + __file__ + ".tar"
    tool.do_run(in_file=tool.file_to_copy_from_context("samples/simple.xml", prefix=False))
    with tarfile.open(tool.output_tar) as tar:
       meta = json.load(tar.extractfile(tool.metadata_file))
       out = tar.extractfile("output").read()
    os.unlink(tool.output_tar)
    assert meta['files'][0]['name'] == "output"
    assert meta['files'][0]['type'] == "text/plain"
    assert out == b'Hello World\n'


def test_do_run_get_string():
    tool = dockertools.tool_with_file(__file__)
    out = tool.do_get_string(in_file=tool.file_to_copy_from_context("samples/simple.xml", prefix=False))
    assert out == 'Hello World\n'


def test_in_str():
    tool = dockertools.tool_with_file(__file__)
    c_file = tool.set_file_content('<test>This is a test </test>')
    out = tool.do_get_string(in_file=c_file)
    assert out == 'This is a test \n'
