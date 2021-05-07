ARG tool_version=0.9.5

FROM golang:1.15-buster as build
ARG tool_version
ENV TOOL_VERSION=$tool_version

LABEL MAINTAINER=cincan.io

RUN mkdir /vt && cd /vt && go mod init virustotal \
    && go get -d -v  "github.com/VirusTotal/vt-cli/vt@$TOOL_VERSION" \
    && go build -o /go/bin/vt github.com/VirusTotal/vt-cli/vt

FROM alpine:latest as runtime
COPY --from=build /go/bin/vt /usr/bin/vt

ARG tool_version
ENV TOOL_VERSION=$tool_version

RUN apk update && apk add --no-cache \
    ca-certificates \
    libc6-compat \
    && addgroup -S appuser \
    && adduser -s /sbin/nologin --disabled-password -G appuser appuser


USER appuser

WORKDIR "/home/appuser"
# meta.json should be kept as final modification for layers
COPY meta.json /opt/
ENTRYPOINT ["vt"]
CMD ["--help"]
