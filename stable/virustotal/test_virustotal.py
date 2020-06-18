from testing import dockertools
import pytest


SAMPLE_FILE1="virustotal/samples/url_example.txt"
OUTPUT_FOLDER="virustotal/samples/"
SAMPLE_FILE2="virustotal/samples/hash_example.txt"

def test_help():
    tool = dockertools.tool_with_file(__file__)
    out = tool.run_get_string([])
    assert out.startswith("usage: virustotal.py [-h] [-v] [--send] --output OUTPUT [--config CONFIG]")

def test_input_url_no_APIkey():
    """Test sending url_example.txt without API key to virustotal"""
    tool = dockertools.tool_with_file(__file__)
    out = tool.run_get_string(args=["--url_file", f"{SAMPLE_FILE1}", "-o", f"{OUTPUT_FOLDER}/"])
    assert out.startswith("Empty api key file")
