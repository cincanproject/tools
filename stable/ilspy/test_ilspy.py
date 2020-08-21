from testing import dockertools
from pathlib import Path
import pytest
import shutil
# Filepath relative to project root directory (expected location to call pytest)
SAMPLE_FILE="samples/msdos/suspicious_dos_sample.exe"
_tmp_path_factory = None

# Should be identical for testing '--help' argument
def test_entry_point():
    tool = dockertools.tool_with_file(__file__)
    out = tool.run_get_string([])
    assert out.startswith("dotnet tool for decompiling .NET assemblies and generating portable PDBs\n\nUsage: ilspycmd [arguments] [options]")

def test_help():
    tool = dockertools.tool_with_file(__file__)
    out = tool.run_get_string(["--help"])
    assert out.startswith("dotnet tool for decompiling .NET assemblies and generating portable PDBs\n\nUsage: ilspycmd [arguments] [options]")


def test_do_run_no_options_only_input_file():
    """Test decompiling without options, produces source code to STDOUT"""
    tool = dockertools.tool_with_file(__file__)
    out = tool.run_get_string(args=[f"{SAMPLE_FILE}"])
    assert out.startswith("using Microsoft.Win32;")
    assert out.endswith("ProcessWindowStyle.Hidden\n\t\t\t});\n\t\t}\n\t}\n}\n")

def test_do_run_get_PDB(tmp_path):
    """Test creating of PDB file"""
    d = tmp_path / "pdb"
    d.mkdir()
    tool = dockertools.tool_with_file(__file__)
    out = tool.run_get_string(args=["-o", f"{d.relative_to(Path.cwd())}/", "-genpdb", f"{SAMPLE_FILE}"])
    assert len(list(d.iterdir())) == 1
    assert Path(d / "suspicious_dos_sample.pdb").is_file()

def test_do_run_create_project(tmp_path):
    """Test creating of decompiled Visual Studio Project from binary"""
    d = tmp_path / "vsp"
    d.mkdir()
    tool = dockertools.tool_with_file(__file__)
    out = tool.run_get_string(args=["-o", f"{d.relative_to(Path.cwd())}/", "-p", f"{SAMPLE_FILE}"])
    assert len(list(d.iterdir())) == 3
    assert Path(d / "Innocent.csproj").is_file()

@pytest.fixture(scope="session", autouse=True)
def delete_temporary_files(request, tmp_path_factory):
    """Cleanup a testing directory once we are finished."""
    _tmp_path_factory = tmp_path_factory
    def cleanup():
        tmp_path = _tmp_path_factory.getbasetemp()
        if Path(tmp_path).exists() and Path(tmp_path).is_dir():
            shutil.rmtree(tmp_path)
    request.addfinalizer(cleanup)
