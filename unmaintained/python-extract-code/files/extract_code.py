import os
import argparse
import subprocess
import shutil

import exe_python_version


SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))

def filter_interesting_filepaths(filepaths, interesting_byte=b"\xe3"):
    for filepath in filepaths:
        with open(filepath, "rb") as f:
            first_byte = f.read(1)

        if first_byte == interesting_byte:
            yield filepath

def run_uncompyle6(path, outpath):
    outpath = os.path.join(outpath, os.path.basename(path) + ".py")
    output = subprocess.check_output(["uncompyle6", path])

    with open(outpath, "wb") as f:
        f.write(output)


def find_correct_header(path):
    pyc_filepath = None
    filepaths = exe_python_version.recursive_filepaths(path)
    for filepath in filepaths:
        if exe_python_version.is_pyc(filepath):
            pyc_filepath = filepath
            break

    with open(pyc_filepath, "rb") as f:
        header = f.read(12)

    return header


def correct_bytecode(path, header):
    outpath = path + ".pyc"
    with open(path, "rb") as f:
        filedata = f.read()

    filedata = header + filedata

    with open(outpath, "wb") as f:
        f.write(filedata)
    
    return outpath


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extract Python code from Python compiled EXE")
    parser.add_argument("inpath", help="Path to file or folder containing files")
    args = vars(parser.parse_args())

    if not os.path.exists(args["inpath"]):
        print("Path '{}' does not exists.".format(args["inpath"]))
        exit()

    if os.path.isfile(args["inpath"]):
        filepaths = [args["inpath"]]
    else:
        filepaths = recursive_filepaths(args["inpath"])

    for filepath in filepaths:
        output_dir = exe_python_version.extract_exe(filepath)
        header = find_correct_header(output_dir)
        unpacked_filepaths = exe_python_version.recursive_filepaths(output_dir)
        for unpacked_filepath in filter_interesting_filepaths(unpacked_filepaths):
            code_output_dir = os.path.basename(filepath)
            if not os.path.exists(code_output_dir):
                os.mkdir(code_output_dir)

            pyc_path = correct_bytecode(unpacked_filepath, header)
            run_uncompyle6(pyc_path, code_output_dir)
        
    shutil.rmtree(output_dir)