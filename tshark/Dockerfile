FROM alpine:3.9

LABEL MAINTAINER=cincan.io
LABEL io.cincan.input="application/pcap"
LABEL io.cincan.output="application/json,text/xml"

COPY commands.json /cincan/commands.json

RUN apk update && apk add --no-cache \
	tshark=2.6.9-r0

ENTRYPOINT ["tshark"]
CMD ["--help"]
