import os
import zipfile
from metatool import dockertools

SAMPLE = '_samples/memory/Win7SP1x86_23418.raw'

def test_entry_point():
    tool = dockertools.tool_with_file(__file__)
    out = tool.run_get_string([])
    assert out.startswith('Usage: Volatility - A memory forensics analysis platform.')


def test_help():
    tool = dockertools.tool_with_file(__file__)
    out = tool.run_get_string(['--help'])
    assert out.startswith('Usage: Volatility - A memory forensics analysis platform.')


def test_do_kdbgscan():
    with zipfile.ZipFile(SAMPLE + '.zip', 'r') as f:
        f.extractall('_samples/memory/')
    tool = dockertools.tool_with_file(__file__)

    out = tool.run_get_string(['kdbgscan', '-f', SAMPLE])
    os.remove(SAMPLE)
    assert out.startswith('**************************************************\n'
    'Instantiating KDBG using:')
