# "A Tool for parsing PCAP and capturing network traffic."

From Wireshark User's Guide:

> TShark is a terminal oriented version of Wireshark designed for capturing and displaying packets when an interactive user interface isn’t necessary or available. It supports the same options as wireshark. For more information on tshark consult your local manual page (man tshark) or the online version.

## Input

```
PCAP, network traffic
```

## Output

```
tshark report, JSON, XML
```

## Supported tags and respective `Dockerfile` links
* `latest` ([*tshark/Dockerfile*](https://gitlab.com/CinCan/dockerfiles/blob/master/tshark/Dockerfile))

## Usage

### Get help

Get command line help of the tool this way, using the
`cincan` (https://gitlab.com/cincan/cincan-command) tool:
```
cincan run cincan/tshark --help
```

or using `docker` directly

```
docker run --rm cincan/tshark --help
```

### Analysing a PCAP file

Analyze the content of a pcap file using the `cincan` tool:

```
cincan run cincan/tshark -r <PCAP-FILE>
```

or using `docker` directly, the sample in absolute directory <SAMPLES>
(e.g. `/home/myname/mysamples``)

```
docker run --rm -v <SAMPLES>:/samples cincan/tshark -r /samples/<PCAP-FILE>
```

### Capturing host traffc

You can capture host traffic from <INTERFACE> the following manner:

```
docker run --rm -v <SAMPLES>:/samples --net host cincan/tshark -i <INTERFACE> -w - > mycapture.pcap
```


## Project homepage

https://github.com/wireshark/wireshark
