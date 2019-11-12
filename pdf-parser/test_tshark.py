from metatool import dockertools
import json
import pytest


def test_help():
    tool = dockertools.tool_with_file(__file__)
    out = tool.run_get_string([])
    assert out.startswith('Usage: pdf-parser.py [options] pdf-file|zip-file|url')


def test_pdf():
    tool = dockertools.tool_with_file(__file__)
    out = tool.run_get_string(["-r", tool.file_to_copy_from_context("samples/ping_localhost.pcap"), "-c", "2", "-T", "json"])
    js = json.loads(out)
    assert js[0]['_source']['layers']['ip']['ip.src'] == '127.0.0.1'
    assert len(js) == 2


def test_hints():
    tool = dockertools.tool_with_file(__file__)
    hints = tool.resolve_commands().command_hints()
    assert "|".join(hints) == "-r ^file -Tjson|-r ^file -Tpdml"


def test_do_run():
    tool = dockertools.tool_with_file(__file__)

    out = tool.do_get_string(in_file=tool.file_to_copy_from_context("samples//ping_localhost.pcap", prefix=False),
                             out_type='application/json', args=["-r", "^in", "-c", "2", "-Tjson"])
    assert out.startswith("[")

    out = tool.do_get_string(in_file=tool.file_to_copy_from_context("samples//ping_localhost.pcap", prefix=False),
                             out_type='text/xml', args=["-r", "^in", "-c", "2", "-Tpdml"])
    assert out.startswith("<?xml")

    with pytest.raises(Exception):
        tool.do_get_string(in_file=tool.file_to_copy_from_context("samples//ping_localhost.pcap", prefix=False),
                           args=[])
    with pytest.raises(Exception):
        tool.do_get_string(in_file=tool.file_to_copy_from_context("samples//ping_localhost.pcap", prefix=False),
                           out_type='text/nosuch', args=[])
