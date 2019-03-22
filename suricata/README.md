# Suricata is a free and open source, mature, fast and robust network threat 
detection engine

The Suricata engine is capable of real time intrusion detection (IDS), inline 
intrusion prevention (IPS), network security monitoring (NSM) and offline pcap 
processing.

Suricata inspects the network traffic using a powerful and extensive rules and 
signature language, and has powerful Lua scripting support for detection of complex 
threats.

## Supported tags and respective `Dockerfile` links

* `latest` 
([*suricata/Dockerfile*](https://gitlab.com/CinCan/dockerfiles/blob/master/suricata/Dockerfile))

## Usage

***Single pcap file***
```
docker run --rm -v /home/cincan/pcaps:/pcaps \ 
-v /home/cincan/suricata_logs:/logs \
cincan/suricata -r /pcaps/sample.pcap -l /logs
```

***All pcaps in the directory***
```
docker run --rm -v /home/cincan/pcaps:/pcaps \ 
-v /home/cincan/suricata_logs:/logs \
cincan/suricata -r /pcaps -l /logs
```

***Options***
```
-r <path>             : run in pcap file/offline mode
-l <dir>              : default log directory
```
Additional options: 
https://suricata.readthedocs.io/en/suricata-4.1.0/command-line-options.html 

## Project homepage

https://github.com/OISF/suricata

