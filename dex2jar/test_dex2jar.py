from metatool import dockertools
from zipfile import ZipFile

def test_help():
    tool = dockertools.tool_with_file(__file__)
    out = tool.run_get_string([])
    assert out.startswith("d2j-dex2jar")

def test_apk_to_jar():
    tool = dockertools.tool_with_file(__file__)
    out = tool.run_get_string([tool.file_to_copy_from_context("samples/selendroid-test-app.apk")])
    assert "./selendroid-test-app-dex2jar.jar" in out
 #   print(out)

#def test_do_run():
 #   tool = dockertools.tool_with_file(__file__)
#
 #   out = tool.do_get_string(in_file=tool.file_to_copy_from_context("samples//selendroid-test-app.apk", prefix=False),
  #                            out_type='jar',args=["d"])
   # assert out.startswith("[")
