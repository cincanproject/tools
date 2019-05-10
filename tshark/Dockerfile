FROM alpine:3.9

LABEL MAINTAINER=cincan.io

RUN apk update && apk add --no-cache \
	tshark=2.6.8-r0

ENTRYPOINT ["tshark"]
CMD ["--help"]
