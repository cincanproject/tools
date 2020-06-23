from testing import dockertools
from os import path, getcwd, path
import shutil
import pytest

SAMPLE_FILE = "samples/android_apk/selendroid-test-app.apk"

def test_help():
    tool = dockertools.tool_with_file(__file__)
    out = tool.run_get_string([])
    assert out.startswith("Apktool")

def test_apk_to_jar(tmp_path):
    d = tmp_path / "apk_tool"
    d.mkdir()
    tool = dockertools.tool_with_file(__file__)
    tool.output_dirs = [d.relative_to(getcwd())]
    out = tool.run_get_string(
        ["d", SAMPLE_FILE, "-f", "-o", f"{d.relative_to(getcwd())}"]
    )
    assert out.startswith("I: Using Apktool")
    assert out.endswith("Copying original files...\n")


@pytest.fixture(scope="session", autouse=True)
def delete_temporary_files(request, tmp_path_factory):
    """Cleanup a testing directory once we are finished."""
    _tmp_path_factory = tmp_path_factory

    def cleanup():
        tmp_path = _tmp_path_factory.getbasetemp()
        if path.exists(tmp_path) and path.isdir(tmp_path):
            shutil.rmtree(tmp_path)

    request.addfinalizer(cleanup)
