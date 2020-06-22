from metatool import dockertools

SAMPLE_FILE="_samples/source/c/overflow.c"

def test_help():
    tool = dockertools.tool_with_file(__file__)
    out = tool.run_get_string([])
    assert out.startswith("Flawfinder version")

def test_analysis():
    tool = dockertools.tool_with_file(__file__)
    out = tool.run_get_string([SAMPLE_FILE])
    for i, line in enumerate(out.splitlines()):
        if i == 1:
            assert line.startswith("Number of rules (primarily dangerous function names) in C/C++ ruleset: 223")
        if i == 6:
            assert line.startswith("_samples/source/c/overflow.c:7:  [4] (buffer) strcpy:")
