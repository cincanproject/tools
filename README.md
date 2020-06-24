[![pipeline status](https://gitlab.com/CinCan/tools/badges/master/pipeline.svg)](https://gitlab.com/CinCan/tools/commits/master)

# Dockerfiles for the CinCan project

This repository will automatically build and publish Docker images into Docker Hub using GitLab-CI.

The pipeline will try to build a new image for each directory that **_has changes_** _since the latest passed commit_, once provided tests have been passed. The most of the tools are tested with real samples to see that they work as excepted.

README description of each tool is synchronized into Docker Hub as well.

Actual images can be found from:
[https://hub.docker.com/r/cincan/](https://hub.docker.com/r/cincan/)

For adding a new tool or upgrading the version of existing one, see [CONTRIBUTING.md](CONTRIBUTING.md)

## Description of the current tools
### Linux tools

| Tool name | Description | Input               | Platform |
|-----------|-------------|---------------------|----------|
| [pastelyzer](https://gitlab.com/CinCan/tools/-/tree/master/pastelyzer) |  the paste analyzer | text  | Linux |
| [sleuthkit](https://gitlab.com/CinCan/tools/-/tree/master/sleuthkit) |  A collection of command line tools that allows you to analyze disk images and recover files. | raw, ewf, vmdk, vhd  | Linux |
| [vba2graph](https://gitlab.com/CinCan/tools/-/tree/master/vba2graph) |  Generate call graphs from VBA code | office documents such as .doc, .xls, .bas  | Linux |
| [r2-bin-carver](https://gitlab.com/CinCan/tools/-/tree/master/r2-bin-carver) |  R2 bin carver | memory dumps  | Linux |
| [feature_extractor](https://gitlab.com/CinCan/tools/-/tree/master/feature_extractor) |  Feature_extractor | list of possible IoCs  | Linux |
| [trufflehog](https://gitlab.com/CinCan/tools/-/tree/master/trufflehog) |  TruffleHog Searches through git repositories for accidentally committed secrets | git repository  | Linux |
| [keyfinder](https://gitlab.com/CinCan/tools/-/tree/master/keyfinder) |  Keyfinder | filesystem, APK  | Linux |
| [osslsigncode](https://gitlab.com/CinCan/tools/-/tree/master/osslsigncode) |  osslsigncode | exe/sys/dll  | Linux |
| [headless-thunderbird](https://gitlab.com/CinCan/tools/-/tree/master/headless-thunderbird) |  Headless Thunderbird to screenshot email messages | eml  | Linux |
| [eml_parser](https://gitlab.com/CinCan/tools/-/tree/master/eml_parser) |  Parse .eml email files | eml  | Linux |
| [xsv](https://gitlab.com/CinCan/tools/-/tree/master/xsv) |  Fast CSV command line toolkit | csv, tsv  | Linux |
| [output-standardizer](https://gitlab.com/CinCan/tools/-/tree/master/output-standardizer) |  Generate md report from Cincan's Concourse pipelines, or convert single tool output to JSON.   | cincan/binwalk, cincan/pdf2john, cincan/pdfxray_lite and cincan/strings outputs  | Linux |
| [binwalk](https://gitlab.com/CinCan/tools/-/tree/master/binwalk) |  Firmware Analysis Tool | binary  | Linux |
| [binary-analysis-tool-bat](https://gitlab.com/CinCan/tools/-/tree/master/binary-analysis-tool-bat) |  Binary Analysis Tool BAT with extra tools | binary  | Linux |
| [access-log-visualization](https://gitlab.com/CinCan/tools/-/tree/master/access-log-visualization) |  Visualizing webserver's access log data to help detecting malicious activity | access.log (Apache)  | Linux |
| [xmldump](https://gitlab.com/CinCan/tools/-/tree/master/xmldump) |  Parse XML files. | XML  | Linux |
| [regripper](https://gitlab.com/CinCan/tools/-/tree/master/regripper) |  Extract data from Windows registry | Windows registry hive files  | Linux |
| [zsteg](https://gitlab.com/CinCan/tools/-/tree/master/zsteg) |  detect stegano-hidden data in PNG & BMP | PNG, BMP  | Linux |
| [pe-scanner](https://gitlab.com/CinCan/tools/-/tree/master/pe-scanner) |  Get information of a PE (portable executable) file | PE/EXE/DLL  | Linux |
| [manalyze](https://gitlab.com/CinCan/tools/-/tree/master/manalyze) |  Manalyze - a static analyzer for PE executables | PE files  | Linux |
| [python-extract-code](https://gitlab.com/CinCan/tools/-/tree/master/python-extract-code) |  Extract code | PE  | Linux |
| [peframe](https://gitlab.com/CinCan/tools/-/tree/master/peframe) |  PEframe | PE  | Linux |
| [ioc_parser](https://gitlab.com/CinCan/tools/-/tree/master/ioc_parser) |  A tool to extract indicators of compromise from security reports | PDF, txt, xlsx, html  | Linux |
| [pyocr](https://gitlab.com/CinCan/tools/-/tree/master/pyocr) |  Optical character recognition (OCR) wrapper for Tesseract OCR engine | PDF, png, jpg  | Linux |
| [jsunpack-n](https://gitlab.com/CinCan/tools/-/tree/master/jsunpack-n) |  Jsunpack-n | PDF, URL, PCAP, JavaScript, SWF  | Linux |
| [pdfexaminer](https://gitlab.com/CinCan/tools/-/tree/master/pdfexaminer) |  PDFExaminer | PDF files  | Linux |
| [peepdf](https://gitlab.com/CinCan/tools/-/tree/master/peepdf) |  Powerful Python tool to analyze PDF documents. | PDF  | Linux |
| [pdfxray-lite](https://gitlab.com/CinCan/tools/-/tree/master/pdfxray-lite) |  PDF X-RAY Lite 1.0 to analyze PDF files for malicious objects.  | PDF  | Linux |
| [pdfid](https://gitlab.com/CinCan/tools/-/tree/master/pdfid) |  PDFID | PDF  | Linux |
| [pdf-parser](https://gitlab.com/CinCan/tools/-/tree/master/pdf-parser) |  PDF-parser | PDF  | Linux |
| [tshark](https://gitlab.com/CinCan/tools/-/tree/master/tshark) |  A Tool for parsing PCAP and capturing network traffic. | PCAP, network traffic  | Linux |
| [floss](https://gitlab.com/CinCan/tools/-/tree/master/floss) |  FireEye Labs Obfuscated String Solver | Malware with (obfuscated) strings  | Linux |
| [steghide](https://gitlab.com/CinCan/tools/-/tree/master/steghide) |  A Steganography program that is able to hide data (and extract) in various kinds of image- and audio-files. | JPEG, BMP, WAV, AU  | Linux |
| [pywhois](https://gitlab.com/CinCan/tools/-/tree/master/pywhois) |  Pywhois | IP / list of IPs  | Linux |
| [ioc_strings](https://gitlab.com/CinCan/tools/-/tree/master/ioc_strings) |  Extracts urls, hashes, emails, ips, domains and base64 (other) from a file. | File/Directory  | Linux |
| [iocextract](https://gitlab.com/CinCan/tools/-/tree/master/iocextract) |  Advanced Indicator of Compromise (IOC) extractor | File  | Linux |
| [pdf2john](https://gitlab.com/CinCan/tools/-/tree/master/pdf2john) |  John the Ripper for extracting hash from PDF files | Encrypted PDF  | Linux |
| [radare2](https://gitlab.com/CinCan/tools/-/tree/master/radare2) |  Radare2 is complete unix-like framework for reverse engineering and binary analysis - version 4.4.0 | ELF, Mach-O, Fatmach-O, PE, PE+, MZ, COFF, OMF, TE, XBE, BIOS/UEFI, Dyldcache, DEX, ART, CGC, Java class, Android boot image, Plan9 executable, ZIMG, MBN/SBL bootloader, ELF coredump, MDMP (Windows minidump), WASM (WebAssembly binary), Commodore VICE emulator, QNX, Game Boy (Advance), Nintendo DS ROMs and Nintendo 3DS FIRMs, various filesystems.  | Linux |
| [snowman-decompile](https://gitlab.com/CinCan/tools/-/tree/master/snowman-decompile) |  Snowman-decompile | ELF Mach-O PE LE  | Linux |
| [flawfinder](https://gitlab.com/CinCan/tools/-/tree/master/flawfinder) |  Flawfinder - Finds possible security weaknesses in C/C++ source code | C/C++ code  | Linux |
| [ghidra-decompiler](https://gitlab.com/CinCan/tools/-/tree/master/ghidra-decompiler) |  Ghidra Headless Analyzer - Version 9.1 | Any software binary in native instructions.  | Linux |
| [clamav](https://gitlab.com/CinCan/tools/-/tree/master/clamav) |  ClamAV virus scanner:  Release 0.102.2 | Any file or directory.  | Linux |
| [radamsa](https://gitlab.com/CinCan/tools/-/tree/master/radamsa) |  Radamsa is a test case generator for robustness testing, a.k.a. a fuzzer. | Any data  | Linux |
| [dex2jar](https://gitlab.com/CinCan/tools/-/tree/master/dex2jar) |  Tool to decompile dex files to jar | APK file  | Linux |
| [twiggy](https://gitlab.com/CinCan/tools/-/tree/master/twiggy) |  Twiggy analyzes a binary's call graph | .wasm, partial ELF & Mach-O support   | Linux |
| [fernflower](https://gitlab.com/CinCan/tools/-/tree/master/fernflower) |  Analytical decompiler for Java | .jar, .class, .zip  | Linux |
| [jd-cmd](https://gitlab.com/CinCan/tools/-/tree/master/jd-cmd) |  The jd-cmd is a simple command line wrapper around JD Core Java Decompiler project. Decompiles .dex and .jar -files to java. | .jar -file  | Linux |
| [cfr](https://gitlab.com/CinCan/tools/-/tree/master/cfr) |  Class File Reader - another java decompiler | .jar -file  | Linux |
| [oledump](https://gitlab.com/CinCan/tools/-/tree/master/oledump) |  A Program to analyse OLE files. | .doc, .xls, .ppt  | Linux |
| [vipermonkey](https://gitlab.com/CinCan/tools/-/tree/master/vipermonkey) |  A VBA parser and emulation engine to analyze malicious macros | .doc, .dot, .docm, .dotm, .xml, .mht, .xls, .xlsm, .xlsb, .pptm, .ppsm, VBA/VBScript source  | Linux |
| [oletools](https://gitlab.com/CinCan/tools/-/tree/master/oletools) |  Oletools - version 0.55.1 | .doc, .dot, .docm, .dotm, .xml, .mht, .xls, .xlsm, .xlsb, .pptm, .ppsm, VBA/VBScript source  | Linux |
| [apktool](https://gitlab.com/CinCan/tools/-/tree/master/apktool) |  A tool for reverse engineering 3rd party, closed, binary Android apps. | .apk, .jar   | Linux |
| [jadx](https://gitlab.com/CinCan/tools/-/tree/master/jadx) |  Dex to Java decompiler | .apk, .dex, .jar, .class, .smali, .zip, .aar, .arsc  | Linux |
| [ilspy](https://gitlab.com/CinCan/tools/-/tree/master/ilspy) |  ILSpy (console only) - version 5.0.2 | .NET Assembly  | Linux |
| [ssdeep](https://gitlab.com/CinCan/tools/-/tree/master/ssdeep) |  Ssdeep | *  | Linux |
| [ssdc](https://gitlab.com/CinCan/tools/-/tree/master/ssdc) |  Ssdeep based clustering tool | *  | Linux |
| [volatility](https://gitlab.com/CinCan/tools/-/tree/master/volatility) |  Volatility |   - Raw linear sample (dd)   - Hibernation file (from Windows 7 and earlier)   - Crash dump file   - VirtualBox ELF64 core dump   - VMware saved state and snapshot files   - EWF format (E01)    - LiME format   - Mach-O file format   - QEMU virtual machine dumps   - Firewire    - HPAK (FDPro)  | Linux |
| [virustotal](https://gitlab.com/CinCan/tools/-/tree/master/virustotal) |  Analyze suspicious files and URLs to detect types of malware |  | Linux |
| [suricata](https://gitlab.com/CinCan/tools/-/tree/master/suricata) |  Suricata  |  | Linux |
| [scrape-website](https://gitlab.com/CinCan/tools/-/tree/master/scrape-website) |  |  | Linux |
| [s3-resource-simple](https://gitlab.com/CinCan/tools/-/tree/master/s3-resource-simple) |  Simple S3 Resource for [Concourse CI](http://concourse.ci) |  | Linux |
| [pdf-tools](https://gitlab.com/CinCan/tools/-/tree/master/pdf-tools) |  The DidierStevensSuite by Didier Stevens |  | Linux |
| [identify-file](https://gitlab.com/CinCan/tools/-/tree/master/identify-file) |  Identify-file |  | Linux |
| [hyperscan](https://gitlab.com/CinCan/tools/-/tree/master/hyperscan) |  High-performance regular expression matching library |  | Linux |
| [dns-tools](https://gitlab.com/CinCan/tools/-/tree/master/dns-tools) |  |  | Linux |
| [c-worker](https://gitlab.com/CinCan/tools/-/tree/master/c-worker) |  Concourse Worker |  | Linux |
| [c-ci](https://gitlab.com/CinCan/tools/-/tree/master/c-ci) |  Concourse CI |  | Linux |
| [add2git-lfs](https://gitlab.com/CinCan/tools/-/tree/master/add2git-lfs) |  ADD2GIT-LFS |  | Linux |
