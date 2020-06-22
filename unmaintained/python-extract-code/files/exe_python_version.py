import os
import requests
import argparse
import binascii
import subprocess
import shutil


SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))


def recursive_filepaths(path):
    for root, subdir, filenames in os.walk(path):
        for filename in filenames:
            filepath = os.path.join(root, filename)
            yield filepath


def get_pyc_magic(path):
    with open(path, "rb") as f:
        pyc_bytes = f.read(2)
    pyc_magic = int(binascii.hexlify(pyc_bytes[::-1]), 16)
    return pyc_magic


def download_magic(url="https://raw.githubusercontent.com/google/pytype/master/pytype/pyc/magic.py",
                    magic_path=os.path.join(SCRIPT_DIR, "magic.py")
                    ):

    if os.path.exists(magic_path):
        return

    resp = requests.get(url)
    magic = resp.text
    with open(magic_path, "w") as f:
        f.write(magic)

def get_pyc_py_version(path):
    pyc_magic = get_pyc_magic(path)
    if not pyc_magic in magic.PYTHON_MAGIC:
        return (0, 0)

    py_version = magic.PYTHON_MAGIC[pyc_magic]
    return py_version, pyc_magic


def extract_exe(path):
    unpacker_script = os.path.join(SCRIPT_DIR, "python_exe_unpack.py")
    output_dir = os.path.join(SCRIPT_DIR, "unpacked")
    try:
        subprocess.check_output(["python3", unpacker_script, "-i", path, "-o", output_dir])
    except:
        pass

    return output_dir


def is_pyc(path):
    if path.endswith(".pyc"):
        return True
    
    return False


def extract_exe_version(path, verbose=False):
    output_dir = extract_exe(filepath)
    if not output_dir:
        shutil.rmtree(output_dir)
        return None
    all_versions = []
    all_magics = []
    for pyc_filepath in recursive_filepaths(output_dir):
        if not is_pyc(pyc_filepath):
            continue
        py_version, pyc_magic = get_pyc_py_version(pyc_filepath)
        all_versions.append(py_version)
        all_magics.append(pyc_magic)

    version = list(set(all_versions))
    if len(version) != 1 and verbose:
        print("ERROR: Found more than 1 version or no version at all.")
        return None

    version = version[0]
    pyc_magic = all_magics[0]

    if verbose:
        print("{}: Python version: {}.{} ({})".format(filepath, version[0], version[1], pyc_magic))
    shutil.rmtree(output_dir)
    return version, pyc_magic
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Define with which Python version EXE file was 'compiled'")
    parser.add_argument("inpath", help="Path to file or folder containing files")
    parser.add_argument("--count", help="Count amount of Python EXE files", action="store_true")
    args = vars(parser.parse_args())

    if not os.path.exists(args["inpath"]):
        print("Path '{}' does not exists.".format(args["inpath"]))
        exit()

    if os.path.isfile(args["inpath"]):
        filepaths = [args["inpath"]]
    else:
        filepaths = recursive_filepaths(args["inpath"])

    download_magic()
    import magic

    count = 0
    for filepath in filepaths:
        out = extract_exe_version(filepath, verbose=True)
        if out:
            count += 1

        if args["count"]:
            print("Amount of Python EXE files: {}".format(count))