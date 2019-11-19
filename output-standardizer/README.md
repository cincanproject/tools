# Output-standardizer

Generate a Markdown report from CinCan project's result files of a specific Concourse pipeline,  

or standardize single tool output data from plain text into to JSON format.  

## Input

```
cincan/binwalk, cincan/pdf2john, cincan/pdfxray_lite, cincan/strings outputs
```

## Output

```
json / markdown
```

## Supported tags and respective `Dockerfile` links

* `latest` ([*output-standardizer/Dockerfile*](https://gitlab.com/CinCan/tools/tree/master/output-standardizer))


## Usage

***1. Clone the repository***

```
git clone https://gitlab.com/CinCan/tools
cd tools/output-standardizer/
```

***2. Build OR pull the docker image*** 

```
docker build . -t cincan/output-standardizer
docker pull cincan/output-standardizer
```

***3. Run the docker container***

Standardize a file in folder "samples":

`$ docker run --rm -v /samples:/samples cincan/output-standardizer json -i output/binwalk_output.txt -o output/binwalk_output_standardized.json -t binwalk
`  



***Options***
```  
usage: standardizer <command> [<args>]

Available commands are:

     markdown       To generate Markdown report of specific type from various tool result files.
     json           To standardize specific tool output into the JSON format.

Tool used to standardize output of various tools in JSON output format or as
Markdown report.

positional arguments:
  command     Subcommand to run. Each command has their own help.

optional arguments:
  -h, --help  show this help message and exit
```

## Project homepage

[https://gitlab.com/CinCan/tools-output-standardization](https://gitlab.com/CinCan/tools-output-standardization)
