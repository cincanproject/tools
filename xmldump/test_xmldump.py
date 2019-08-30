import dockertools


def test_image():
    tool = dockertools.ToolImage(path="xmldump")
    out = tool.run_get_string(["text", tool.file_to_copy("samples/simple.xml")])
    assert out == 'Hello World\n'
