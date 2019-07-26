# Volatility

## "An advanced memory forensics framework"


## Supported tags and respective `Dockerfile` links

* `latest` ([*volatility/Dockerfile*](https://gitlab.com/CinCan/tools/blob/master/volatility/Dockerfile))

### Input

```
  - Raw linear sample (dd)
  - Hibernation file (from Windows 7 and earlier)
  - Crash dump file
  - VirtualBox ELF64 core dump
  - VMware saved state and snapshot files
  - EWF format (E01) 
  - LiME format
  - Mach-O file format
  - QEMU virtual machine dumps
  - Firewire 
  - HPAK (FDPro)
```

### Output

```
Volatility report
  
(Can also convert files between the formats listed previously)

```


## Usage example:

Get a high level summary of a memory sample:  


`$ docker run --rm -v /samples:/samples -ti cincan/volatility imageinfo -f /samples/sampleimage.vmem`  


See full list of commands:  


[https://github.com/volatilityfoundation/volatility/wiki/Command-Reference](https://github.com/volatilityfoundation/volatility/wiki/Command-Reference)  


## Project homepage

https://github.com/volatilityfoundation/volatility
