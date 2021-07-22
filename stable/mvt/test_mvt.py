from testing import dockertools
import pytest
import shutil
import json
import os

SAMPLE_FILE = ""

# Should be identical for adding '--help' argument.

def test_entrypoint_and_build():
    """This method just builds the image and checks the output without arguments.
    Later methods should use same build image."""
    tool = dockertools.tool_with_file(__file__)
    out = tool.run_get_string([])
    assert out.strip().startswith("This is unofficial shell script wrapper for Mobile Verification Toolkit to be used in Docker container.")

mvt_ios_h = """Usage: mvt-ios [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  check-backup    Extract artifacts from an iTunes backup
  check-fs        Extract artifacts from a full filesystem dump
  check-iocs      Compare stored JSON results to provided indicators
  decrypt-backup  Decrypt an encrypted iTunes backup"""
  

def test_mvt_ios_help():
    tool = dockertools.tool_with_file(__file__)
    out = tool.run_get_string(["mvt-ios", "--help"])
    assert out.strip().startswith(mvt_ios_h)

mvt_android_h = """Usage: mvt-android [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  check-adb      Check an Android device over adb
  check-backup   Check an Android Backup
  download-apks  Download all or non-safelisted installed APKs installed..."""

def test_mvt_ios_help():
    tool = dockertools.tool_with_file(__file__)
    out = tool.run_get_string(["mvt-android", "--help"])
    assert out.strip().startswith(mvt_android_h)

@pytest.fixture(scope="session", autouse=True)
def delete_temporary_files(request, tmp_path_factory):
    """Cleanup a testing directory once we are finished."""
    _tmp_path_factory = tmp_path_factory

    def cleanup():
        tmp_path = _tmp_path_factory.getbasetemp()
        if os.path.exists(tmp_path) and os.path.isdir(tmp_path):
            shutil.rmtree(tmp_path)

    request.addfinalizer(cleanup)

