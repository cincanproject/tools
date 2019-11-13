# PDF-parser

PDF-parser tool will parse a PDF document to identify the fundamental elements used in the analyzed file

## Input

```
PDF
```

## Output

```
PDF-parser report
```

## Supported tags and respective `Dockerfile` links

* `latest` ([*pdf-parser/Dockerfile*](https://gitlab.com/CinCan/tools/tree/master/pdf-parser))


## Usage

***1. Clone the repository***

```
git clone https://gitlab.com/CinCan/tools
cd tools/pdf-parser/
```

***2. Build OR pull the docker image*** 

```
docker build . -t cincan/pdf-parser
docker pull cincan/pdf-parser
```

***3. Run the docker container***

Example 1. Analyze a file in directory "/samples":

`$ docker run --rm -v /samples:/samples cincan/pdf-parser /samples/sample.pdf -a`  


Example 2. Analyze a file through filters, and display content for objects withouth streams:  

`$ docker run --rm -v /samples:/samples cincan/pdf-parser /samples/sample.pdf -c --filter`   


Example 3. Run with the cincan command line tool, using &Hex decoder:  

`cincan run pdf-parser ^/samples/sample.pdf -c --filter --decoders=decoder_ah.py`


***Options***
```  
Usage: pdf-parser.py [options] pdf-file|zip-file|url
pdf-parser, use it to parse a PDF document

Options:
  --version             show program's version number and exit
  -h, --help            show this help message and exit
  -m, --man             Print manual
  -s SEARCH, --search=SEARCH
                        string to search in indirect objects (except streams)
  -f, --filter          pass stream object through filters (FlateDecode,
                        ASCIIHexDecode, ASCII85Decode, LZWDecode and
                        RunLengthDecode only)
  -o OBJECT, --object=OBJECT
                        id(s) of indirect object(s) to select, use comma (,)
                        to separate ids (version independent)
  -r REFERENCE, --reference=REFERENCE
                        id of indirect object being referenced (version
                        independent)
  -e ELEMENTS, --elements=ELEMENTS
                        type of elements to select (cxtsi)
  -w, --raw             raw output for data and filters
  -a, --stats           display stats for pdf document
  -t TYPE, --type=TYPE  type of indirect object to select
  -O, --objstm          parse stream of /ObjStm objects
  -v, --verbose         display malformed PDF elements
  -x EXTRACT, --extract=EXTRACT
                        filename to extract malformed content to
  -H, --hash            display hash of objects
  -n, --nocanonicalizedoutput
                        do not canonicalize the output
  -d DUMP, --dump=DUMP  filename to dump stream content to
  -D, --debug           display debug info
  -c, --content         display the content for objects without streams or
                        with streams without filters
  --searchstream=SEARCHSTREAM
                        string to search in streams
  --unfiltered          search in unfiltered streams
  --casesensitive       case sensitive search in streams
  --regex               use regex to search in streams
  --overridingfilters=OVERRIDINGFILTERS
                        override filters with given filters (use raw for the
                        raw stream content)
  -g, --generate        generate a Python program that creates the parsed PDF
                        file
  --generateembedded=GENERATEEMBEDDED
                        generate a Python program that embeds the selected
                        indirect object as a file
  -y YARA, --yara=YARA  YARA rule (or directory or @file) to check streams
                        (can be used with option --unfiltered)
  --yarastrings         Print YARA strings
  --decoders=DECODERS   decoders to load (separate decoders with a comma , ;
                        @file supported)
  --decoderoptions=DECODEROPTIONS
                        options for the decoder
  -k KEY, --key=KEY     key to search in dictionaries


Included decoders:
	decoder_add1
	decoder_ah
	decoder_chr
	decoder_rol1
	decoder_xor1 
```

## Project homepage

[https://github.com/DidierStevens/DidierStevensSuite](https://github.com/DidierStevens/DidierStevensSuite)
