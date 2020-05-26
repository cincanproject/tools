import lzma
import os
from os.path import basename
import shutil

from contextlib import contextmanager

from pathlib import Path
from tempfile import mktemp

from metatool import dockertools
import pytest

def test_help():
    tool = dockertools.tool_with_file(__file__)
    out = tool.run_get_string([])
    assert out.startswith("usage: eml2json")

def test_samparse_plugin(mail):
    tool = dockertools.tool_with_file(__file__)
    tool.output_dirs = [mail.relative_to(os.getcwd())]
    out = tool.run_get_string([str(mail)])
    assert "北京 2017年12月02-03日 销售主管 确认n.pdf" in out

@pytest.fixture(scope="module", autouse=True)
def delete_temporary_files(request, tmp_path_factory):
    """Cleanup a testing directory once we are finished."""
    _tmp_path_factory = tmp_path_factory
    def cleanup():
        tmp_path = _tmp_path_factory.getbasetemp()
        if os.path.exists(tmp_path) and os.path.isdir(tmp_path):
            shutil.rmtree(tmp_path)
    request.addfinalizer(cleanup)
