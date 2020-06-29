from testing import dockertools
from zipfile import ZipFile
import os
import shutil
import pytest

SAMPLE_FILE="samples/android_apk/selendroid-test-app.apk"

def test_help():
    tool = dockertools.tool_with_file(__file__)
    out = tool.run_get_string([])
    assert out.startswith("d2j-dex2jar")

def test_apk_to_jar(tmp_path):
    d = tmp_path / "dex2jar_tmp"
    d.mkdir()
    tool = dockertools.tool_with_file(__file__)
    output_d = d.relative_to(os.getcwd()) / "sample.jar"
    out = tool.run_get_string(args=[SAMPLE_FILE, "-o", str(output_d)])
    assert f"{output_d}" in out


@pytest.fixture(scope="session", autouse=True)
def delete_temporary_files(request, tmp_path_factory):
    """Cleanup a testing directory once we are finished."""
    _tmp_path_factory = tmp_path_factory

    def cleanup():
        tmp_path = _tmp_path_factory.getbasetemp()
        if os.path.exists(tmp_path) and os.path.isdir(tmp_path):
            shutil.rmtree(tmp_path)

    request.addfinalizer(cleanup)
