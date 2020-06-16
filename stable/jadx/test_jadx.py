from os import path, getcwd
import shutil
import pytest
from metatool import dockertools
from pathlib import Path

SAMPLE_FILE="_samples/android_apk/selendroid-test-app-dex2jar.jar"

def test_help():
    tool = dockertools.tool_with_file(__file__)
    out = tool.run_get_string(["-h"])
    assert out.replace('\r', '').startswith("\njadx")


def test_decompile_jar(tmp_path):
    """Test decompiling jar file"""
    d = tmp_path / "jadx_tool"
    d.mkdir
    tool = dockertools.tool_with_file(__file__)
    tool.output_dirs = [d.relative_to(getcwd())]
    out = tool.run_get_string([SAMPLE_FILE, "-d", f"{d.relative_to(getcwd()) / 'selendroid-test.zip'}"])
    assert Path(d / "selendroid-test.zip").is_dir()


@pytest.fixture(scope="session", autouse=True)
def delete_temporary_files(request, tmp_path_factory):
    """Cleanup a testing directory once we are finished."""
    _tmp_path_factory = tmp_path_factory
    def cleanup():
        tmp_path = _tmp_path_factory.getbasetemp()
        if path.exists(tmp_path) and path.isdir(tmp_path):
            shutil.rmtree(tmp_path)
    request.addfinalizer(cleanup)
