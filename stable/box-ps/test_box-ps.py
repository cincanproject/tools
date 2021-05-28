import os
import shutil

from testing import dockertools
import pytest

SAMPLE_FILE="samples/source/powershell/hello.ps1"

def test_entrypoint():
    tool = dockertools.tool_with_file(__file__)
    out = tool.run_get_string([])
    assert out.replace('\r', '').startswith("[-] must give either script contents or input file\n")


def test_encodedbinary_deobfuscation(tmp_path, tool):
    d = tmp_path / "box-ps"
    d.mkdir()
    tool.output_dirs = [d.relative_to(os.getcwd())]

    output_dir = d.relative_to(os.getcwd()) / "test"
    report = output_dir / 'report.json'
    stdout_txt = output_dir / 'stdout.txt'

    out = tool.run_get_string(["-InFile", SAMPLE_FILE, "-OutDir", str(output_dir)])
    assert os.path.isfile(report)
    assert os.path.isfile(stdout_txt)

    with report.open() as report_json:
        assert "Hello from CinCan" in report_json.read()

    with stdout_txt.open() as stdout:
        assert "Hello from CinCan" in stdout.read()

@pytest.fixture(scope='function')
def tool(request):
    tool = dockertools.tool_with_file(__file__)
    yield tool

@pytest.fixture(scope="session", autouse=True)
def delete_temporary_files(request, tmp_path_factory):
    """Cleanup a testing directory once we are finished."""
    _tmp_path_factory = tmp_path_factory
    def cleanup():
        tmp_path = _tmp_path_factory.getbasetemp()
        if os.path.exists(tmp_path) and os.path.isdir(tmp_path):
            shutil.rmtree(tmp_path)
    request.addfinalizer(cleanup)
