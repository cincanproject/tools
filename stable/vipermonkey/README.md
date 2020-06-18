# A VBA parser and emulation engine to analyze malicious macros

ViperMonkey is a VBA Emulation engine written in Python, used to analyze and
de-obfuscate VBA Macros contained in Microsoft Office documents.

## Input

```
.doc, .dot, .docm, .dotm, .xml, .mht, .xls, .xlsm, .xlsb, .pptm, .ppsm, VBA/VBScript source
```

## Output

```
ViperMonkey report
```

## Supported tags and respective `Dockerfile` links
* `latest` ([*vipermonkey/Dockerfile*](https://gitlab.com/CinCan/tools/blob/master/vipermonkey/Dockerfile))

## Usage

Using the `cincan` command to analyze a document for macros to stdout:

```
cincan run cincan/vipermonkey sample.doc
```

Using the `docker` command to achieve the same:

```
docker run --rm -v `pwd`:/samples cincan/vipermonkey /samples/sample.doc
```

Display potential IOCs stored in intermediate VBA during emulation (URLs and base64):

```
cincan run cincan/vipermonkey -c sample.doc
```

## Project homepage

https://github.com/decalage2/ViperMonkey
