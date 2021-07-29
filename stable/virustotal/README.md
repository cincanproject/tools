# Official CLI for VirusTotal API. Analyze suspicious files and URLs to detect malware.

Official CLI for VirusTotal API. Retrieves file or url results from the VirusTotal database. File, hash, URL/IP can be used for searching.

## Input
```
any file
```

## Output

```
Virustotal report
```

## Supported tags and respective `Dockerfile` links

* `latest` 
([*virustotal/Dockerfile*](https://gitlab.com/CinCan/tools/-/blob/master/stable/virustotal/Dockerfile))

## Usage

***Method 1. Clone the repository and build by yourself***

***1. Clone the repository***

```
git clone https://gitlab.com/CinCan/tools
cd tools/virustotal/
```

***2. Build OR pull the docker image***

```
docker build . -t cincan/virustotal
docker pull cincan/virustotal
```

***3. Run the Docker container***

### Information from hashes

**With `cincan-command` or using Docker**:

Get information about file hash:

```console
cincan run cincan/virustotal -k <APIKEY> file <HASH>
# Or similar with Docker
docker run cincan/virustotal -k <APIKEY> file <HASH>
```

Scans all hashes in the newline delimited file. Note `-i` flag to pass *stdin* into container.

```console
cat hashes.txt | cincan run -i cincan/virustotal -k <APIKEY> file -`
# Same with Docker
cat hashes.txt | docker run -i cincan/virustotal -k <APIKEY> file -
```

### Scan actual file

With cincan-command
```
cincan run cincan/virustotal -k <APIKEY> scan file yourfile.exe 
```
Or Docker:

```
docker run -v /files:/files cincan/virustotal -k <APIKEY> scan file  /files/yourfile.exe 
```

For more information, use `--help` option of the tool.

## Testing
Tox can be used for testing this tool (run from root of this repository):
```
pip install tox
tox stable/virustotal
```

## Project homepage

https://github.com/VirusTotal/vt-cli
