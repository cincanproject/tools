import dockertools
import re

pattern = re.compile("^\\s*(\\S+)\\s+(\\S+)\\s+(\\S+)\\s+(\\S+)\\s+(\\S+)\\s*$")


def test_image():
    tool = dockertools.ToolImage(path="pdf-tools")
    out = tool.run(["python", "base64dump.py", tool.file_to_copy("samples/text_txt.pdf")]).decode('utf8')
    values = []
    for line in out.splitlines():
        m = re.match(pattern, line)
        if m is not None:
            # print("{} {} {}".format(m.group(1), m.group(3), m.group(5)))
            values.append((m.group(1), m.group(3), m.group(5)))
    assert values[1][0] == '1:'
    assert values[1][1] == 'R/Filter'
    assert values[1][2] == '8e306826ca2c662dc71e92c6bf8eaef5'
    assert values[2][0] == '2:'
    assert values[3][0] == '3:'
