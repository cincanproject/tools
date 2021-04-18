# Ghidra Headless Analyzer

Ghidra is a software reverse engineering (SRE) framework created by National Security Agency.
This is an attempt to make docker image for purely decompiling binaries with headless version of Ghidra, and to produce decompiled C - code.

These includes sets of postscripts, which can be run in headless mode.


## Input

```
Any software binary in native instructions.
```

## Output

```
With default script, Decompiled source code in pseudo C - code. Output depends on used scripts.
```

## Usage

### Installation

***Method 1. Clone the repository and build by yourself***

```
git clone https://gitlab.com/CinCan/tools
cd tools/ghidra-decompiler
docker build . -t cincan/ghidra-decompiler
```

***Method 2. Pull the docker image*** 

```
docker pull cincan/ghidra-decompiler
```

***Method 3. use ['cincan'](https://gitlab.com/CinCan/cincan-command) tool*** 

Follow 'cincan' tool installation steps. If this tool is used, no need to install 'ghidra-decompiler' separately.

### Running

***Method 1. Run the docker container***

Analyse a sample in directory "/samples":  

```
docker run -v /samples:/samples cincan/ghidra-decompiler decompile /samples/ghidra_sample.exe
```

Or get possible arguments for the program:  

```
docker run -v /samples:/samples cincan/ghidra-decompiler --help
```

***Method 2. Run with 'cincan' tool:***

Analyse a provided example sample. It can be found from path `_samples/amd64/hello_world` from _samples directory.

```
cincan run cincan/ghidra-decompiler decompile _samples/amd64/hello_world
```

Get help for specifically this tool:

```
cincan run cincan/ghidra-decompiler --help
```

## Testing

Few tests are included for testing the functionality of container. These contains at least:

  * Test entrypoint
  * Test `--help` option
  * Decompile without options (= let Ghidra detect configuration automatically)

Tox can be used for testing this tool (run from root of this repository):
```
pip install tox
tox ghidra-decompiler
```

### Sample file

Simple C file, which as following code:

```c
#include <stdio.h>
int main()
{
    printf("Hello, World!\n");
    printf("And Hello for Ghidra Headless Analyzer!\n");
    return 0;
}
```
File is located in : `_samples/amd64/hello_world`

## Project homepage

https://ghidra-sre.org/

See more about Headless Analyzer in [here.](https://ghidra.re/ghidra_docs/analyzeHeadlessREADME.html)

## Licence

Ghidra itself is distributed under Apache 2.0 licence, however all additional features included here are under MIT licence.
