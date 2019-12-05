from metatool import dockertools
import json
import pytest

SAMPLE_FILE="_samples/pcap/ping_localhost.pcap"

def test_help():
    tool = dockertools.tool_with_file(__file__)
    out = tool.run_get_string([])
    assert out.startswith('TShark (Wireshark)')

def test_pcap_to_json():
    tool = dockertools.tool_with_file(__file__)
    out = tool.run_get_string(["-r", SAMPLE_FILE, "-c", "2", "-T", "json"])
    js = json.loads(out)
    assert js[0]['_source']['layers']['ip']['ip.src'] == '127.0.0.1'
    assert len(js) == 2


def test_do_run():
    tool = dockertools.tool_with_file(__file__)

    out = tool.run_get_string(
        ["-r", SAMPLE_FILE, "-c", "2", "-Tjson"])
    assert out.startswith("[")

    out = tool.run_get_string(
        ["-r", SAMPLE_FILE, "-c", "2", "-Tpdml"])
    assert out.startswith("<?xml")

    res = tool.run(["-r", "nosuchfile.pcap", "-c", "2", "-Tpdml"])
    assert res.exit_code != 0