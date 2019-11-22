from metatool import dockertools

def test_help():
    tool = dockertools.tool_with_file(__file__)
    out = tool.run_get_string([])
    assert out.startswith("Usage: \n\t./jsunpackn.py [fileName")

def test_with_pdf():
    tool = dockertools.tool_with_file(__file__)
    out = tool.run_get_string([tool.file_to_copy_from_context("samples/testfile.pdf"), "-V"])
    assert "decoding_530752faa103f6929a7f067eee4088517970e6a9" in out.splitlines()[3]

