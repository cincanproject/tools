import pathlib
import pytest
import shutil
from metatool import dockertools

SAMPLE_FILE="_samples/txt/hello.txt"

def test_help():
    tool = dockertools.tool_with_file(__file__)
    out = tool.run_get_string(['--help'])
    assert out.startswith('Usage: radamsa [arguments] [file ...]')


def test_fuzz_stdout():
    tool = dockertools.tool_with_file(__file__)
    out = tool.run_get_string(['-s', '110', '-n', '2', '-o', '-', SAMPLE_FILE])
    assert out == 'HelWorld!\nlo, World!\n'


def test_fuzz_file(tmp_path):
    d = tmp_path / "radamsa_tmp"
    d.mkdir()
    tool = dockertools.tool_with_file(__file__)
    dest_dir = d.relative_to(pathlib.Path.cwd())
    tool.output_dirs = [dest_dir / "fuzzed"]
    r = tool.run(['-s', '0', '-n', '10', '-o', f'{dest_dir}/fuzzed/%n', SAMPLE_FILE])
    assert r.exit_code == 0
    files = [p.as_posix() for p in sorted(pathlib.Path(d / "fuzzed").iterdir())]
    assert files == [
        f'{d}/fuzzed/1',
        f'{d}/fuzzed/10',
        f'{d}/fuzzed/2',
        f'{d}/fuzzed/3',
        f'{d}/fuzzed/4',
        f'{d}/fuzzed/5',
        f'{d}/fuzzed/6',
        f'{d}/fuzzed/7',
        f'{d}/fuzzed/8',
        f'{d}/fuzzed/9',
    ]

@pytest.fixture(scope="session", autouse=True)
def delete_temporary_files(request, tmp_path_factory):
    """Cleanup a testing directory once we are finished."""
    _tmp_path_factory = tmp_path_factory
    def cleanup():
        tmp_path = _tmp_path_factory.getbasetemp()
        if pathlib.Path(tmp_path).exists() and pathlib.Path(tmp_path).is_dir():
            shutil.rmtree(tmp_path)
    request.addfinalizer(cleanup)