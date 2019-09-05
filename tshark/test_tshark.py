import dockertools
import json


def test_image():
    tool = dockertools.ToolImage(path="tshark")
    out = tool.run_get_string(["-r", tool.file_to_copy("samples/ping_localhost.pcap"), "-c", "2", "-T", "json"])
    js = json.loads(out)
    assert js[0]['_index'] == 'packets-2019-09-05'
    assert js[0]['_source']['layers']['ip']['ip.src'] == '127.0.0.1'
    assert len(js) == 2


def test_hints():
    tool = dockertools.ToolImage(path="tshark")
    hints = tool.list_command_line()
    assert "|".join(hints) == "-r ^<file> -Tjson|-r ^<file> -Tpdml"
