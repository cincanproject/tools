from .. import dockertools


def test_image():
    tool = dockertools.ToolImage(path="xmldump")
    out = tool.run_get_string(["text", "^xmldump/samples/simple.xml"])
    assert out == 'Hello World\n'
