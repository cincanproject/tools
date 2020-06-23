from testing import dockertools
import pytest
import shutil
import json
import os

# Use same sample file than ilspy is using
SAMPLE_FILE = "samples/msdos/suspicious_dos_sample.exe"

# Should be identical for adding '--help' argument.


def test_entrypoint_and_build():
    """This method just builds the image and checks the output without arguments.
    Later methods should use same build image."""
    tool = dockertools.tool_with_file(__file__)
    out = tool.run_get_string([])
    assert out.strip().startswith("Clam AntiVirus: Scanner")
    assert out.strip().endswith(
        "files inside. The above options ensure safe processing of this kind of data."
    )


def test_help():
    tool = dockertools.tool_with_file(__file__)
    out = tool.run_get_string(["--help"])
    assert out.strip().startswith("Clam AntiVirus: Scanner")
    assert out.strip().endswith(
        "files inside. The above options ensure safe processing of this kind of data."
    )


@pytest.mark.slow
def test_do_run_get_tmp_json(tmp_path):
    """Test creating of JSON file from test results. Does not work for all files."""
    d = tmp_path / "clamav_tmp"
    d.mkdir()
    tool = dockertools.tool_with_file(__file__)
    out = tool.run_get_string(
        args=[
            "--gen-json",
            "--leave-temps",
            f"--tempdir={d.relative_to(os.getcwd())}/",
            f"{SAMPLE_FILE}",
        ]
    )
    # Get files
    files = [x for x in d.iterdir() if x.is_file()]

    assert len(files) == 1
    with open(files[0]) as jsonfile:
        j_obj = json.load(jsonfile)
        # ClamAV calculates MDF5 of sample file, let's check it...
        assert j_obj.get("FileMD5") == "c14fe9dbd952233ed549687374d765ec"


@pytest.fixture(scope="session", autouse=True)
def delete_temporary_files(request, tmp_path_factory):
    """Cleanup a testing directory once we are finished."""
    _tmp_path_factory = tmp_path_factory

    def cleanup():
        tmp_path = _tmp_path_factory.getbasetemp()
        if os.path.exists(tmp_path) and os.path.isdir(tmp_path):
            shutil.rmtree(tmp_path)

    request.addfinalizer(cleanup)
