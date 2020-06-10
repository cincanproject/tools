import os
import shutil

from contextlib import contextmanager

from metatool import dockertools
import pytest

SAMPLE_FILE="_samples/txt/attachments.eml"

def test_help(tool):
    out = tool.run_get_string([])
    assert out.startswith("usage: eml2json")

def test_parsing(tool, tmp_path):
    out = tool.run_get_string([SAMPLE_FILE])
    assert ".pdf" in out

def test_attachment_extract(tool, tmp_path):
    d = tmp_path / "eml_parser_tmp"
    d.mkdir()
    tool.output_dirs = [d.relative_to(os.getcwd())]
    out = tool.run_get_string([SAMPLE_FILE, "-e"])
    assert ".pdf" in out
    assert os.path.isfile("北京 2017年12月02-03日 销售主管 确认n.pdf")

@pytest.fixture(scope='function')
def tool(request):
    tool = dockertools.tool_with_file(__file__)
    yield tool

@pytest.fixture(scope="module", autouse=True)
def delete_temporary_files(request, tmp_path_factory):
    """Cleanup a testing directory once we are finished."""
    _tmp_path_factory = tmp_path_factory
    def cleanup():
        tmp_path = _tmp_path_factory.getbasetemp()
        if os.path.exists(tmp_path) and os.path.isdir(tmp_path):
            shutil.rmtree(tmp_path)
    request.addfinalizer(cleanup)
