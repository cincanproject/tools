# ClamAV virus scanner:  Release 0.102.0

This container is focused on using 'clamscan' client of the ClamAV to make general purpose scans available.


## Input

```
Any file or directory.
```

## Output

```
ClamAV report
```

## Supported tags and respective `Dockerfile` links
* `latest` ([*clamscan/Dockerfile*](Dockerfile))

## Usage

### Installation

***Method 1. Clone the repository and build by yourself***

```
git clone https://gitlab.com/CinCan/tools
cd tools/clamav
docker build . -t cincan/clamav
```

***Method 2. Pull the docker image*** 

```
docker pull cincan/clamav
```

***Method 3. use ['cincan'](https://gitlab.com/CinCan/cincan-command) tool*** 

Follow 'cincan' tool installation steps. If this tool is used, no need to install 'ClamAV' separately.

### Running

***Method 1. Run the docker container***


*Scan all files in a folder:*

```
docker run --rm -v /samples:/samples cincan/clamav -r /samples/
```

*Scan all files, list only infected ones:*

```
docker run --rm -v /samples:/samples cincan/clamav -r -i /samples/
```

Or get all possible arguments for the clamscan client:  

`$ docker run -v /samples:/samples cincan/clamav --help`

***Method 2. Run with 'cincan' tool:***

Analyse a provided some sample. Expecting than samples directory is in current directory:

`$ cincan run cincan/clamav samples/clamav_sample.exe`

Get help for specifically this tool:

`$ cincan run cincan/clamav --help `

## Testing

Few tests are included for testing the functionality of container. These contains at least:

  * Test entrypoint and help command
  * Test scanning for sample file, and partially check produced JSON

Sample file is same than tool [ILSpy](../islpy) is using.

Tox can be used for testing this tool (run from root of this repository):
```
pip install tox
tox clamav
```



## Project homepage

https://www.clamav.net/

## 

Licence

ClamAV itself is distributed under GPLv2. All of the extra code here is distributed under MIT licence.