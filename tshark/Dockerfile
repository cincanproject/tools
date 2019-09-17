FROM alpine:3.9

LABEL MAINTAINER=cincan.io
LABEL io.cincan.input="application/vnd.tcpdump.pcap"
LABEL io.cincan.output="application/json,text/xml"

COPY cincan /cincan

RUN apk update && apk add --no-cache \
	tshark=2.6.9-r0

ENTRYPOINT ["tshark"]
CMD ["--help"]
