[![pipeline status](https://gitlab.com/CinCan/tools/badges/master/pipeline.svg)](https://gitlab.com/CinCan/tools/commits/master)

# Dockerfiles for the CinCan project

This repository will automatically build and publish Docker images into Docker Hub, GitHub Container Registry and Quay.io using GitLab-CI.

The pipeline will try to build a new image for each directory that **_has changes_** _since the latest passed commit_, once provided tests have been passed. The most of the tools are tested with real samples to see that they work as excepted.

README description of each tool is synchronized into Docker Hub as well.

Actual images can be found from:
 * [CinCan Docker Hub repository](https://hub.docker.com/r/cincan/)
 * [CinCan GitHub Container Registry](https://github.com/orgs/cincanproject/packages)
 * [CinCan Quay Registry](https://quay.io/organization/cincan)

For adding a new tool or upgrading the version of existing one, see [CONTRIBUTING.md](CONTRIBUTING.md)

## Description of the current tools
### Linux tools

### Stable

| Tool name | Description | Input               | Platform |
|-----------|-------------|---------------------|----------|
| [7zip](https://gitlab.com/CinCan/tools/-/tree/master/stable/7zip) |  Command line port of 7-Zip which provides utilities to (un)pack compressed archives | 7z, ZIP, GZIP, BZIP2, XZ, TAR, APM, ARJ, CAB, CHM, CPIO, CramFS, DEB, DMG, FAT, HFS, ISO, LZH, LZMA, LZMA2, MBR, MSI, MSLZ, NSIS, NTFS, RAR, RPM, SquashFS, UDF,VHD, WIM, XAR, Z  | Linux |
| [access-log-visualization](https://gitlab.com/CinCan/tools/-/tree/master/stable/access-log-visualization) |  Visualizing webserver's access log data to help detecting malicious activity | access.log (Apache)  | Linux |
| [apktool](https://gitlab.com/CinCan/tools/-/tree/master/stable/apktool) |  A tool for reverse engineering 3rd party, closed, binary Android apps. | .apk, .jar   | Linux |
| [binwalk](https://gitlab.com/CinCan/tools/-/tree/master/stable/binwalk) |  Firmware Analysis Tool | binary  | Linux |
| [cfr](https://gitlab.com/CinCan/tools/-/tree/master/stable/cfr) |  Class File Reader - another java decompiler | .jar -file  | Linux |
| [clamav](https://gitlab.com/CinCan/tools/-/tree/master/stable/clamav) |  ClamAV virus scanner | Any file or directory.  | Linux |
| [dex2jar](https://gitlab.com/CinCan/tools/-/tree/master/stable/dex2jar) |  Tool to decompile dex files to jar | APK file  | Linux |
| [eml_parser](https://gitlab.com/CinCan/tools/-/tree/master/stable/eml_parser) |  Parse .eml email files | eml  | Linux |
| [feature_extractor](https://gitlab.com/CinCan/tools/-/tree/master/stable/feature_extractor) |  Feature_extractor | list of possible IoCs  | Linux |
| [fernflower](https://gitlab.com/CinCan/tools/-/tree/master/stable/fernflower) |  Analytical decompiler for Java | .jar, .class, .zip  | Linux |
| [flawfinder](https://gitlab.com/CinCan/tools/-/tree/master/stable/flawfinder) |  Flawfinder - Finds possible security weaknesses in C/C++ source code | C/C++ code  | Linux |
| [floss](https://gitlab.com/CinCan/tools/-/tree/master/stable/floss) |  FireEye Labs Obfuscated String Solver | Malware with (obfuscated) strings  | Linux |
| [ghidra-decompiler](https://gitlab.com/CinCan/tools/-/tree/master/stable/ghidra-decompiler) |  Ghidra Headless Analyzer - Version 9.1 | Any software binary in native instructions.  | Linux |
| [ilspy](https://gitlab.com/CinCan/tools/-/tree/master/stable/ilspy) |  ILSpy (console only) - version 6.1.0 | .NET Assembly  | Linux |
| [ioc_strings](https://gitlab.com/CinCan/tools/-/tree/master/stable/ioc_strings) |  Extracts urls, hashes, emails, ips, domains and base64 (other) from a file. | File/Directory  | Linux |
| [iocextract](https://gitlab.com/CinCan/tools/-/tree/master/stable/iocextract) |  Advanced Indicator of Compromise (IOC) extractor | File, STDIN  | Linux |
| [jadx](https://gitlab.com/CinCan/tools/-/tree/master/stable/jadx) |  jadx - Dex to Java decompiler | .apk, .dex, .jar, .class, .smali, .zip, .aar, .arsc  | Linux |
| [jd-cmd](https://gitlab.com/CinCan/tools/-/tree/master/stable/jd-cmd) |  Command line wrapper around JD Core Java Decompiler. Decompiles .dex and .jar -files to java. | .jar -file  | Linux |
| [jsunpack-n](https://gitlab.com/CinCan/tools/-/tree/master/stable/jsunpack-n) |  Jsunpack-n - Emulates browser functionality, detect exploits etc. | PDF, URL, PCAP, JavaScript, SWF  | Linux |
| [manalyze](https://gitlab.com/CinCan/tools/-/tree/master/stable/manalyze) |  Manalyze - a static analyzer for PE executables | PE files  | Linux |
| [oledump](https://gitlab.com/CinCan/tools/-/tree/master/stable/oledump) |  A Program to analyse OLE files. | .doc, .xls, .ppt  | Linux |
| [oletools](https://gitlab.com/CinCan/tools/-/tree/master/stable/oletools) |  Oletools - version 0.56 to analyze Microsoft OLE2 files | .doc, .dot, .docm, .dotm, .xml, .mht, .xls, .xlsm, .xlsb, .pptm, .ppsm, VBA/VBScript source  | Linux |
| [osslsigncode](https://gitlab.com/CinCan/tools/-/tree/master/stable/osslsigncode) |  osslsigncode | exe/sys/dll  | Linux |
| [output-standardizer](https://gitlab.com/CinCan/tools/-/tree/master/stable/output-standardizer) |  Generate md report from Cincan's Concourse pipelines, or convert single tool output to JSON.   | cincan/binwalk, cincan/pdf2john, cincan/pdfxray_lite and cincan/strings outputs  | Linux |
| [pastelyzer](https://gitlab.com/CinCan/tools/-/tree/master/stable/pastelyzer) |  pastelyzer - find security and privacy related artifacts from text documents | text  | Linux |
| [pdf-parser](https://gitlab.com/CinCan/tools/-/tree/master/stable/pdf-parser) |  PDF-parser - parse PDF to identify fundamental elements | PDF  | Linux |
| [pdfid](https://gitlab.com/CinCan/tools/-/tree/master/stable/pdfid) |  PDFID - scan PDFs for certain keywords, triage potentially malicious files | PDF  | Linux |
| [pdfxray-lite](https://gitlab.com/CinCan/tools/-/tree/master/stable/pdfxray-lite) |  PDF X-RAY Lite 1.0 to analyze PDF files for malicious objects.  | PDF  | Linux |
| [peepdf](https://gitlab.com/CinCan/tools/-/tree/master/stable/peepdf) |  Powerful Python tool to analyze PDF documents. | PDF  | Linux |
| [peframe](https://gitlab.com/CinCan/tools/-/tree/master/stable/peframe) |  PEframe - static analysis for PE executables and MS office documents | PE  | Linux |
| [pyocr](https://gitlab.com/CinCan/tools/-/tree/master/stable/pyocr) |  Optical character recognition (OCR) wrapper for Tesseract OCR engine | PDF, png, jpg  | Linux |
| [pywhois](https://gitlab.com/CinCan/tools/-/tree/master/stable/pywhois) |  Pywhois - retrieve information from IP addresses | IP / list of IPs  | Linux |
| [radamsa](https://gitlab.com/CinCan/tools/-/tree/master/stable/radamsa) |  Radamsa is a test case generator for robustness testing, a.k.a. a fuzzer. | Any data  | Linux |
| [radare2](https://gitlab.com/CinCan/tools/-/tree/master/stable/radare2) |  Radare2 is complete unix-like framework for reverse engineering and binary analysis - version 4.5.0 | ELF, Mach-O, Fatmach-O, PE, PE+, MZ, COFF, OMF, TE, XBE, BIOS/UEFI, Dyldcache, DEX, ART, CGC, Java class, Android boot image, Plan9 executable, ZIMG, MBN/SBL bootloader, ELF coredump, MDMP (Windows minidump), WASM (WebAssembly binary), Commodore VICE emulator, QNX, Game Boy (Advance), Nintendo DS ROMs and Nintendo 3DS FIRMs, various filesystems.  | Linux |
| [regripper](https://gitlab.com/CinCan/tools/-/tree/master/stable/regripper) |  Extract data from Windows registry | Windows registry hive files  | Linux |
| [sleuthkit](https://gitlab.com/CinCan/tools/-/tree/master/stable/sleuthkit) |  A collection of command line tools that allows you to analyze disk images and recover files. | raw, ewf, vmdk, vhd  | Linux |
| [snowman-decompile](https://gitlab.com/CinCan/tools/-/tree/master/stable/snowman-decompile) |  Snowman-decompile - a native code to C/C++ decompiler | ELF Mach-O PE LE  | Linux |
| [ssdc](https://gitlab.com/CinCan/tools/-/tree/master/stable/ssdc) |  Ssdeep based clustering tool | *  | Linux |
| [ssdeep](https://gitlab.com/CinCan/tools/-/tree/master/stable/ssdeep) |  Ssdeep - For computing context triggered piecewise hashes (CTPH), also called fuzzy hashes. | *  | Linux |
| [steghide](https://gitlab.com/CinCan/tools/-/tree/master/stable/steghide) |  A Steganography program - hide data (and extract) in various kinds of image- and audio-files. | JPEG, BMP, WAV, AU  | Linux |
| [tshark](https://gitlab.com/CinCan/tools/-/tree/master/stable/tshark) |  A Tool for parsing PCAP and capturing network traffic. | PCAP, network traffic  | Linux |
| [vipermonkey](https://gitlab.com/CinCan/tools/-/tree/master/stable/vipermonkey) |  A VBA parser and emulation engine to analyze malicious macros | .doc, .dot, .docm, .dotm, .xml, .mht, .xls, .xlsm, .xlsb, .pptm, .ppsm, VBA/VBScript source  | Linux |
| [virustotal](https://gitlab.com/CinCan/tools/-/tree/master/stable/virustotal) |  Official CLI for VirusTotal API. Analyze suspicious files and URLs to detect malware. |   | Linux |
| [volatility](https://gitlab.com/CinCan/tools/-/tree/master/stable/volatility) |  Volatility - An advanced memory forensics framework |   - Raw linear sample (dd)   - Hibernation file (from Windows 7 and earlier)   - Crash dump file   - VirtualBox ELF64 core dump   - VMware saved state and snapshot files   - EWF format (E01)    - LiME format   - Mach-O file format   - QEMU virtual machine dumps   - Firewire    - HPAK (FDPro)  | Linux |
| [xsv](https://gitlab.com/CinCan/tools/-/tree/master/stable/xsv) |  Fast CSV command line toolkit | csv, tsv  | Linux |
| [yara](https://gitlab.com/CinCan/tools/-/tree/master/stable/yara) |  Yara - The pattern matching swiss knife  | Any file as target  | Linux |
| [zsteg](https://gitlab.com/CinCan/tools/-/tree/master/stable/zsteg) |  detect stegano-hidden data in PNG & BMP | PNG, BMP  | Linux |
### In Development

| Tool name | Description | Input               | Platform |
|-----------|-------------|---------------------|----------|
| [headless-thunderbird](https://gitlab.com/CinCan/tools/-/tree/master/development/headless-thunderbird) |  Headless Thunderbird to screenshot email messages | eml  | Linux |
| [ioc_parser](https://gitlab.com/CinCan/tools/-/tree/master/development/ioc_parser) |  A tool to extract indicators of compromise from security reports | PDF, txt, xlsx, html  | Linux |
| [pdf2john](https://gitlab.com/CinCan/tools/-/tree/master/development/pdf2john) |  John the Ripper for extracting hash from PDF files | Encrypted PDF  | Linux |
| [scrape-website](https://gitlab.com/CinCan/tools/-/tree/master/development/scrape-website) |  |  | Linux |
| [trufflehog](https://gitlab.com/CinCan/tools/-/tree/master/development/trufflehog) |  TruffleHog Searches through git repositories for accidentally committed secrets | git repository  | Linux |
### Not maintained anymore

It is very possible that some of these are not working.

| Tool name | Description | Input               | Platform |
|-----------|-------------|---------------------|----------|
| [add2git-lfs](https://gitlab.com/CinCan/tools/-/tree/master/unmaintained/add2git-lfs) |  ADD2GIT-LFS |  | Linux |
| [binary-analysis-tool-bat](https://gitlab.com/CinCan/tools/-/tree/master/unmaintained/binary-analysis-tool-bat) |  Binary Analysis Tool BAT with extra tools | binary  | Linux |
| [c-ci](https://gitlab.com/CinCan/tools/-/tree/master/unmaintained/c-ci) |  Concourse CI |  | Linux |
| [c-worker](https://gitlab.com/CinCan/tools/-/tree/master/unmaintained/c-worker) |  Concourse Worker |  | Linux |
| [dns-tools](https://gitlab.com/CinCan/tools/-/tree/master/unmaintained/dns-tools) |  |  | Linux |
| [hyperscan](https://gitlab.com/CinCan/tools/-/tree/master/unmaintained/hyperscan) |  High-performance regular expression matching library |  | Linux |
| [identify-file](https://gitlab.com/CinCan/tools/-/tree/master/unmaintained/identify-file) |  Identify-file |  | Linux |
| [keyfinder](https://gitlab.com/CinCan/tools/-/tree/master/unmaintained/keyfinder) |  Keyfinder | filesystem, APK  | Linux |
| [pdf-tools](https://gitlab.com/CinCan/tools/-/tree/master/unmaintained/pdf-tools) |  The DidierStevensSuite by Didier Stevens |  | Linux |
| [pdfexaminer](https://gitlab.com/CinCan/tools/-/tree/master/unmaintained/pdfexaminer) |  Upload a PDF to www.pdfexaminer.com/pdfapi.php and get results | PDF files  | Linux |
| [pe-scanner](https://gitlab.com/CinCan/tools/-/tree/master/unmaintained/pe-scanner) |  Get information of a PE (portable executable) file | PE/EXE/DLL  | Linux |
| [python-extract-code](https://gitlab.com/CinCan/tools/-/tree/master/unmaintained/python-extract-code) |  Extract code | PE  | Linux |
| [r2-bin-carver](https://gitlab.com/CinCan/tools/-/tree/master/unmaintained/r2-bin-carver) |  R2 bin carver | memory dumps  | Linux |
| [s3-resource-simple](https://gitlab.com/CinCan/tools/-/tree/master/unmaintained/s3-resource-simple) |  Simple S3 Resource for [Concourse CI](http://concourse.ci) |  | Linux |
| [shellcode2exe](https://gitlab.com/CinCan/tools/-/tree/master/unmaintained/shellcode2exe) |  Convert shellcodes into executable files, for multiple platforms. | shellcode  | Linux |
| [suricata](https://gitlab.com/CinCan/tools/-/tree/master/unmaintained/suricata) |  Suricata  |  | Linux |
| [twiggy](https://gitlab.com/CinCan/tools/-/tree/master/unmaintained/twiggy) |  Twiggy analyzes a binary's call graph | .wasm, partial ELF & Mach-O support   | Linux |
| [vba2graph](https://gitlab.com/CinCan/tools/-/tree/master/unmaintained/vba2graph) |  Generate call graphs from VBA code | office documents such as .doc, .xls, .bas  | Linux |
| [xmldump](https://gitlab.com/CinCan/tools/-/tree/master/unmaintained/xmldump) |  Parse XML files. | XML  | Linux |
