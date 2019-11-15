from metatool import dockertools
import os.path
from os import path
import shutil

def test_help():
    tool = dockertools.tool_with_file(__file__)
    out = tool.run_get_string([])
    assert out.startswith("\njadx - dex to java decompiler")


def test_decompile_jar():
    tool = dockertools.tool_with_file(__file__)
    out = tool.run_get_string([tool.file_to_copy_from_context("samples/selendroid-test-app-dex2jar.jar"), "-ds", "^^selendroid-test-app.zip"])
    #how to check that what's in file system
    assert str(path.exists('selendroid-test-app.zip'))


def test_remove_file():
    #check that file exists
    if(str(path.exists('selendroid-test-app.zip'))):
        #remove file    
        shutil.rmtree("selendroid-test-app.zip")
    #check that file doesn't exist any more