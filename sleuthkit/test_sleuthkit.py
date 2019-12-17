from metatool import dockertools
import pytest

SAMPLE_FILE="_samples/disks/7-ntfs-undel.dd"

def test_tools_help(tool):
    out = tool.run_get_string(["help"])
    assert "fsstat" in out
    assert "fls" in out

def test_fsstat(tool):
    out = tool.run_get_string(["fsstat", SAMPLE_FILE])
    assert "285C576D5C5734B2" in out
    assert "NTFS_DEL" in out
    assert "First Cluster of MFT: 2005" in out
    assert "Sector Size: 512" in out

def test_blkstat(tool):
    out = tool.run_get_string(["blkstat", SAMPLE_FILE, "3"])
    assert "Allocated" in out

def test_ils(tool):
    out = tool.run_get_string(["ils", SAMPLE_FILE])
    assert "29|f|0|0|1078084840|1078084840|1078084840|1078084817|777|1|1584" in out
 
def test_fls_deleted_entries(tool):
    tool = dockertools.tool_with_file(__file__)
    out = tool.run_get_string(["fls", "-d", SAMPLE_FILE])
    assert "frag1.dat" in out
    assert "mult1.dat" in out
    assert "dir1" in out

@pytest.fixture(scope='function')
def tool(request):
    tool = dockertools.tool_with_file(__file__)
    yield tool

