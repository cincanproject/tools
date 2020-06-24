from metatool import dockertools


SAMPLE_FILE="_samples/pdf/ioc_test.pdf"

def test_entrypoint():
    tool = dockertools.tool_with_file(__file__)
    out = tool.run_get_string([])
    assert out.startswith("usage: iocextract [-h] [--input INPUT] [--output OUTPUT] [--extract-emails]")

def test_help():
    tool = dockertools.tool_with_file(__file__)
    out = tool.run_get_string(["--help"])
    assert out.startswith("usage: iocextract [-h] [--input INPUT] [--output OUTPUT] [--extract-emails]")

def test_sample_pdf():
    tool = dockertools.tool_with_file(__file__)
    tool.is_tty = True
    out = tool.run_get_string(["--input", SAMPLE_FILE])
    assert out.startswith("https://kasperskycontenthub.com/securelist/files/2015/05/grabit_us.png")

