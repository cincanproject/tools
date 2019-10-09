import os

from metatool import dockertools


def test_echo():
    tool = dockertools.tool_with_file(__file__)
    out = tool.run_get_string(["echo HelloWorld"], preserve_image=True)
    assert out == "HelloWorld\n"


def test_mkdir_output():
    tool = dockertools.tool_with_file(__file__)
    out = tool.run_get_string(["cd ^^test_out_dir/; echo HelloWorldEnd > a.txt"], preserve_image=True)
    with open("test_out_dir/a.txt", "r") as f:
        out_data = f.read()
    os.unlink("test_out_dir/a.txt")
    os.rmdir("test_out_dir")
    assert out_data == "HelloWorldEnd\n"
