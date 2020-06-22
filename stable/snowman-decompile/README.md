# Snowman-decompile

A native code to C/C++ decompiler. Parses given files, decompiles them, and prints the requested
information (by default, C++ code) to the specified files.

## Input

```
ELF Mach-O PE LE
```

## Output

```
Snowman report
```

## Supported tags and respective `Dockerfile` links

* `latest` ([*snowman-decompile/Dockerfile*](https://gitlab.com/CinCan/tools/tree/master/snowman-decompile))


## Usage

***1. Clone the repository***

```
git clone https://gitlab.com/CinCan/tools
cd tools/snowman-decompile/
```

***2. Build OR pull the docker image*** 

```
docker build . -t cincan/snowman-decompile
docker pull cincan/snowman-decompile
```

***3. Run the docker container***

Analyse a sample in directory "/samples":

`$ docker run --rm -v $(pwd):/samples cincan/snowman-decompile -v /samples/sample.exe`

or with cincan command:

`$ cincan run cincan/snowman-decompile /samples/sample.exe`



***Options***
```  
Usage: nocode [options] [--] file...

Options:
  --help, -h                  Produce this help message and quit.
  --verbose, -v               Print progress information to stderr.
  --print-sections[=FILE]     Print information about sections of the executable file.
  --print-symbols[=FILE]      Print the symbols from the executable file.
  --print-instructions[=FILE] Print parsed instructions to the file.
  --print-cfg[=FILE]          Print control flow graph in DOT language to the file.
  --print-ir[=FILE]           Print intermediate representation in DOT language to the file.
  --print-regions[=FILE]      Print results of structural analysis in DOT language to the file.
  --print-cxx[=FILE]          Print reconstructed program into given file.
  --from[=ADDR]               From disassemble boundary.
  --to[=ADDR]                 To disassemble boundary.

Version: ITDIR-N
Available architectures: arm-le arm-be 8086 i386 x86-64
Available parsers: ELF Mach-O PE LE
Report bugs to: https://github.com/yegord/snowman/issues
License: GNU General Public License, version 3 or any later version <https://github.com/yegord/snowman/blob/master/doc/licenses.asciidoc>

```

## Project homepage

[https://github.com/yegord/snowman/](https://github.com/yegord/snowman/)
