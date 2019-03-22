# Binary Analysis Tool BAT with extra tools

## Supported tags and respective `Dockerfile` links

* `latest` 
([*binary-analysis-tool-bat/Dockerfile*](https://gitlab.com/CinCan/dockerfiles/blob/master/binary-analysis-tool-bat/Dockerfile))

## Usage

***BAT help***

`$ docker run cincan/binary-analysis-tool-bat --help`

***BAT basic usage (for one sample)***

`$ docker run -v /samples:/samples cincan/binary-analysis-tool-bat -b 
/samples/example.bin -o /samples/example_output.gz`

***BAT basic usage (for multiple samples)***

`$ docker run -v /samples:/samples cincan/binary-analysis-tool-bat -d /samples -u 
/samples/output`

## Project homepage

https://github.com/armijnhemel/binaryanalysis
