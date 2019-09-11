import dockertools


def test_no_args_error():
    tool = dockertools.ToolImage(path="r2-callgraph/v0.1")
    out = tool.run_get_string([])
    assert out.startswith("[r] Cannot open '/io/binary")
