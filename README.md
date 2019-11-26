## Dockerfiles for the CinCan project

This repository will automatically build and publish docker images to Docker Hub using GitLab-CI.

The pipeline will try to build a new image for each directory that **_has changes_** _in the latest commit_.

Actual images can be found from:
[https://hub.docker.com/r/cincan/](https://hub.docker.com/r/cincan/)  

## Practices for creating the tools

### Dockerfile

Label for maintainer should be added:

`LABEL MAINTAINER=cincan.io`

Each tool should use `ENV` for describing version number of the tool, and use it for installation, if possible. Variable name must be `VERSION`
 * This gives a way for reading version information of the tool from every container, just by checking VERSION environment variable.
 * Dockerfiles can be automatically parsed for documentation, and VERSION information can be acquired in this way.

e.g. `ENV VERSION=1.0` or `ENV VERSION 1.0`

Tool itself should be latest *stable* version, and it is hopefully installed with previously mentioned VERSION environment variable. In this way, we can maintain the actual version of the tool and described version to be identical.

It is preferable to specify dependency package versions as well, but not mandatory.

### Image should run as non-root

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

Use the user by adding line close to end: `USER appuser`   

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

`tox <tool-directory-name>`

The tests are dependant of the some methods of the [cincan tool](https://gitlab.com/CinCan/cincan-command) which is implemented with Python. Currently, at least following methods are available:
  * tool_with_file(\__file__) - make instance of the tool
  * run_get_string([\<POSSIBLE ARGS>]) - for running the tool and getting STDOUT and possible output files

### Licence should be added

If there are no limitations with the licence of the tool, set it as MIT licence. Otherwise, try to be as permissive as possible with tool's licence.


### Previous leads to following README formatting:

README should describe shortly:
  * the purpose of the tool
  * format of input files
  * format of output files
  * how to run the tool with 'cincan' wrapper tool
  * how to run the tool with docker
  * How to run test for this tool, and description of possible sample file
  * Credits for the original creator of the tool
    * Project link
    * Maintainer link, twitter handle?
  * Licence

## Description of the current tools

### Linux tools

| Tool name                | Description                                        | Input               | Platform |
|--------------------------|----------------------------------------------------|---------------------|----------|
| **Binary analysis**          |                                                    |                     |          |
| [binary-analysis-tool-bat](https://gitlab.com/CinCan/tools/tree/master/binary-analysis-tool-bat) | Binary Analysis Tool BAT with extra tools          | binary              | Linux    |
| [binwalk](https://gitlab.com/CinCan/tools/tree/master/binwalk)                  | Firmware analysis tool                             | binary              | Linux    |
| [dotnetdecompile](https://gitlab.com/CinCan/tools/tree/master/dotnetdecompile)          | Decompiler using th ILSpy engine                   | .NET                | Linux    |
| [ghidra-decompiler](https://gitlab.com/CinCan/tools/tree/master/ghidra-decompiler)        |                                                    |                     | Linux    |
| [manalyze](https://gitlab.com/CinCan/tools/tree/master/manalyze)                 | A Static analyzer for executables                  | binary              | Linux    |
| [r2-callgraph](https://gitlab.com/CinCan/tools/tree/master/r2-callgraph)             | Modificated Radare2 image to analyze binaries      | ELF / PE binary     | Linux    |
| [snowman-decompile](https://gitlab.com/CinCan/tools/tree/master/snowman-decompile)        | A Native code to C/C++ decompiler                  | ELF Mach-O PE LE    | Linux    |
| [twiggy](https://gitlab.com/CinCan/tools/tree/master/twiggy)                   | Analyze a binary's call graph                      | .wasm (ELF/Mach-O)  | Linux    |
| [peframe](https://gitlab.com/CinCan/tools/tree/master/peframe)               | Static analysis on PE and MS Office documents     | binary                    | Linux    |
| [pe-scanner](https://gitlab.com/CinCan/tools/tree/master/pe-scanner)               |                                                    |                     | Linux    |
| **Memory analysis**          |                                                    |                     |          |
| [r2-bin-carver](https://gitlab.com/CinCan/tools/tree/master/r2-bin-carver)            | A Script to carve files from memory dumps          | memory dumps        | Linux    |
| [volatility](https://gitlab.com/CinCan/tools/tree/master/volatility)               | An Advanced memory forensics framework             | memory samples      | Linux    |
| **Network analysis**         |                                                    |                     |          |
| [dns-tools](https://gitlab.com/CinCan/tools/tree/master/dns-tools)                |                                                    |                     | Linux    |
| [scrape-website](https://gitlab.com/CinCan/tools/tree/master/scrape-website)           |                                                    |                     | Linux    |
| [suricata](https://gitlab.com/CinCan/tools/tree/master/suricata)                 | Network threat detection engine (IDS, IPS, NSM)    | PCAP,network traffic| Linux    |
| [tshark](https://gitlab.com/CinCan/tools/tree/master/tshark)                   | Parse PCAP and capture network traffic             | PCAP,network traffic| Linux    |
| [pywhois](https://gitlab.com/CinCan/tools/tree/master/pywhois)                  | Retrieve information of IP addresses               | IP                  | Linux    |
| **Shellcode analysis**       |                                                    |                     |          |
| [shellcode2exe](https://gitlab.com/CinCan/tools/tree/master/shellcode2exe)            | Converts shellcode into executables                | shellcode           | Linux    |
| **Document analysis**        |                                                    |                     |          |
| [jsunpack-n](https://gitlab.com/CinCan/tools/tree/master/jsunpack-n)               | Scans URLs and PDFs.                               | PDF,URL,PCAP,JS,SWF | Linux    |
| [oledump](https://gitlab.com/CinCan/tools/tree/master/oledump)            | Analyze MS Office (OLE) files                      | DOC, XLS, PPT       | Linux    |
| [olevba](https://gitlab.com/CinCan/tools/tree/master/olevba)                   | Extract and analyze VBA macros from Office files   | DOC,DOT,XML,PPTM,VBA| Linux    |
| [pdf-tools](https://gitlab.com/CinCan/tools/tree/master/pdf-tools)                | The DidierStevensSuite                             | PDF                 | Linux    |
| [pdf2john](https://gitlab.com/CinCan/tools/tree/master/pdf2john)                 | John The Ripper for extracting hash from PDF       | Encrypted PDF       | Linux    |
| [pdfexaminer](https://gitlab.com/CinCan/tools/tree/master/pdfexaminer)              | Uploads PDF to www.pdfexaminer.com for scanning    | PDF                 | Linux    |
| [pdfid](https://gitlab.com/CinCan/tools/tree/master/pdfid)                    | Scan PDFs for keywords, Javascript, auto-open...   | PDF                 | Linux    |
| [pdfxray-lite](https://gitlab.com/CinCan/tools/tree/master/pdfxray-lite)             | Analyze PDFs                                       | PDF                 | Linux    |
| [peepdf](https://gitlab.com/CinCan/tools/tree/master/peepdf)                   | A Powerful python tool to analyze PDFs             | PDF, shellcode      | Linux    |
| [rtfobj](https://gitlab.com/CinCan/tools/tree/master/rtfobj)                   | Detect and extract (OLE) objects in RTF files      | RTF                 | Linux    |
| [vba2graph](https://gitlab.com/CinCan/tools/tree/master/vba2graph)                | Generate call graphs from VBA code                 | DOC,XLS,BAS         | Linux    |
| **APK analysis tools**                    |                                                    |                     |          |
| [apktool](https://gitlab.com/CinCan/tools/tree/master/apktool) | A tool for reverse engineering 3rd party, closed, binary Android app     | .apk | Linux    |
| [dex2jar](https://gitlab.com/CinCan/tools/tree/master/dex2jar) | Tool to decompile dex files to jar         | .dex, .apk | Linux    |
| [jd-cmd](https://gitlab.com/CinCan/tools/tree/master/jd-cmd) | Decompiles .dex and .jar -files to java.            | .dex, .jar | Linux    |
| [jadx](https://gitlab.com/CinCan/tools/tree/master/jadx) | Dex to Java decompiler            | .dex, .jar | Linux    |
| **Other**                    |                                                    |                     |          |
| [access-log-visualization](https://gitlab.com/CinCan/tools/tree/master/access-log-visualization) | Visualizing webserver's access log data            | access.log (Apache) | Linux    |
| [c-ci](https://gitlab.com/CinCan/tools/tree/master/c-ci)                     | The Concourse CI                                   |                     | Linux    |
| [c-worker](https://gitlab.com/CinCan/tools/tree/master/c-worker)                 | The Concourse Worker                               |                     | Linux    |
| [clamscan](https://gitlab.com/CinCan/tools/tree/master/clamscan)                 | ClamAV virus scanner                               | any                 | Linux    |
| [flawfinder](https://gitlab.com/CinCan/tools/tree/master/flawfinder)               | Scan C/C++ code for security flaws                 | C/C++               | Linux    |
| [hyperscan](https://gitlab.com/CinCan/tools/tree/master/hyperscan)                | Regular expression matching library                |                     | Linux    |
| [identify-file](https://gitlab.com/CinCan/tools/tree/master/identify-file)            | Identifies file type using several techniques      |                     | Linux    |
| [iocextract](https://gitlab.com/CinCan/tools/tree/master/iocextract)               | Extracts urls, hashes, emails and ips from a file  | any                 | Linux    |
| [ioc_strings](https://gitlab.com/CinCan/tools/tree/master/ioc_strings)               | Extracts urls, hashes, emails, ips, domains and base64 (other) from a file.  | any                 | Linux    |
| [keyfinder](https://gitlab.com/CinCan/tools/tree/master/keyfinder)                | Find and analyze key files on a filesystem or APK  | filesystems, APK    | Linux    |
| [s3-resource-simple](https://gitlab.com/CinCan/tools/tree/master/s3-resource)       | A Resource to upload files to S3                   |                     | Linux    |
| [sleuthkit](https://gitlab.com/CinCan/tools/tree/master/sleuthkit)                | Open source digital forensics                      |                     | Linux    |
| [trufflehog](https://gitlab.com/CinCan/tools/tree/master/trufflehog)               | Search git repos for accidentally committed secrets| git repository      | Linux    |
| [virustotal](https://gitlab.com/CinCan/tools/tree/master/virustotal)               | Analyze files and URLs to detect malware           | any                 | Linux    |
| [xmldump](https://gitlab.com/CinCan/tools/tree/master/xmldump)                  | Parse XML files                                    | XML                 | Linux    |


### Windows tools

| **Binary analysis**          |                                                    |                     |          |
|--------------------------|----------------------------------------------------|---------------------|----------|
| [binskim](https://gitlab.com/CinCan/tools/tree/master/binskim)                  | A Light-weight PE scanner                          | binary              | Windows  |
| [jakstab](https://gitlab.com/CinCan/tools/tree/master/jakstab)                  | Analyze executables,recover control flow graphs    | ELF / PE binary     | Windows  |
| [pestudio](https://gitlab.com/CinCan/tools/tree/master/pestudio)                 | Scan binary files for security related information | EXE,DLL,CPL,OCX...  | Windows  |
| **System and file analysis** |                                                    |                     |          |
| [capture-bat](https://gitlab.com/CinCan/tools/tree/master/capture-bat)              | A Behavioral analysis tool of WIN32 apps           |                     | Windows  |
| [processhacker](https://gitlab.com/CinCan/tools/tree/master/processhacker)            | Monitor resources, debug software, detect malware  |                     | Windows  |
| [regshot](https://gitlab.com/CinCan/tools/tree/master/regshot)                  | Registry compare utility                           |                     | Windows  |
| [sysanalyzer](https://gitlab.com/CinCan/tools/tree/master/sysanalyzer)              | An Automated malcode runtime analysis application  |                     | Windows  |
| [sysinternals](https://gitlab.com/CinCan/tools/tree/master/sysinternals)             | Manage, troubleshoot and diagnose Win systems/apps |                     | Windows  |
| **Shellcode analysis**       |                                                    |                     |          |
| [convertshellcode](https://gitlab.com/CinCan/tools/tree/master/convertshellcode)         | Shellcode disassembler                             | shellcode           | Windows  |
| **Document analysis**        |                                                    |                     |          |
| [officemalscanner](https://gitlab.com/CinCan/tools/tree/master/officemalscanner)         | Scan MS Office files for malicious traces          | DOC, XLS, PPT       | Windows  |
| [oledump-win](https://gitlab.com/CinCan/tools/tree/master/oledump-win)                  | Analyze MS Office (OLE) files                      | DOC, XLS, PPT       | Windows  | 
| [pdf-parser](https://gitlab.com/CinCan/tools/tree/master/pdf-parser)               | Parse PDF to identify the fundamental elements     | PDF                 | Windows  |
| [pdf-stream-dumper](https://gitlab.com/CinCan/tools/tree/master/pdf-stream-dumper)        | Analyze PDF documents                              | PDF                 | Windows  |


