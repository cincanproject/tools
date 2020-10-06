# Oletools - version 0.56 to analyze Microsoft OLE2 files

"Oletools is a package of python tools to analyze Microsoft OLE2 files (also called Structured Storage, Compound File Binary Format or Compound Document File Format) Extract and analyse VBA macro source code from Office documents."

Tools have been divided based on the purpose:

### Analysing malicious documents

* oleid: to analyze OLE files to detect specific characteristics usually found in malicious files.
*  olevba: to extract and analyze VBA Macro source code from MS Office documents (OLE and OpenXML).
*  MacroRaptor: to detect malicious VBA Macros
*  msodde: to detect and extract DDE/DDEAUTO links from MS Office documents, RTF and CSV
*  pyxswf: to detect, extract and analyze Flash objects (SWF) that may be embedded in files such as MS Office documents (e.g. Word, Excel) and RTF, which is especially useful for malware analysis.
*  oleobj: to extract embedded objects from OLE files.
  ()  rtfobj: to extract embedded objects from RTF files.

### Analysing the structure of OLE files

* olemeta: to extract all standard properties (metadata) from OLE files.
* oletimes: to extract creation and modification timestamps of all streams and storages.
* oledir: to display all the directory entries of an OLE file, including free and orphaned entries.
* olemap: to display a map of all the sectors in an OLE file.


Descriptions have been taken from the home of oletools: https://github.com/decalage2/oletools 

Note, that olebrowse is **no in use.** We can use only CLI tools from container.

There is script [entrypoint.sh](entrypoint.sh) which is wrapping all of the oletools and providing simple user intefrace to use these tools from the docker container.

## Input

```
.doc, .dot, .docm, .dotm, .xml, .mht, .xls, .xlsm, .xlsb, .pptm, .ppsm, VBA/VBScript source
```

## Output

```
<oletool-based> report
JSON
```

## Usage

### Installation

***Method 1. Clone the repository and build it by yourself***

```
git clone https://gitlab.com/CinCan/tools
cd tools/oletools
docker build . -t cincan/oletools
```

***Method 2. Pull the docker image*** 

```
docker pull cincan/oletools
```

***Method 3. use ['cincan'](https://gitlab.com/CinCan/cincan-command) tool*** 

Follow 'cincan' tool installation steps. If this tool is used, no need to install 'oletools' separately.


### Running


***Method 1. Run with 'cincan' tool:***

Analyse a provided example sample. It can be found from path `_samples/msoffice/very_suspicious.doc` from _samples directory.

Generally, tools are used as: 

`cincan run cincan/oletools <oletoolname> ARGS`

As there are set of tools, the name of specific tool should be given first. Use `--help` option for each tool to get more specific help.

Olevba is used as example tool in this case.


```
cincan run cincan/oletools olevba _samples/msoffice/very_suspicious.doc
```

Get help for specifically this tool:

```
cincan run cincan/oletools olevba --help
```

***Method 2. Run the docker container***

Analyse a sample in directory "/samples".



Olevba is used as example tool in this case.

```
docker run -v /samples:/samples cincan/oletools olevba /samples/suspicious_document.doc
```

Or get possible arguments for general oletools wrapper program:  

```
docker run -v /samples:/samples cincan/oletools --help
```

## Testing

Few tests are included for testing the functionality of container. These contains at least:

  * Test entrypoint
  * Test `--help` option
  * Testing simple analysis for each tool

Tox can be used for testing this tool (run from root of this repository):
```
pip install tox
tox stable/oletools
```

### Sample file
MS Office Word document, which contains macros.  

It was originally created for CriM 2019 CinCan workshop. 

Macros and "payload" of the document is modified in such a way, that document is safe.  
However, some anti-virus engines might still classify it as malicious.

File is located at `_samples/msoffice/very_suspicious.doc`


## Project homepage

https://github.com/decalage2/oletools
