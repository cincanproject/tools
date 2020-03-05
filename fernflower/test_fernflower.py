from metatool import dockertools
import pytest
import os
import shutil

SAMPLE_FILE="_samples/android_apk/selendroid-test-app-dex2jar.jar"

def test_tools_help(tool):
    out = tool.run_get_string([])
    assert "Usage: java -jar fernflower.jar" in out

def test_decompile(tmp_path, tool):
    d = tmp_path / "fernflower_tmp"
    d.mkdir()
    tool.output_dirs = [d.relative_to(os.getcwd())]
    out = tool.run_get_string([SAMPLE_FILE, str(d.relative_to(os.getcwd()))])
    assert "Decompiling class org/apache/commons/io/output/XmlStreamWriter" in out
    decompiled = d.relative_to(os.getcwd()) / "selendroid-test-app-dex2jar.jar"
    assert os.path.isfile(decompiled)

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

