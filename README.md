[![pipeline status](https://gitlab.com/CinCan/tools/badges/master/pipeline.svg)](https://gitlab.com/CinCan/tools/commits/master)

## Dockerfiles for the CinCan project

This repository will automatically build and publish docker images to Docker Hub using GitLab-CI.

The pipeline will try to build a new image for each directory that **_has changes_** _in the latest commit_.

Actual images can be found from:
[https://hub.docker.com/r/cincan/](https://hub.docker.com/r/cincan/)  

## Practices for creating the tool images

### Dockerfile

Label for maintainer should be added:

`LABEL MAINTAINER=cincan.io`

Each tool should use `ENV` for describing version number of the tool, and use it for installation, if possible. Variable name must be `VERSION`
 * This gives a way for reading version information of the tool from every container, just by checking VERSION environment variable.
 * Dockerfiles can be automatically parsed for documentation, and VERSION information can be acquired in this way.

e.g. `ENV VERSION=1.0` or `ENV VERSION 1.0`

Tool itself should be latest *stable* version, and it is hopefully installed with previously mentioned VERSION environment variable. In this way, we can maintain the actual version of the tool and described version to be identical.

#### Specify dependency versions and base image version

It is preferable to specify dependency package versions as well to maintain repeatability of the builds.

In general, the version tag for base image should be *latest* to ensure upgrades of important security updates. However, if someone feels for being able to follow up of all important security updates, usage of precise version is allowed. 

Recommended base image type is [**Alpine**](https://hub.docker.com/_/alpine) to minimize the size.

#### Use checksums

If something is downloaded in build phase from external source(s) as zip etc., use checksums e.g. SHA256 verification to verify that content is, what it is supposed to be.

Example from Ghidra:
```
ENV GHIDRA_SHA256 3d61de711b7ea18bdee3ed94c31429e4946603b3e7d082cca5e949bbd651f051

RUN wget --progress=bar:force -O /tmp/ghidra.zip https://ghidra-sre.org/ghidra_9.1-BETA_DEV_20190923.zip && \
    echo "$GHIDRA_SHA256 /tmp/ghidra.zip" | sha256sum -c - 
```

#### Image should run as non-root

Create user named as `appuser` and give required permissions for it to run the tool.

Example for Alpine based image:
```shell
addgroup -S appuser && \
adduser -s /sbin/nologin --disabled-password -G appuser appuser
```
Example for Debian based image:
```shell
groupadd -g 1000 appuser && \
useradd -u 1000 -g appuser -s /sbin/nologin appuser
```

Use the user as early as possible with the line `USER appuser` to ensure clean permissions for the image!

Set working directory for home of this user: `WORKDIR "/home/appuser"` and this is preferably empty.

### Testing

At least `entrypoint` and `--help` command should be tested for image.
Possible test(s) could be added for real sample, and preferably at least one will be implemented.

This requires sample file, and it should be:
  * non-malicious
  * free-to-use, preferably created for this purpose

Tests have been implemented by using [*pytest*](https://docs.pytest.org/en/latest/), and the execution is automated with tool named [tox.](https://tox.readthedocs.io/en/latest/)

See reference for [tox.ini](tox.ini)

All tests can be run as:
```
pip install tox
tox
```
Or single test by running:

```
tox <tool-directory-name>
```

Tests are dependant of some the methods of the [cincan tool](https://gitlab.com/CinCan/cincan-command) which is implemented with Python. Currently, at least following methods are available:
  * tool_with_file(\__file__) - make instance of the tool
  * tool.run_get_string([\<POSSIBLE ARGS>]) - for running the tool and getting STDOUT and possible output files

  Thest wrapper named as dockertools is used for actually using the `cincan` tool, see source code in [here.](metatool)


  #### WIP - resolve unused samples from _SAMPLES directory:

  Following magic can be executed in tools root directory:

  ```shell
   find _samples -type f | grep -v "$(find . -name "test_*.py" -exec grep  "SAMPLE_FILE.*=" {} \; | tr -d " \"" | awk -F "=" '{print $2}' | sort | uniq -u)" | xargs rm -d 
  ```

This excepts that variable `SAMPLE_FILE` has been used for defining location of the the sample file(s) in test_*.py file(s). 

In the future, maybe implement testing utility, which should take filename as input, and automatically detects which sample files are unused.

### Licence should be added

If there are no limitations with the licence of the tool, set it as MIT licence. Otherwise, try to be as permissive as possible with tool's own licence.


### Previous leads to following README formatting:

README should describe shortly:
  * The purpose of the tool
  * Format of input files
  * Format of output files
  * How to run the tool with 'cincan' wrapper tool
  * How to run the tool with docker
  * How to run test for this tool, and description of possible sample file
  * Credits for the original creator of the tool
    * Project link
    * Maintainer link, twitter handle?
  * Licence

## Description of the current tools
### Linux tools

| Tool name | Description | Input               | Platform |
|-----------|-------------|---------------------|----------|
| [pastelyzer](https://gitlab.com/CinCan/tools/-/tree/master/pastelyzer) |  the paste analyzer | text  | Linux |
| [shellcode2exe](https://gitlab.com/CinCan/tools/-/tree/master/shellcode2exe) |  Convert shellcodes into executable files, for multiple platforms. | shellcode  | Linux |
| [sleuthkit](https://gitlab.com/CinCan/tools/-/tree/master/sleuthkit) |  Open Source Digital Forensics | raw, ewf, vmdk, vhd  | Linux |
| [vba2graph](https://gitlab.com/CinCan/tools/-/tree/master/vba2graph) |  Generate call graphs from VBA code | office documents such as .doc, .xls, .bas  | Linux |
| [r2-bin-carver](https://gitlab.com/CinCan/tools/-/tree/master/r2-bin-carver) |  R2 bin carver | memory dumps  | Linux |
| [feature_extractor](https://gitlab.com/CinCan/tools/-/tree/master/feature_extractor) |  Feature_extractor | list of possible IoCs  | Linux |
| [trufflehog](https://gitlab.com/CinCan/tools/-/tree/master/trufflehog) |  TruffleHog Searches through git repositories for accidentally committed secrets | git repository  | Linux |
| [keyfinder](https://gitlab.com/CinCan/tools/-/tree/master/keyfinder) |  Keyfinder | filesystem, APK  | Linux |
| [osslsigncode](https://gitlab.com/CinCan/tools/-/tree/master/osslsigncode) |  osslsigncode | exe/sys/dll  | Linux |
| [headless-thunderbird](https://gitlab.com/CinCan/tools/-/tree/master/headless-thunderbird) |  Headless Thunderbird to screenshot email messages | eml  | Linux |
| [eml_parser](https://gitlab.com/CinCan/tools/-/tree/master/eml_parser) |  Library to parse .eml files | eml  | Linux |
| [output-standardizer](https://gitlab.com/CinCan/tools/-/tree/master/output-standardizer) |  Output-standardizer | cincan/binwalk, cincan/pdf2john, cincan/pdfxray_lite, cincan/strings outputs  | Linux |
| [binwalk](https://gitlab.com/CinCan/tools/-/tree/master/binwalk) |  Firmware Analysis Tool | binary  | Linux |
| [binary-analysis-tool-bat](https://gitlab.com/CinCan/tools/-/tree/master/binary-analysis-tool-bat) |  Binary Analysis Tool BAT with extra tools | binary  | Linux |
| [access-log-visualization](https://gitlab.com/CinCan/tools/-/tree/master/access-log-visualization) |  Visualizing webserver's access log data to help detecting malicious activity | access.log (Apache)  | Linux |
| [xmldump](https://gitlab.com/CinCan/tools/-/tree/master/xmldump) |  Parse XML files. | XML  | Linux |
| [regripper](https://gitlab.com/CinCan/tools/-/tree/master/regripper) |  Extract data from Windows registry | Windows registry hive files  | Linux |
| [zsteg](https://gitlab.com/CinCan/tools/-/tree/master/zsteg) |  detect stegano-hidden data in PNG & BMP | PNG, BMP  | Linux |
| [pe-scanner](https://gitlab.com/CinCan/tools/-/tree/master/pe-scanner) |  Get information of a PE (portable executable) file | PE/EXE/DLL  | Linux |
| [manalyze](https://gitlab.com/CinCan/tools/-/tree/master/manalyze) |  Manalyze | PE files  | Linux |
| [python-extract-code](https://gitlab.com/CinCan/tools/-/tree/master/python-extract-code) |  Extract code | PE  | Linux |
| [peframe](https://gitlab.com/CinCan/tools/-/tree/master/peframe) |  PEframe | PE  | Linux |
| [ioc_parser](https://gitlab.com/CinCan/tools/-/tree/master/ioc_parser) |  A tool to extract indicators of compromise from security reports | PDF, txt, xlsx, html  | Linux |
| [pyocr](https://gitlab.com/CinCan/tools/-/tree/master/pyocr) |  Optical character recognition (OCR) wrapper for Tesseract OCR engine | PDF, png, jpg  | Linux |
| [jsunpack-n](https://gitlab.com/CinCan/tools/-/tree/master/jsunpack-n) |  Jsunpack-n | PDF, URL, PCAP, JavaScript, SWF  | Linux |
| [pdfexaminer](https://gitlab.com/CinCan/tools/-/tree/master/pdfexaminer) |  PDFExaminer | PDF files  | Linux |
| [peepdf](https://gitlab.com/CinCan/tools/-/tree/master/peepdf) |  Powerful Python tool to analyze PDF documents. | PDF  | Linux |
| [pdfxray-lite](https://gitlab.com/CinCan/tools/-/tree/master/pdfxray-lite) |  Analyze PDF files | PDF  | Linux |
| [pdfid](https://gitlab.com/CinCan/tools/-/tree/master/pdfid) |  PDFID | PDF  | Linux |
| [pdf-parser](https://gitlab.com/CinCan/tools/-/tree/master/pdf-parser) |  PDF-parser | PDF  | Linux |
| [tshark](https://gitlab.com/CinCan/tools/-/tree/master/tshark) |  A Tool for parsing PCAP and capturing network traffic. | PCAP, network traffic  | Linux |
| [floss](https://gitlab.com/CinCan/tools/-/tree/master/floss) |  FireEye Labs Obfuscated String Solver | Malware with (obfuscated) strings  | Linux |
| [steghide](https://gitlab.com/CinCan/tools/-/tree/master/steghide) |  A Steganography program that is able to hide data (and extract) in various kinds of image- and audio-files. | JPEG, BMP, WAV, AU  | Linux |
| [pywhois](https://gitlab.com/CinCan/tools/-/tree/master/pywhois) |  Pywhois | IP / list of IPs  | Linux |
| [ioc_strings](https://gitlab.com/CinCan/tools/-/tree/master/ioc_strings) |  IOC strings | File/Directory  | Linux |
| [iocextract](https://gitlab.com/CinCan/tools/-/tree/master/iocextract) |  Advanced Indicator of Compromise (IOC) extractor | File  | Linux |
| [pdf2john](https://gitlab.com/CinCan/tools/-/tree/master/pdf2john) |  John the Ripper for extracting hash from PDF files | Encrypted PDF  | Linux |
| [radare2](https://gitlab.com/CinCan/tools/-/tree/master/radare2) |  Radare2 is complete unix-like framework for reverse engineering and binary analysis - version 4.3.1 | ELF, Mach-O, Fatmach-O, PE, PE+, MZ, COFF, OMF, TE, XBE, BIOS/UEFI, Dyldcache, DEX, ART, CGC, Java class, Android boot image, Plan9 executable, ZIMG, MBN/SBL bootloader, ELF coredump, MDMP (Windows minidump), WASM (WebAssembly binary), Commodore VICE emulator, QNX, Game Boy (Advance), Nintendo DS ROMs and Nintendo 3DS FIRMs, various filesystems.  | Linux |
| [snowman-decompile](https://gitlab.com/CinCan/tools/-/tree/master/snowman-decompile) |  Snowman-decompile | ELF Mach-O PE LE  | Linux |
| [flawfinder](https://gitlab.com/CinCan/tools/-/tree/master/flawfinder) |  Finds possible security weaknesses in C/C++ source code | C/C++ code  | Linux |
| [ghidra-decompiler](https://gitlab.com/CinCan/tools/-/tree/master/ghidra-decompiler) |  Ghidra Headless Analyzer - Version 9.1 | Any software binary in native instructions.  | Linux |
| [clamav](https://gitlab.com/CinCan/tools/-/tree/master/clamav) |  ClamAV virus scanner:  Release 0.102.0 | Any file or directory.  | Linux |
| [radamsa](https://gitlab.com/CinCan/tools/-/tree/master/radamsa) |  A Tool for parsing PCAP and capturing network traffic. | Any data  | Linux |
| [dex2jar](https://gitlab.com/CinCan/tools/-/tree/master/dex2jar) |  Tool to decompile dex files to jar | APK file  | Linux |
| [twiggy](https://gitlab.com/CinCan/tools/-/tree/master/twiggy) |  Twiggy analyzes a binary's call graph | .wasm, partial ELF & Mach-O support   | Linux |
| [rtfobj](https://gitlab.com/CinCan/tools/-/tree/master/rtfobj) |  A Python module to detect and extract embedded objects stored in RTF files, such as OLE objects. | .rtf  | Linux |
| [fernflower](https://gitlab.com/CinCan/tools/-/tree/master/fernflower) |  Analytical decompiler for Java | .jar, .class, .zip  | Linux |
| [jd-cmd](https://gitlab.com/CinCan/tools/-/tree/master/jd-cmd) |  The jd-cmd is a simple command line wrapper around JD Core Java Decompiler project. Decompiles .dex and .jar -files to java. | .jar -file  | Linux |
| [oledump](https://gitlab.com/CinCan/tools/-/tree/master/oledump) |  A Program to analyse OLE files. | .doc, .xls, .ppt  | Linux |
| [oletools](https://gitlab.com/CinCan/tools/-/tree/master/oletools) |  Oletools - version 0.55.1 | .doc, .dot, .docm, .dotm, .xml, .mht, .xls, .xlsm, .xlsb, .pptm, .ppsm, VBA/VBScript source  | Linux |
| [apktool](https://gitlab.com/CinCan/tools/-/tree/master/apktool) |  A tool for reverse engineering 3rd party, closed, binary Android apps. | .apk, .jar   | Linux |
| [jadx](https://gitlab.com/CinCan/tools/-/tree/master/jadx) |  Dex to Java decompiler | .apk, .dex, .jar, .class, .smali, .zip, .aar, .arsc  | Linux |
| [ilspy](https://gitlab.com/CinCan/tools/-/tree/master/ilspy) |  ILSpy (console only) - version 5.0.2 | .NET Assembly  | Linux |
| [ssdeep](https://gitlab.com/CinCan/tools/-/tree/master/ssdeep) |  Ssdeep | *  | Linux |
| [ssdc](https://gitlab.com/CinCan/tools/-/tree/master/ssdc) |  Ssdeep based clustering tool | *  | Linux |
| [volatility](https://gitlab.com/CinCan/tools/-/tree/master/volatility) |  Volatility |   - Raw linear sample (dd)   - Hibernation file (from Windows 7 and earlier)   - Crash dump file   - VirtualBox ELF64 core dump   - VMware saved state and snapshot files   - EWF format (E01)    - LiME format   - Mach-O file format   - QEMU virtual machine dumps   - Firewire    - HPAK (FDPro)  | Linux |
| [virustotal](https://gitlab.com/CinCan/tools/-/tree/master/virustotal) |  Analyze suspicious files and URLs to detect types of malware |  | Linux |
| [test2tool](https://gitlab.com/CinCan/tools/-/tree/master/test2tool) |  |  | Linux |
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
### Windows tools

| Tool name | Description | Input               | Platform |
|-----------|-------------|---------------------|----------|
| [sysinternals](https://gitlab.com/CinCan/tools/-/tree/master/sysinternals) |  |  | Windows |
| [sysanalyzer](https://gitlab.com/CinCan/tools/-/tree/master/sysanalyzer) |  Input |  | Windows |
| [regshot](https://gitlab.com/CinCan/tools/-/tree/master/regshot) |  |  | Windows |
| [processhacker](https://gitlab.com/CinCan/tools/-/tree/master/processhacker) |  |  | Windows |
| [pestudio](https://gitlab.com/CinCan/tools/-/tree/master/pestudio) |  |  | Windows |
| [pdf-stream-dumper](https://gitlab.com/CinCan/tools/-/tree/master/pdf-stream-dumper) |  |  | Windows |
| [oledump-win](https://gitlab.com/CinCan/tools/-/tree/master/oledump-win) |  |  | Windows |
| [officemalscanner](https://gitlab.com/CinCan/tools/-/tree/master/officemalscanner) |  |  | Windows |
| [jakstab](https://gitlab.com/CinCan/tools/-/tree/master/jakstab) |  |  | Windows |
| [convertshellcode](https://gitlab.com/CinCan/tools/-/tree/master/convertshellcode) |  |  | Windows |
| [capture-bat](https://gitlab.com/CinCan/tools/-/tree/master/capture-bat) |  |  | Windows |
| [binskim](https://gitlab.com/CinCan/tools/-/tree/master/binskim) |  |  | Windows |
