from testing import dockertools

SAMPLE_FILE="samples/source/c/overflow.c"


default_opts = """
flawfinder [--help | -h] [--version] [--listrules]
  [--allowlink] [--followdotdir] [--nolink]
           [--patch filename | -P filename]
  [--inputs | -I] [--minlevel X | -m X]
           [--falsepositive | -F] [--neverignore | -n]
  [--context | -c] [--columns | -C] [--dataonly | -D]
           [--html | -H] [--immediate | -i] [--singleline | -S]
           [--omittime] [--quiet | -Q]
  [--loadhitlist F] [--savehitlist F] [--diffhitlist F]
  [--] [source code file or source root directory]+

  The options cover various aspects of flawfinder as follows.
"""

def test_entrypoint():
    tool = dockertools.tool_with_file(__file__)
    out = tool.run_get_string([])
    assert out.startswith(default_opts)

def test_help():
    tool = dockertools.tool_with_file(__file__)
    out = tool.run_get_string(["--help"])
    assert out.startswith(default_opts)

def test_analysis():
    tool = dockertools.tool_with_file(__file__)
    out = tool.run_get_string([SAMPLE_FILE])
    for i, line in enumerate(out.splitlines()):
        if i == 1:
            assert line.startswith("Number of rules (primarily dangerous function names) in C/C++ ruleset: 222")
        if i == 6:
            assert line.startswith("samples/source/c/overflow.c:7:  [4] (buffer) strcpy:")
