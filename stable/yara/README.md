# Yara - The pattern matching swiss knife 

This image contains `yara` command-line client with some pre-installed rules (https://github.com/Yara-Rules/rules). Rules are updated on rebuilding the image.

Root of the rules repository is in the path `/rules/` inside container.
E.g. path to `index.yar` is `/rules/index.yar`.

"YARA is a tool aimed at (but not limited to) helping malware researchers to identify and classify malware samples. With YARA you can create descriptions of malware families (or whatever you want to describe) based on textual or binary patterns. Each description, a.k.a. rule, consists of a set of strings and a boolean expression which determine its logic."

# Input

```
Any file as target
```

# Output

```
Yara report, possible description of rule match
```

# Usage


### Installation

***Method 1. Clone the repository and build by yourself***

```
git clone https://gitlab.com/CinCan/tools
cd tools/stable/yara
docker build . -t cincan/yara
```

***Method 2. Pull the docker image*** 

```
docker pull cincan/yara
```

***Method 3. use ['cincan'](https://gitlab.com/CinCan/cincan-command) tool*** 

Follow 'cincan' tool installation steps. If this tool is used, no need to install 'yara' separately.

### Running

***Method 1. Run with 'cincan' tool:***

Use `-w` to disable warnings. Example of running all the rules from container:

```
cincan run cincan/yara -w  "/rules/index.yar" samples/msdos/suspicious_dos_sample.exe
```


Get general help for using container:

```
cincan run cincan/yara --help
```


***Method 2. Run the docker container***

Let's expect that we have subfolder in current directory named as 'samples'

```
docker run --rm -v $(pwd)/samples:/samples cincan/yara -w "/rules/index.yar" /samples/suspicious_dos_sample.exe
```

This will make yara to scan the file with all rules.

Consult yara [documentation](https://yara.readthedocs.io/en/stable/commandline.html) for more information!




## Home page

[https://github.com/VirusTotal/yara](https://github.com/VirusTotal/yara)