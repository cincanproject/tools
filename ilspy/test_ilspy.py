from metatool import dockertools
import json
import pytest

def test_help():
    tool = dockertools.tool_with_file(__file__)
    out = tool.run_get_string([])
    assert out.startswith("dotnet tool for decompiling .NET assemblies and generating portable PDBs\n\nUsage: ilspycmd [arguments] [options]")


def test_do_run():
    tool = dockertools.tool_with_file(__file__)

    out = tool.do_get_string(in_file=tool.file_to_copy_from_context("samples//ilspy_sample.exe", prefix=False),
                             out_type='application/string', args=["^in"])
    assert out.startswith("using Microsoft.Win32;")

    #out = tool.do_get_string(in_file=tool.file_to_copy_from_context("samples//ping_localhost.pcap", prefix=False),
    #                         out_type='text/xml', args=["-r", "^in", "-c", "2", "-Tpdml"])
    #assert out.startswith("<?xml")

    #with pytest.raises(Exception):
    #    tool.do_get_string(in_file=tool.file_to_copy_from_context("samples//ping_localhost.pcap", prefix=False),
    #                       args=[])
    #with pytest.raises(Exception):
    #    tool.do_get_string(in_file=tool.file_to_copy_from_context("samples//ping_localhost.pcap", prefix=False),
    #                       out_type='text/nosuch', args=[])