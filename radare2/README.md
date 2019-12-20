# radare2 - version 4.1.0

Radare2 is complete unix-like framework for reverse engineering and binary analysis. It is built around command line tools, but there is also graphical user interface [Cutter](https://cutter.re/) built around it.
It is a rewrite from scratch from original radare.

It supports disassembling code, debugging programs, attaching to remote gdb servers, analyzing binaries such as relocations of symbols, binary diffing with graphs, producing ROP gadgets and shellcodes and so on.

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

# Project homepage

Website: https://www.radare.org/n/
GitHub: https://github.com/radareorg/radare2
Cutter (GUI): https://cutter.re/
Cutter Git: https://github.com/radareorg/cutter

# Licence

GNU General Public License v3.0