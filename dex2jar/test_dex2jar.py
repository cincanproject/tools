from metatool import dockertools
from zipfile import ZipFile
import pytest

SAMPLE_FILE="_samples/android_apk/selendroid-test-app.apk"

@pytest.mark.dev
def test_help():
    tool = dockertools.tool_with_file(__file__)
    out = tool.run_get_string([])
    assert out.startswith("d2j-dex2jar")

@pytest.mark.dev
def test_apk_to_jar():
    tool = dockertools.tool_with_file(__file__)
    out = tool.run_get_string([tool.file_to_copy_from_context("samples/selendroid-test-app.apk")])
    assert "./selendroid-test-app-dex2jar.jar" in out