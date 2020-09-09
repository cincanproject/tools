import lzma
import os
from os.path import basename
import shutil

from contextlib import contextmanager

from pathlib import Path
from tempfile import mktemp

from testing import dockertools
import pytest

def test_help():
    tool = dockertools.tool_with_file(__file__)
    out = tool.run_get_string([])
    assert out.startswith("Rip v.2.8")

def test_samparse_plugin(sam_hive):
    tool = dockertools.tool_with_file(__file__)
    tool.output_dirs = [sam_hive.relative_to(os.getcwd())]
    out = tool.run_get_string(["-r", str(sam_hive), "-p", "samparse"])
    assert out.startswith("samparse v.20160203")
    assert "S-1-5-21-3583694148-1414552638-2922671848-500" in out
    assert "S-1-5-21-3583694148-1414552638-2922671848-501" in out
    assert "S-1-5-21-3583694148-1414552638-2922671848-1000" in out

def test_product_plugin(software_hive):
    tool = dockertools.tool_with_file(__file__)
    tool.output_dirs = [software_hive.relative_to(os.getcwd())]
    out = tool.run_get_string(["-r", str(software_hive), "-p", "product"])
    assert "Microsoft .NET Framework 4.7 v.4.7.02053, 20180102" in out
    assert "Microsoft Silverlight v.5.1.50907.0, 20180102" in out

def test_winver_plugin(software_hive):
    tool = dockertools.tool_with_file(__file__)
    tool.output_dirs = [software_hive.relative_to(os.getcwd())]
    out = tool.run_get_string(["-r", str(software_hive), "-p", "winver"])
    assert "ProductName = Windows 7 Enterprise" in out
    assert "CSDVersion  = Service Pack 1" in out
    assert "InstallDate = Wed Jan  3 01:21:25 2018" in out

def extract_lzma(tmp_path, path):
    tmp_file = tmp_path / basename(path)
    with open(tmp_file, 'wb') as tmp:
        with lzma.open(path) as f:
            tmp.write(f.read())
    return tmp_file

@pytest.fixture(scope='function')
def test_data_dir():
    return Path('samples/msdos/')

@pytest.fixture(scope='function')
def sam_hive(tmp_path, test_data_dir):
    temp_file = extract_lzma(tmp_path, test_data_dir / 'SAM.xz')
    yield temp_file

@pytest.fixture(scope='function')
def software_hive(tmp_path, test_data_dir):
    temp_path = extract_lzma(tmp_path, test_data_dir / 'SOFTWARE.xz')
    yield temp_path

@pytest.fixture(scope="module", autouse=True)
def delete_temporary_files(request, tmp_path_factory):
    """Cleanup a testing directory once we are finished."""
    _tmp_path_factory = tmp_path_factory
    def cleanup():
        tmp_path = _tmp_path_factory.getbasetemp()
        if os.path.exists(tmp_path) and os.path.isdir(tmp_path):
            shutil.rmtree(tmp_path)
    request.addfinalizer(cleanup)
