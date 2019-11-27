# Awesome to-be-dockerized list!


This file contains list of potential tools to be added as docker containers into CinCan repository.

## Digital forensics (14.10.2019 from M)

Tools and other information related directly to digital forensics.

### Cheatsheets and other:

* [SANS](https://digital-forensics.sans.org/community/cheat-sheets)
* [Evidence dump format](https://countuponsecurity.com/2015/11/09/digital-forensics-evidence-acquisition-and-ewf-mounting/)
* [Autopsy - gui for many digital forensics tools (such as The Sleuth Kit)](https://www.sleuthkit.org/autopsy/)

### Tools
* [libvshadow](https://github.com/libyal/libvshadow)
    * Restore points from NTFS image, "timetravelling"
    * Tips for docker: https://stackoverflow.com/a/49021109
* [regripper](https://tools.kali.org/forensics/regripper)
    * Contains scripts for detecting evil patterns in registry

* [plaso](https://github.com/log2timeline/plaso)  
    * Timeline all the things!
  
* [autotimeliner](https://github.com/andreafortuna/autotimeliner)


Need for tool to run ARM linux binaries?
e.g 
  * https://stackoverflow.com/a/37918885

SIFT Workstation (This was really wanted "tool" to get to work with docker?)
* [SIFT Workstation](https://digital-forensics.sans.org/community/downloads)


## Static analysis

* [CIML](https://github.com/mtreinish/ciml)
* [Rekall Forensics](http://www.rekall-forensic.com/)
* [AIL framework](https://github.com/CIRCL/AIL-framework)
* [Android Emulation Toolkit (AET)](https://github.com/nixu-corp/aet)
* [IREC](https://binalyze.com/products/irec-free/)
    * *Supports only Windows operating systems*
    * *Does not have CLI, controlling can be made only via GUI*
* [Assemblyline](https://cyber.gc.ca/en/assemblyline)
* [Viper](https://github.com/viper-framework/viper)
* [MASTIFF](https://git.korelogic.com/mastiff.git/)
* [angr](https://github.com/angr/angr)
* [Strings](https://sourceware.org/binutils/docs/binutils/strings.html)
* [Objdump](https://www.systutorials.com/docs/linux/man/1-objdump/)
* [IDA](https://www.hex-rays.com/products/ida/support/download.shtml)
* [Radare](https://rada.re/r/)
* [JAD](http://www.javadecompilers.com/jad)

## Packer analysis

* [RDG](http://www.rdgsoft.net/)
* [PEiD](https://www.softpedia.com/get/Programming/Packers-Crypters-Protectors/PEiD-updated.shtml)
* [PACKERID](https://code.google.com/archive/p/malwaremustdie/downloads)
* [LANGUAGE 2000](https://farrokhi.net/language/)
    * *Supports only Windows operating systems*
    * *GUI ONLY*
* [ExeScan](https://securityxploded.com/exe-scan.php)
* [Q-UNPACK](https://authorne.info/dkpWMXUXKCVFSgM4OgwdAj4mQlBFC3MDM1N4EFUTHyYzQlsTP3MDMxAjOlQGU3gQBgJAeGNLDxcu)

## Online tools and malware analysis

* [AlienVault](https://www.alienvault.com/)
* [Domaintools](https://www.domaintools.com/)
* [censys](https://censys.io/)
* [Shodan](https://www.shodan.io/)
* [ThreatConnect](https://threatconnect.com/)
* [PassiveTotal](https://www.riskiq.com/products/passivetotal/)
* [VirSCAN](http://www.virscan.org/)
* [malwr (temporarily unavailable)](https://malwr.com/)
* [MalwareViz](https://www.malwareviz.com/)
* [ViCheck](https://www.vicheck.ca/)
* [MetaDefender](https://metadefender.opswat.com/#!/)

## Document analysis

* [OffVis](http://go.microsoft.com/fwlink/?LinkId=158791)
    * *Supports only Windows operating systems*
    * *Does not have CLI, controlling can be made only via GUI*
* [Cryptam](http://www.malwaretracker.com/doc.php)
* [PDF X-RAY](https://github.com/9b/pdfxray_public)
* [origami-pdf](https://code.google.com/archive/p/origami-pdf/)

## Jupyter Notebooks

* [azure-sentinel-notebooks](https://github.com/Azure/Azure-Sentinel-Notebooks) Added 4.11.2019
* [papermill](https://github.com/nteract/papermill) Added 4.11.2019

## Browser malware analysis


## System and file analysis

* [gmer](http://www.gmer.net/)
    * *Supports only Windows operating systems*
    * *Does not have CLI, controlling can be made only via GUI*
* [procdot](http://procdot.com/)
* [RadioGraphy](http://www.security-projects.com/?RadioGraPhy)
* [Noriben](https://github.com/Rurik/Noriben)
* [API Monitor](http://www.rohitab.com/apimonitor)
    * *Supports only Windows operating systems*
    * *Does not have CLI, controlling can be made only via GUI*
* [Sysmon Tools](https://github.com/nshalabi/SysmonTools)
    * *Supports only Windows operating systems*
    * *Does not have CLI, controlling can be made only via GUI*

## Shellcode analysis

* [ShellDetect](https://securityxploded.com/shell-detect.php)
* [libemu](https://github.com/buffer/libemu)

* [Shellcode Analysis](http://www.malwaretracker.com/shellcode.php)
* [jmp2it](https://github.com/adamkramer/jmp2it/)
* [scdbg shellcode analysis](https://isc.sans.edu/diary/rss/24058)

## Feeds

* [PhisTank](https://www.phishtank.com/)
* [Abuse.ch](https://abuse.ch/)
* [VXVault](https://github.com/InfectedPacket/VxVault)

## Memory forensics

HOX!
* [Volatility3](https://github.com/volatilityfoundation/volatility3) Added 4.11.2019

* [Volatilitux](https://code.google.com/archive/p/volatilitux/)
* [LiME](https://github.com/504ensicsLabs/LiME)
* [Memoryze](https://www.fireeye.com/services/freeware/memoryze.html)
* [Redline](https://www.fireeye.com/services/freeware/redline.html)
* [VolUtility](https://github.com/kevthehermit/VolUtility)

## Malware analysis tool lists

* [rshipp github](https://github.com/rshipp/awesome-malware-analysis)
* [hslatman github](https://github.com/hslatman/awesome-threat-intelligence)
* [malware-analyzer.com](http://www.malware-analyzer.com/analysis-tools)
* [malwoverview](https://github.com/alexandreborges/malwoverview) Added (4.11.2019)
* [preframe](https://github.com/guelfoweb/peframe) Added 4.11.2019
    * Static analysis on Portable Executable and generic suspicious file

## Pcap
 * [Zeek / Bro](https://zeek.org/)
 * [molo.ch](https://molo.ch/) Added 4.11.2019

## Log analysis

* [sigma](https://github.com/Neo23x0/sigma)
    * Generic Signature Format for SIEM systems

## Other software

* [Botnet source codes](https://github.com/maestron/botnets)
* [osquery](https://osquery.io/)
* [GTFOBins](https://gtfobins.github.io/#)
* [cuckoo](https://hub.docker.com/r/blacktop/cuckoo/)
* [CAPE](https://github.com/ctxis/CAPE) Added 4.11.2019
    * Sandbox derived from Cuckoo, designed to extract payloads
* [Cortex Analyzer](https://github.com/TheHive-Project/Cortex-Analyzers)
* [DEPENDENCY-TRACK](https://dependencytrack.org/)
* [yara](https://github.com/virustotal/yara)
* [Inav](http://lnav.org/)
* [ANY RUN](https://any.run/)
* [Joe Sandbox](https://www.joesecurity.org/)
* [Sandboxed Execution Environment](https://github.com/F-Secure/see)
* [OllyDbg](http://www.ollydbg.de/)
* [WinDbg](https://docs.microsoft.com/en-us/windows-hardware/drivers/debugger/)
* [WireShark](https://www.wireshark.org/)
* [Hybrid Analysis](https://www.hybrid-analysis.com/)
* [Hashcat](https://www.hashcat.net/)
    * [*dizcza/docker-hashcat By dizcza (Linux)*](https://hub.docker.com/r/dizcza/docker-hashcat)

* [photon](https://github.com/s0md3v/Photon) Added 4.11.2019
    * Crawler for subdomains, URLS, files etc.
