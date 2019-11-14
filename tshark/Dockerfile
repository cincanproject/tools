FROM alpine:3.10

LABEL MAINTAINER=cincan.io

RUN apk update && apk add --no-cache \
	tshark=3.0.4-r0

ENTRYPOINT ["tshark"]
CMD ["--help"]
