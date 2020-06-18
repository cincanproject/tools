from testing import dockertools
import pytest

SAMPLE_FILE="samples/msoffice/very_suspicious.doc"

# NOTE: No tests for all tools yet. 

def test_entrypoint():
    tool = dockertools.tool_with_file(__file__)
    out = tool.run_get_string([])
    assert out.startswith("\n  This is shell script wrapper for oletools.\n")

def test_help():
    tool = dockertools.tool_with_file(__file__)
    out = tool.run_get_string(["--help"])
    assert out.startswith("\n  This is shell script wrapper for oletools.\n")

def test_olevba():
    tool = dockertools.tool_with_file(__file__)
    out = tool.run_get_string(["olevba", SAMPLE_FILE])
    assert out.endswith("|Executable file name                         |\n+----------+--------------------+---------------------------------------------+\n\n")

def test_oleid():
    tool = dockertools.tool_with_file(__file__)
    out = tool.run_get_string(["oleid", SAMPLE_FILE])
    assert out.endswith("\n Flash objects                  0                        \n\n")

def test_oledir():
    tool = dockertools.tool_with_file(__file__)
    out = tool.run_get_string(["oledir", SAMPLE_FILE])
    assert out.endswith("|WordDocument                |115310|                                      \n")

def test_olefile():
    tool = dockertools.tool_with_file(__file__)
    out = tool.run_get_string(["olefile", SAMPLE_FILE])
    assert out.endswith("This document may contain VBA macros.\n\nNon-fatal issues raised during parsing:\nNone\n")

def test_macroRaptor():
    tool = dockertools.tool_with_file(__file__)
    out = tool.run_get_string(["mraptor", SAMPLE_FILE])
    assert out.endswith("Exit code: 2 - Macro OK\n")
