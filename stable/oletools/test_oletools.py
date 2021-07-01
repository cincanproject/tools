from testing import dockertools
import pytest

SAMPLE_FILE="samples/msoffice/very_suspicious.doc"

# NOTE: No tests for all tools yet. 

OLEID_OUT = """
Filename: samples/msoffice/very_suspicious.doc
--------------------+--------------------+----------+--------------------------
Indicator           |Value               |Risk      |Description               
--------------------+--------------------+----------+--------------------------
File format         |MS Word 97-2003     |info      |                          
                    |Document or Template|          |                          
--------------------+--------------------+----------+--------------------------
Container format    |OLE                 |info      |Container type            
--------------------+--------------------+----------+--------------------------
Application name    |Microsoft Office    |info      |Application name declared 
                    |Word                |          |in properties             
--------------------+--------------------+----------+--------------------------
Properties code page|1252: ANSI Latin 1; |info      |Code page used for        
                    |Western European    |          |properties                
                    |(Windows)           |          |                          
--------------------+--------------------+----------+--------------------------
Author              |Mallory             |info      |Author declared in        
                    |                    |          |properties                
--------------------+--------------------+----------+--------------------------
Encrypted           |False               |none      |The file is not encrypted 
--------------------+--------------------+----------+--------------------------
VBA Macros          |Yes                 |Medium    |This file contains VBA    
                    |                    |          |macros. No suspicious     
                    |                    |          |keyword was found. Use    
                    |                    |          |olevba and mraptor for    
                    |                    |          |more info.                
--------------------+--------------------+----------+--------------------------
XLM Macros          |No                  |none      |This file does not contain
                    |                    |          |Excel 4/XLM macros.       
--------------------+--------------------+----------+--------------------------
External            |0                   |none      |External relationships    
Relationships       |                    |          |such as remote templates, 
                    |                    |          |remote OLE objects, etc   
--------------------+--------------------+----------+--------------------------
"""

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
    assert out.endswith(OLEID_OUT)

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
