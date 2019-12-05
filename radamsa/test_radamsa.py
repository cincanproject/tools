import pathlib

from metatool import dockertools


def test_help():
    tool = dockertools.tool_with_file(__file__)
    out = tool.run_get_string(['--help'])
    assert out.startswith('Usage: radamsa [arguments] [file ...]')


def test_fuzz_stdout():
    tool = dockertools.tool_with_file(__file__)
    out = tool.run_get_string(['-s', '110', '-n', '2', '-o', '-', 'radamsa/samples/hello.txt'])
    assert out == 'HelWorld!\nlo, World!\n'
