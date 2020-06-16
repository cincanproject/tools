# "A Tool for parsing PCAP and capturing network traffic."

From Wireshark User's Guide:

> TShark is a terminal oriented version of Wireshark designed for capturing and displaying packets when an interactive user interface isn’t necessary or available. It supports the same options as wireshark. For more information on tshark consult your local manual page (man tshark) or the online version.

The project was started by
Gerald Combs in 1997 and has involved since with the help of a
community of contributors into very versatile tool supporting hundreds
of supported protocols and media formats. Wireshark is the capture and
analysis tool used by network administrators, developers, security
researchers, etc.

## Input

```
PCAP, network traffic
```

## Output

```
tshark report, JSON, XML
```

## Supported tags and respective `Dockerfile` links
* `latest` ([*tshark/Dockerfile*](https://gitlab.com/CinCan/tools/blob/master/tshark/Dockerfile))

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
cincan run --cap-add NET_RAW --cap-add NET_ADMIN --network host cincan/tshark -i <INTERFACE> -w - > traffic.pcap
```


or using docker with identical command line, just replace 'cincan' with 'docker.

## Project homepage

https://github.com/wireshark/wireshark
