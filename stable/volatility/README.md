# Volatility - An advanced memory forensics framework

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


## Usage

### Installation

__*Method 1. Clone the repository and build by yourself*__
```
git clone https://gitlab.com/CinCan/tools
cd tools/volatility
docker build . -t cincan/volatility
```

__*Method 2. Pull the docker image*__
```
docker pull cincan/volatility
```
__*Method 3. use 'cincan' tool*__

Follow ['cincan'](https://gitlab.com/CinCan/cincan-command) tool installation steps. If this tool is used, no need to install 'Volatility' separately.
Get a high level summary of a memory sample:  

### Running

__*Method 1. Run the docker container*__

Print help and possible arguments for the program:

`$ docker run cincan/volatility`

Get basic information for a sample `volatility_sample.vmem` in directory `/samples`

`$ docker run --rm -v /samples:/samples -ti cincan/volatility imageinfo -f /samples/volatility_sample.vmem`  

__*Method 2. Run with 'cincan' tool:*__

Print help and possible arguments for the program:
 
`$ cincan run cincan/volatility`

Get basic information for a sample `volatility_sample.vmem` in directory `samples`

`$ cincan run cincan/volatility imageinfo -f samples/volatility_sample.vmem`


See full command reference:


[https://github.com/volatilityfoundation/volatility/wiki/Command-Reference](https://github.com/volatilityfoundation/volatility/wiki/Command-Reference)  

### Testing

Three tests are included for testing the functionality of the container.
* Running the container without any extra parameters
* Running a built-in plugin (imageinfo)
* Running an external plugin (yarascan)

Tox can be used for testing this tool (run from the root of this repository):
```
pip install tox
tox stable/volatility
```

### Sample file

Sample file used for testing is available at

### Project homepage

https://github.com/volatilityfoundation/volatility

### License

[GNU General Public License v2.0](https://github.com/volatilityfoundation/volatility/blob/master/LICENSE.txt)