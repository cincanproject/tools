## Tool metadata

CinCan project aims to ease up using various incident investigation tools. 
One way for this is to *Dockerize* the tools.

CinCan project is also adding metadata
about the input and output formats a tool supports.
This allows to seek the tools which are relevant to a particular data processing use case.

Further, the metadata can contain "hints" how the tool may be invoked to process
data of particular format. The hints can be used as basis of invoking the tool, 
but allow also creation of harmonized command line which is the same for all tools.

### Supported input and output formats

The supported input and output formats are described as labels inside the Docker container.
Labels can be extracted from image registry without downloading the docker images,
which allows a search over all images in a registry.

The supported input formats are listed as comma-separated list by label 
`io.cincan.input` and the output formats by label `io.cincan.output`.
For example, this is snipped from `Dockerfile` for the tool *tshark*:

    LABEL io.cincan.input="application/pcap"
    LABEL io.cincan.output="application/json,text/xml"

The formats are identified by strings, which are defined using the following process:

 1. Use registered file types by IANA
 (https://www.iana.org/assignments/media-types/media-types.xhtml).
 
 2. Use type names used by TheHive/Cortex
 (https://github.com/TheHive-Project/CortexDocs/blob/master/api/how-to-create-an-analyzer.md#datatypelist)
 
 3. Make a up type name
 
#### Incomplete list of media types 

The following lists some media types encountered when defining input/output formats
in the Cincan project

| Type                               | Description                             |
|------------------------------------|-----------------------------------------|
| application/json                   | JSON formatted data                     |
| application/pdf                    | PDF document                            |
| application/vnd.tcpdump.pcap       | PCAP traffic capture                    |
| application/zip                    | ZIP compressed file                     |
| ip                                 | IP address                              |
| text/plain                         | Plain text data                         |
| text/xml                           | XML formatted data                      |

### Tool hints

Test tool hints are in `cincan` directory in file `commands.json`.
The directory and the file must be copied into the Docker image in following manner:

    COPY cincan /cincan

The commands file is JSON formatted with following kind of structure (from *tshark* tool):

    {
      "commands": [
        {
          "command": ["-r", "<file>", "-Tjson"],
          "input": "application/vnd.tcpdump.pcap",
          "output": "application/json"
        }, {
          "command": ["-r", "<file>", "-Tpdml"],
          "input": "application/vnd.tcpdump.pcap",
          "output": "text/xml"
        }
      ]
    }

