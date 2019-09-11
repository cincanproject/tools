import dockertools
import json
import pytest


def test_help():
    tool = dockertools.ToolImage(path="tshark")
    out = tool.run_get_string([])
    assert out.startswith('TShark (Wireshark)')


def test_pcap_to_json():
    tool = dockertools.ToolImage(path="tshark")
    out = tool.run_get_string(["-r", tool.file_to_copy_from_context("samples/ping_localhost.pcap"), "-c", "2", "-T", "json"])
    js = json.loads(out)
    assert js[0]['_source']['layers']['ip']['ip.src'] == '127.0.0.1'
    assert len(js) == 2


def test_hints():
    tool = dockertools.ToolImage(path="tshark")
    hints = tool.list_command_line()
    assert "|".join(hints) == "-r ^<file> -Tjson|-r ^<file> -Tpdml"


def test_do_run():
    tool = dockertools.ToolImage(path="tshark")

    out = tool.do_get_string(in_file=tool.file_to_copy_from_context("samples//ping_localhost.pcap", prefix=False),
                             out_type='application/json', args=["-c", "2"])
    assert out.startswith("[")

    out = tool.do_get_string(in_file=tool.file_to_copy_from_context("samples//ping_localhost.pcap", prefix=False),
                             out_type='text/xml', args=["-c", "2"])
    assert out.startswith("<?xml")

    with pytest.raises(Exception):
        tool.do_get_string(in_file=tool.file_to_copy_from_context("samples//ping_localhost.pcap", prefix=False),
                           args=["-c", "2"])
    with pytest.raises(Exception):
        tool.do_get_string(in_file=tool.file_to_copy_from_context("samples//ping_localhost.pcap", prefix=False),
                           out_type='text/nosuch', args=["-c", "2"])
