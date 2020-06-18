from testing import dockertools

SAMPLE_FILE="samples/android_apk/selendroid-test-app.apk"

def test_help():
    tool = dockertools.tool_with_file(__file__)
    out = tool.run_get_string([])
    assert out.startswith("ssdeep version 2.14.2 by Jesse Kornblum and the ssdeep Project")

def test_hash():
    tool = dockertools.tool_with_file(__file__)
    out = tool.run_get_string([SAMPLE_FILE])
    assert out.startswith("ssdeep,1.1--blocksize:hash:hash,filename\n6144:nHcS99ALfcA6AVzMNijFxZY+8YN0JjkP+Lo:nHcS9+L9V2ijFx2YuWP+Lo")
