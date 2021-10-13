from testing import dockertools

SAMPLE_FILE = "samples/amd64/hello_world_r2"


def test_entrypoint():
    tool = dockertools.tool_with_file(__file__)
    out = tool.run_get_string([])
    assert out.startswith("\n  This is shell script wrapper for radare2.\n")


def test_help():
    tool = dockertools.tool_with_file(__file__)
    out = tool.run_get_string(["--help"])
    assert out.startswith("\n  This is shell script wrapper for radare2.\n")


def test_r2():
    tool = dockertools.tool_with_file(__file__)
    out = tool.run_get_string(["r2", "-h"])
    assert out.startswith("Usage: r2 [-ACdfLMnNqStuvwzX] [-P patch] ")


def test_radare2():
    tool = dockertools.tool_with_file(__file__)
    out = tool.run_get_string(["radare2", "-h"])
    assert out.startswith("Usage: r2 [-ACdfLMnNqStuvwzX] [-P patch] ")


def test_r2pm():
    tool = dockertools.tool_with_file(__file__)
    out = tool.run_get_string(["r2pm", "-h"])
    assert out.startswith("Usage: r2pm [init|update|cmd] [...]")


def test_rabin2():
    tool = dockertools.tool_with_file(__file__)
    out = tool.run_get_string(["rabin2", "-h"])
    assert out.startswith("Usage: rabin2 [-AcdeEghHiIjlLMqrRsSUvVxzZ]")


def test_radiff2():
    tool = dockertools.tool_with_file(__file__)
    out = tool.run_get_string(["radiff2", "-h"])
    assert out.startswith("Usage: radiff2 [-abBcCdeGhijnrOpqsSxuUvVzZ]")


def test_rafind2():
    tool = dockertools.tool_with_file(__file__)
    out = tool.run_get_string(["rafind2", "-h"])
    assert out.startswith("Usage: rafind2 [-mXnzZhqv] ")


def test_ragg2():
    tool = dockertools.tool_with_file(__file__)
    out = tool.run_get_string(["ragg2", "-h"])
    assert out.startswith("Usage: ragg2 [-FOLsrxhvz] ")


def test_rahash2():
    tool = dockertools.tool_with_file(__file__)
    out = tool.run_get_string(["rahash2", "-h"])
    assert out.startswith("Usage: rahash2 [-BhjkLqrv]")


def test_rarun2():
    tool = dockertools.tool_with_file(__file__)
    out = tool.run_get_string(["rarun2", "-h"])
    assert out.startswith("Usage: rarun2 -v|-t|script.rr2 [directive ..]")


def test_rasm2():
    tool = dockertools.tool_with_file(__file__)
    out = tool.run_get_string(["rasm2", "-h"])
    assert out.startswith("Usage: rasm2 [-ACdDehLBvw] [-a arch] ")


def test_rax2():
    tool = dockertools.tool_with_file(__file__)
    out = tool.run_get_string(["rax2", "-h"])
    assert out.startswith("Usage: rax2 [options] [expr ...]")


pdf_out = """            ; DATA XREF from entry0 @ 0x1061
/ 35: int main (int argc, char **argv, char **envp);
|           0x00001139      55             push rbp
|           0x0000113a      4889e5         mov rbp, rsp
|           0x0000113d      488d3dc40e00.  lea rdi, str.Hello__World_  ; 0x2008 ; "Hello, World!" ; const char *s
|           0x00001144      e8e7feffff     call sym.imp.puts           ; int puts(const char *s)
|           0x00001149      488d3dc80e00.  lea rdi, str.And_Hello_for_radare2_as_well_ ; 0x2018 ; "And Hello for radare2 as well!" ; const char *s
|           0x00001150      e8dbfeffff     call sym.imp.puts           ; int puts(const char *s)
|           0x00001155      b800000000     mov eax, 0
|           0x0000115a      5d             pop rbp
\\           0x0000115b      c3             ret
\x1b[2K\r"""

def test_simple_inline_analysis():
    tool = dockertools.tool_with_file(__file__)
    out = tool.run_get_string(["r2", "-e", "bin.cache=true", "-e", "scr.color=0", "-Aqc", "pdf @main", SAMPLE_FILE])
    print(out)
    assert out.endswith(pdf_out)


def test_grapscript_no_args_error():
    tool = dockertools.tool_with_file(__file__)
    out = tool.run_get_string(["script", "r2_callgraph.sh"])
    assert out.startswith("No sample directory provided. ")
# No color parameter not working at the moment - no output at all
ghidra_out = """\n\x1b[34mundefined8\x1b[0m \x1b[31mmain\x1b[0m(\x1b[1;95mvoid\x1b[0m)\n\n{\n    \x1b[31msym.imp.puts\x1b[0m(\x1b[33m"Hello, World!"\x1b[0m);\n    \x1b[31msym.imp.puts\x1b[0m(\x1b[33m"And Hello for radare2 as well!"\x1b[0m);\n    \x1b[1;95mreturn\x1b[0m \x1b[33m0\x1b[0m;\n}\n\x1b[2K\r"""

def test_ghidra_plugin():
    tool = dockertools.tool_with_file(__file__)
    out = tool.run_get_string(["r2", "-e", "bin.cache=true", "-Aqc", "pdg @main", SAMPLE_FILE])
    assert out.endswith(ghidra_out)

