import os
import tarfile

from metatool import dockertools


def test_echo():
    tool = dockertools.tool_with_file(__file__)
    out = tool.run_get_string(["echo HelloWorld"])
    assert out == "HelloWorld\n"


def test_do_cat():
    tool = dockertools.tool_with_file(__file__)
    tool.output_tar = "test_output.tar"
    tool.do_get_string(args=["cat ^test2tool/samples/file.txt"])
    with tarfile.open(tool.output_tar) as tar:
        out = tar.extractfile("stdout").read()
    os.unlink(tool.output_tar)
    assert out == b"Just a file\n"


def test_mkdir_output():
    tool = dockertools.tool_with_file(__file__)
    out = tool.run_get_string(["cd ^^test_out_dir/; echo HelloWorldEnd > a.txt"])
    with open("test_out_dir/a.txt", "r") as f:
        out_data = f.read()
    os.unlink("test_out_dir/a.txt")
    os.rmdir("test_out_dir")
    assert out_data == "HelloWorldEnd\n"
