import dockertools


def test_image():
    tool = dockertools.ToolImage(path="tshark")
    out = tool.run_get_string(["-r", tool.file_to_copy("samples/ping_localhost.pcap"), "-c", "2", "-T", "json"])
    assert out == 'FIXME\n'
