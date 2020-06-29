# "A tool to extract indicators of compromise from security reports"

## Input

```
PDF, txt, xlsx, html
```

## Output

```
csv, tsv, json, yara, netflow
```

## Supported tags and respective `Dockerfile` links
* `latest` ([*ioc_parser/Dockerfile*](https://gitlab.com/CinCan/tools/blob/master/ioc_parser/Dockerfile))

## Usage

### Get help

Get the
`cincan` (https://gitlab.com/cincan/cincan-command) tool:
```
cincan run cincan/ioc_parser -h
```

or using `docker` directly

```
docker run --rm cincan/ioc_parser -h
```

### Extract IOCs from PDF

Extract IOCs from a PDF file using the `cincan` tool:

```
cincan run cincan/ioc_parser /samples/ioc.pdf
```

or using `docker` directly, the sample in absolute directory <SAMPLES>
(e.g. `/home/myname/mysamples``)

```
docker run --rm -v <SAMPLES>:/samples cincan/ioc_parser /samples/ioc.pdf
```

## Project homepage

https://github.com/SteveClement/ioc_parser
