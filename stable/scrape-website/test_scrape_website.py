from testing import dockertools
import pytest
import shutil
import glob
import os
import json

help_out ="""usage: scrape-website.js [-h] [--version] [--delay DELAY]
                         [--process-timeout PROCESS_TIMEOUT]
                         [--resolution RESOLUTION] [--full-screenshot]
                         [--output-har] [--output-png] [--url URL]
                         [--url-file URL_FILE] [-o OUTPUT_DIR]
                         [--user-agent USER_AGENT]
                         [--chromium-args CHROMIUM_ARGS] [--tcpdump]
                         [--tcpdump-args TCPDUMP_ARGS]
                         [--crawl-depth CRAWL_DEPTH] [--json]
"""
def test_entrypoint():
    tool = dockertools.tool_with_file(__file__)
    out = tool.run_get_string([])
    assert out.startswith(help_out)

def test_help():
    tool = dockertools.tool_with_file(__file__)
    out = tool.run_get_string(["--help"])
    assert out.startswith(help_out)

def test_url_as_argument(tmp_dir):
    relative_path = tmp_dir.relative_to(os.getcwd())
    tool = dockertools.tool_with_file(__file__)
    tool.output_dirs = [relative_path]
    out = tool.run_get_string(["--url", "https://example.com", "--output-dir", f"{relative_path}"])
    print(out)
    pngs = list(tmp_dir.glob('**/*.png'))
    hars = list(tmp_dir.glob('**/*.har'))
    print(hars)
    assert "https://example.com" in out
    assert os.path.getsize(pngs[0]) > 0
    assert os.path.getsize(hars[0]) > 0
    with open(hars[0], "r") as har_json:
        har = json.load(har_json)
        assert "<h1>Example Domain</h1>" in har['log']['entries'][0]['response']['content']['text']

@pytest.fixture(scope="function")
def tmp_dir(tmp_path):
    d = tmp_path / "scrape-website"
    d.mkdir()
    return d

@pytest.fixture(scope="session", autouse=True)
def delete_temporary_files(request, tmp_path_factory):
    """Cleanup a testing directory once we are finished."""
    _tmp_path_factory = tmp_path_factory
    def cleanup():
        tmp_path = _tmp_path_factory.getbasetemp()
        if os.path.exists(tmp_path) and os.path.isdir(tmp_path):
            shutil.rmtree(tmp_path)
    request.addfinalizer(cleanup)
