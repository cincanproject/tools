# "Library to parse .eml files"

## Input

```
eml
```

## Output

```
json
```

## Supported tags and respective `Dockerfile` links
* `latest` ([*eml_parser/Dockerfile*](https://gitlab.com/CinCan/tools/blob/master/eml_parser/Dockerfile))

## Usage

### Get help

Get the
`cincan` (https://gitlab.com/cincan/cincan-command) tool:
```
cincan run cincan/eml_parser mail.eml
```

or using `docker` directly, the sample in absolute directory <SAMPLES>
(e.g. `/home/user/maildata/`)

```
docker run --rm -v <SAMPLES>:/maildata cincan/eml_parser /maildata/mail.eml
```

## Project homepage

https://github.com/GOVCERT-LU/eml_parser
