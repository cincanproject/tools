from .. import dockertools


def test_image():
    tool = dockertools.ToolImage("tshark")
    out = tool.run_get_string(["-r", "^tshark/samples/ping_localhost.pcap", "-c", "2", "-T", "json"])
    assert out == 'FIXME\n'
