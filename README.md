## Dockerfiles for the CinCan project

This repository will automatically build and publish docker images to Docker Hub using GitLab-CI.

The pipeline will try to build a new image for each directory that **_has changes_** _in the latest commit_.

Actual images can be found from:
[https://hub.docker.com/r/cincan/](https://hub.docker.com/r/cincan/)  


## Description of tools

| Tool name                | Description                                        | Input               | Platform |
|--------------------------|----------------------------------------------------|---------------------|----------|
| access-log-visualization | Visualizing webserver's access log data            | access.log (Apache) | Linux    |
| binary-analysis-tool-bat | Binary Analysis Tool BAT with extra tools          | binary              | Linux    |
| binskim                  | A Light-weight PE scanner                          | binary              | Windows  |
| binwalk                  | Firmware analysis tool                             | binary              | Linux    |
| c-ci                     | The Concourse CI                                   |                     | Linux    |
| c-worker                 | The Concourse Worker                               |                     | Linux    |
| capture-bat              | A Behavioral analysis tool of WIN32 apps           |                     | Windows  |
| clamscan                 | ClamAV virus scanner                               | any                 | Linux    |
| convertshellcode         | Shellcode disassembler                             | shellcode           | Windows  |
| dns-tools                |                                                    |                     | Linux    |
| dotnetdecompile          | Decompiler using th ILSpy engine                   | .NET                | Linux    |
| flawfinder               | Scan C/C++ code for security flaws                 | C/C++               | Linux    |
| ghidra-decompiler        |                                                    |                     | Linux    |
| hyperscan                | Regular expression matching library                |                     | Linux    |
| identify-file            | Identifies file type using several techniques      |                     | Linux    |
| iocextract               | Extracts urls, hashes, emails and ips from a file  | any                 | Linux    |
| jakstab                  |                                                    |                     | Windows  |
| jsunpack-n               | Scans URLs and PDFs.                               | PDF,URL,PCAP,JS,SWF | Linux    |
| keyfinder                | Find and analyze key files on a filesystem or APK  | filesystems, APK    | Linux    |
| manalyze                 | A Static analyzer for executables                  | binary              | Linux    |
| officemalscanner         | Scan MS Office files for malicious traces          | DOC, XLS, PPT       | Windows  |
| oledump                  | Analyze MS Office (OLE) files                      | DOC, XLS, PPT       | Windows  | 
| oledump-linux            | Analyze MS Office (OLE) files                      | DOC, XLS, PPT       | Linux    |
| olevba                   | Extract and analyze VBA macros from Office files   | DOC,DOT,DOCM,DOTM,XML,MHT,XLSM,XLSB,PPTM,PPSM,VBA/VBSCRIPT            | Linux    |
| pdf-parser               | Parse PDF to identify the fundamental elements     | PDF                 | Windows  |
| pdf-stream-dumper        | Analyze PDF documents                              | PDF                 | Windows  |
| pdf-tools                | The DidierStevensSuite                             | PDF                 | Linux    |
| pdf2john                 | John The Ripper for extracting hash from PDF       | Encrypted PDF       | Linux    |
| pdfexaminer              | Uploads PDF to www.pdfexaminer.com for scanning    | PDF                 | Linux    |
| pdfid                    | Scan PDFs for keywords, Javascript, auto-open...   | PDF                 | Linux    |
| pdfxray_lite             | Analyze PDFs                                       | PDF                 | Linux    |
| pe-scanner               |                                                    |                     |          |
| peepdf                   | A Powerful python tool to analyze PDFs             | PDF, shellcode      | Linux    |
| pestudio                 | Scan binary files for security related information | EXE,DLL,CPL,OCX...  | Windows  |
| processhacker            | Monitor resources, debug software, detect malware  |                     | Windows  |
| pywhois                  | Retrieve information of IP addresses               | IP                  | Linux    |
| r2-bin-carver            | A Script to carve files from memory dumps          | memory dumps        | Linux    |
| r2-callgraph             | Modificated Radare2 image to analyze binaries      | ELF / PE binary     | Linux    |
| regshot                  | Registry compare utility                           |                     | Windows  |
| rtfobj                   | Detect and extract (OLE) objects in RTF files      | RTF                 | Linux    |
| s3-resource-simple       | A Resource to upload files to S3                   |                     | Linux    |
| scrape-website           |                                                    |                     | Linux    |
| shellcode2exe            | Converts shellcode into executables                | shellcode           | Linux    |
| sleuthkit                | Open source digital forensics                      |                     | Linux    |
| snowman-decompile        | A Native code to C/C++ decompiler                  | ELF Mach-O PE LE    | Linux    |
| suricata                 | Network threat detection engine (IDS, IPS, NSM)    | PCAP,network traffic| Linux    |
| sysanalyzer              | An Automated malcode runtime analysis application  |                     | Windows  |
| sysinternals             | Manage, troubleshoot and diagnose Win systems/apps |                     | Windows  |
| trufflehog               | Search git repos for accidentally committed secrets| git repository      | Linux    |
| tshark                   | Parse PCAP and capture network traffic             | PCAP,network traffic| Linux    |
| twiggy                   | Analyze a binary's call graph                      | .wasm (ELF/Mach-O)  | Linux    |
| vba2graph                | Generate call graphs from VBA code                 | DOC,XLS,BAS         | Linux    |
| virustotal               | Analyze files and URLs to detect malware           | any                 | Linux    |
| volatility               | An Advanced memory forensics framework             | memory samples      | Linux    |
| xmldump                  | Parse XML files                                    | XML                 | Linux    |

