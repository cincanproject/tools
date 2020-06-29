from testing import dockertools

SAMPLE = 'samples/msdos/suspicious_dos_sample.exe'

def test_entrypoint():
    tool = dockertools.tool_with_file(__file__)
    out = tool.run_get_string([])
    assert out.startswith("Usage:")

def test_help():
    tool = dockertools.tool_with_file(__file__)
    out = tool.run_get_string(["--help"])
    assert out.startswith("Usage:")

def test_pe_sample():
    tool = dockertools.tool_with_file(__file__)
    out = tool.run_get_string(args=['--pe', SAMPLE])
    for i, line in enumerate(out.splitlines()):
        if i == 9:
            assert line.endswith("Subsystem:        IMAGE_SUBSYSTEM_WINDOWS_GUI")
        if i == 16:
            assert line.endswith("InternalName:     Innocent.exe")

    assert out.startswith('* Manalyze 0.9 *')
