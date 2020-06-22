# Parse .eml email files

Extract structured JSON data and attachment files from `.eml` files with the
GOVCERT.LU developed python parser module.

Parses interesting headers out of the email, content-types, hashes of email
bodies, IPs, URLs. etc

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

Output mail as json and extract attachments with the
[`cincan`](https://gitlab.com/cincan/cincan-command) tool:

```
cincan run cincan/eml_parser mail.eml -e outputdir
```

or using `docker` directly, the sample in absolute directories <SAMPLES>
and <OUTPUT> respectively
(e.g. `/home/user/maildata/` and `/home/user/maildata/output`)

```
docker run --rm -v <SAMPLES>:/maildata -v <OUTPUT>:/outputdir cincan/eml_parser /maildata/mail.eml -e outputdir
```

## Project homepage

https://github.com/GOVCERT-LU/eml_parser
