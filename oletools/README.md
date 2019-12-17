# "Extract and analyse VBA macro source code from Office documents."

## Input

```
.doc, .dot, .docm, .dotm, .xml, .mht, .xls, .xlsm, .xlsb, .pptm, .ppsm, VBA/VBScript source
```

## Output

```
olevba report
JSON
```

## Supported tags and respective `Dockerfile` links
* `latest` ([*olevba/Dockerfile*](https://gitlab.com/CinCan/dockerfiles/blob/master/olevba/Dockerfile))

## Usage


```
docker run --rm -v /samples:/samples cincan/olevba /samples/<DOC FILE>
```

***Options***  

```
Usage: olevba [options] <filename> [filename2 ...]

Options:
  -h, --help            show this help message and exit
  -r                    find files recursively in subdirectories.
  -z ZIP_PASSWORD, --zip=ZIP_PASSWORD
                        if the file is a zip archive, open all files from it,
                        using the provided password (requires Python 2.6+)
  -f ZIP_FNAME, --zipfname=ZIP_FNAME
                        if the file is a zip archive, file(s) to be opened
                        within the zip. Wildcards * and ? are supported.
                        (default:*)
  -a, --analysis        display only analysis results, not the macro source
                        code
  -c, --code            display only VBA source code, do not analyze it
  --decode              display all the obfuscated strings with their decoded
                        content (Hex, Base64, StrReverse, Dridex, VBA).
  --attr                display the attribute lines at the beginning of VBA
                        source code
  --reveal              display the macro source code after replacing all the
                        obfuscated strings by their decoded content.
  -l LOGLEVEL, --loglevel=LOGLEVEL
                        logging level debug/info/warning/error/critical
                        (default=warning)
  --deobf               Attempt to deobfuscate VBA expressions (slow)
  --relaxed             Do not raise errors if opening of substream fails

  Output mode (mutually exclusive):
    -t, --triage        triage mode, display results as a summary table
                        (default for multiple files)
    -d, --detailed      detailed mode, display full results (default for
                        single file)
    -j, --json          json mode, detailed in json format (never default)
```


## Project homepage

https://github.com/decalage2/oletools/wiki/olevba
