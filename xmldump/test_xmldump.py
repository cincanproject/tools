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
    out = tool.do_get_string(in_file=tool.file_to_copy_from_context("samples/simple.xml", prefix=False))
    assert out == 'Hello World\n'


def test_in_str():
    tool = dockertools.tool_with_file(__file__)
    c_file = tool.set_file_content('<test>This is a test </test>')
    out = tool.do_get_string(in_file=c_file)
    assert out == 'This is a test \n'