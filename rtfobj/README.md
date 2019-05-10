# "A Python module to detect and extract embedded objects stored in RTF files, such as OLE objects."

## Input

```
.rtf
```

## Output

```
rtfobj report
```

## Supported tags and respective `Dockerfile` links
* `latest` ([*rtfobj/Dockerfile*](https://gitlab.com/CinCan/dockerfiles/blob/master/rtfobj/Dockerfile))

## Usage


*** Detect embedded objects ***
```
docker run --rm -v /samples:/samples cincan/rtfobj /samples/<DOC FILE>
```

*** Extract object number 0 ***
```
docker run --rm -v /samples:/samples cincan/rtfobj /samples/<DOC FILE> -s 0
```

***Options***  

```
rtfobj 0.50 - http://decalage.info/python/oletools
THIS IS WORK IN PROGRESS - Check updates regularly!
Please report any issue at https://github.com/decalage2/oletools/issues

Usage: rtfobj [options] <filename> [filename2 ...]

Options:
  -h, --help            show this help message and exit
  -r                    find files recursively in subdirectories.
  -z ZIP_PASSWORD, --zip=ZIP_PASSWORD
                        if the file is a zip archive, open first file from it,
                        using the provided password (requires Python 2.6+)
  -f ZIP_FNAME, --zipfname=ZIP_FNAME
                        if the file is a zip archive, file(s) to be opened
                        within the zip. Wildcards * and ? are supported.
                        (default:*)
  -l LOGLEVEL, --loglevel=LOGLEVEL
                        logging level debug/info/warning/error/critical
                        (default=warning)
  -s SAVE_OBJECT, --save=SAVE_OBJECT
                        Save the object corresponding to the provided number
                        to a file, for example "-s 2". Use "-s all" to save
                        all objects at once.
  -d OUTPUT_DIR         use specified directory to save output files.```


## Project homepage

https://github.com/decalage2/oletools/wiki/rtfobj
