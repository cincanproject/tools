from .. import dockertools
import re

pattern = re.compile("^\\s*(\\S+)\\s+(\\S.*)$")


def test_image():
    tool = dockertools.ToolImage(path="pdfid")
    out = tool.run_get_string([tool.file_to_copy("samples/text_txt.pdf")])
    values = {}
    for line in out.splitlines():
        m = re.match(pattern, line)
        if m is not None:
            print("X: {}({})".format(m.group(1), m.group(2)))
            values[m.group(1)] = m.group(2)
    assert values['obj'] == '13'
    assert values['endobj'] == '13'
    assert values['stream'] == '2'
    assert values['xref'] == '1'
