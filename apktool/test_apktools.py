from metatool import dockertools

def test_help():
    tool = dockertools.tool_with_file(__file__)
    out = tool.run_get_string([])
    assert out.startswith("Apktool v2.4.0")

def test_apk_to_jar():
    tool = dockertools.tool_with_file(__file__)
    out = tool.run_get_string(["d", tool.file_to_copy_from_context("samples/selendroid-test-app.apk", "o" "selendroid-test-app-test")])
    assert out.startswith("I: Using Apktool 2.4.0 on selendroid-test-app.apk")
