from metatool import dockertools

def test_help():
    tool = dockertools.tool_with_file(__file__)
    out = tool.run_get_string([])
    assert out.startswith("Usage: peepdf.py [options] PDF_file")

def test_with_pdf():
    tool = dockertools.tool_with_file(__file__)
    out = tool.run_get_string([tool.file_to_copy_from_context("samples//testfile.pdf"), "-f", "-C", "js_beautify object 7"])
    assert "CinCan" in out.splitlines()[10]

