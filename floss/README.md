# FireEye Labs Obfuscated String Solver

FireEye Labs Obfuscated String Solver (FLOSS) is a tool for automatically deobfuscating strings from malware binaries. It uses heuristics to identify decoding routines in a sample, extracting cross references and arguments to decoders and then emulates the decoder functions using the extracted arguments. After that it diffs the emulator memory states from before and after emulation and extracts human readable strings.

Floss can also be used just like `strings`, so it can be easily implemented in the normal static analysis workflow.

## Input

```
Malware with (obfuscated) strings
```

## Output

```
Human-readable strings
```

## Supported tags and respective `Dockerfile` links

* `latest` ([*FLOSS/Dockerfile*](https://gitlab.com/CinCan/tools/blob/master/floss/Dockerfile))

## Usage
### Install

***Method 1: Clone the repository and build by yourself***

```
git clone https://gitlab.com/CinCan/tools
cd tools/floss/
docker build . -t cincan/floss
```

***Method 2: Pull the docker image*** 

```
docker pull cincan/floss
```

***Method 3: use ['cincan'](https://gitlab.com/CinCan/cincan-command) tool***

Follow `cincan` tool installation steps. If this tool is used, no need to install `floss` separately.

### Running

***Method 1. Run the docker container***

Analyze a sample:

`$ docker run --rm -v /path/to/samples:/samples cincan/floss /samples/floss_sample.exe`  

***Method 2. Run with ['cincan'](https://gitlab.com/CinCan/cincan-command) tool:***

Analyze the example sample available in the sample folder:

`$ cincan run cincan/floss ../_samples/msdos/suspicious_dos_sample.exe`


***Options***
```shell script
Options:
  --version             show program's version number and exit
  -h, --help            show this help message and exit
  -n MIN_LENGTH, --minimum-length=MIN_LENGTH
                        minimum string length (default is 4)
  -f FUNCTIONS, --functions=FUNCTIONS
                        only analyze the specified functions (comma-separated)
  --save-workspace      save vivisect .viv workspace file in current directory
  -m, --show-metainfo   display vivisect workspace meta information
  --no-filter           do not filter deobfuscated strings (may result in many
                        false positive strings)

  Shellcode options:
    Analyze raw binary file containing shellcode

    -s, --shellcode     analyze shellcode
    -e SHELLCODE_ENTRY_POINT, --shellcode_ep=SHELLCODE_ENTRY_POINT
                        shellcode entry point
    -b SHELLCODE_BASE, --shellcode_base=SHELLCODE_BASE
                        shellcode base offset

  Extraction options:
    Specify which string types FLOSS shows from a file, by default all
    types are shown

    --no-static-strings
                        do not show static ASCII and UTF-16 strings
    --no-decoded-strings
                        do not show decoded strings
    --no-stack-strings  do not show stackstrings

  Format Options:
    -g, --group         group output by virtual address of decoding functions
    -q, --quiet         suppress headers and formatting to print only
                        extracted strings

  Logging Options:
    -v, --verbose       show verbose messages and warnings
    -d, --debug         show all trace messages

  Script output options:
    -i IDA_PYTHON_FILE, --ida=IDA_PYTHON_FILE
                        create an IDAPython script to annotate the decoded
                        strings in an IDB file
    --x64dbg=X64DBG_DATABASE_FILE
                        create a x64dbg database/json file to annotate the
                        decoded strings in x64dbg
    -r RADARE2_SCRIPT_FILE, --radare=RADARE2_SCRIPT_FILE
                        create a radare2 script to annotate the decoded
                        strings in an .r2 file

  Identification Options:
    -p PLUGINS, --plugins=PLUGINS
                        apply the specified identification plugins only
                        (comma-separated)
    -l, --list-plugins  list all available identification plugins and exit

  FLOSS Profiles:
    -x, --expert        show duplicate offset/string combinations, save
                        workspace, group function output
```

## Project homepage

[FireEye Labs Obfuscated String Solver](https://github.com/fireeye/flare-floss)

## License

[Apache License 2.0](https://github.com/fireeye/flare-floss/blob/master/LICENSE.txt)
