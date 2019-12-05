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


def test_fuzz_file():
    tool = dockertools.tool_with_file(__file__)
    tool.output_dirs = ['_tests/fuzzed']
    r = tool.run(['-s', '0', '-n', '10', '-o', '_tests/fuzzed/%n', 'radamsa/samples/hello.txt'])
    assert r.exit_code == 0
    files = [p.as_posix() for p in sorted(pathlib.Path('_tests/fuzzed').iterdir())]
    assert files == [
        '_tests/fuzzed/1',
        '_tests/fuzzed/10',
        '_tests/fuzzed/2',
        '_tests/fuzzed/3',
        '_tests/fuzzed/4',
        '_tests/fuzzed/5',
        '_tests/fuzzed/6',
        '_tests/fuzzed/7',
        '_tests/fuzzed/8',
        '_tests/fuzzed/9',
    ]
