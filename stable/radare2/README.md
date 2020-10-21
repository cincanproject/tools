# Radare2 is complete unix-like framework for reverse engineering and binary analysis - version 4.5.1

Radare2 is complete unix-like framework for reverse engineering and binary analysis. It is built around command line tools, but there is also graphical user interface [Cutter](https://cutter.re/) built around it.
It is a rewrite from scratch from original radare.

It supports disassembling code, debugging programs, attaching to remote gdb servers, analyzing binaries such as relocations of symbols, binary diffing with graphs, producing ROP gadgets and shellcodes and so on.

This image contains additionally plugin [r2ghidra-dec](https://github.com/radareorg/r2ghidra-dec) as preinstalled.

# Input

Radare2 supports variety of different binary architectures. The most updated list  can be found from [here.](https://github.com/radareorg/radare2#architectures)

In practice, you can analyse any file, but here are supported file formats:

```
ELF, Mach-O, Fatmach-O, PE, PE+, MZ, COFF, OMF, TE, XBE, BIOS/UEFI, Dyldcache, DEX, ART, CGC, Java class, Android boot image, Plan9 executable, ZIMG, MBN/SBL bootloader, ELF coredump, MDMP (Windows minidump), WASM (WebAssembly binary), Commodore VICE emulator, QNX, Game Boy (Advance), Nintendo DS ROMs and Nintendo 3DS FIRMs, various filesystems.
```
The most updated list is [here.](https://github.com/radareorg/radare2#file-formats)

# Output

R2 is mostly used in interactive mode, but there are variety of outputs, including graphs, JSON files, different report formats

# Usage


### Installation

***Method 1. Clone the repository and build by yourself***

```
git clone https://gitlab.com/CinCan/tools
cd tools/radare2
docker build . -t cincan/radare2
```

***Method 2. Pull the docker image*** 

```
docker pull cincan/radare2
```

***Method 3. use ['cincan'](https://gitlab.com/CinCan/cincan-command) tool*** 

Follow 'cincan' tool installation steps. If this tool is used, no need to install 'radare2' separately.

Tool supports interactive mode as well.

### Running

There is wrapper script [entrypoint.sh](entrypoint.sh) which enables only to use tools coming with radare2. It also enables for running scripts in [scripts](scripts) folder.

***Method 1. Run the docker container***

Let's expect that we have subfolder in current directory named as 'samples'

```
docker run --rm -itv $(pwd)/samples:/r2/samples cincan/radare2 r2 /r2/samples/hello_world
```

This will make radare2 to open file.

Consult radare2 documentation to make analysis!


***Method 2. Run with 'cincan' tool:***

Above can be executed, when `--interactive` and `--tty` flags are provided (similar to docker) for cincan command.

```
cincan run -it cincan/radare2 r2 samples/hello_world
```

Example fo using 'r2_callgraph.sh' script, which is using 'samples' directory as argument.
It will generate graph from binary's function calls.

```
cincan run cincan/radare2 script r2_callgraph.sh samples
```

Get general help for using container:

```
cincan run cincan/radare2 --help
```

## Blog

For more examples about the tool, see some blog posts:

  * [cincan.io/blog/2019_12_20_radare2/](https://gitlab.com/CinCan/cincan.io/blob/master/site/blog/2019_12_20_radare2.md)


# Project homepage

Website: https://www.radare.org/n/  
GitHub: https://github.com/radareorg/radare2  
Cutter (GUI): https://cutter.re/  
Cutter Git: https://github.com/radareorg/cutter

# Licence

GNU General Public License v3.0
