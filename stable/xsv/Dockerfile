ARG tool_version=0.13.0

FROM alpine:3.11 as build
LABEL MAINTAINER=cincan.io

ARG tool_version
ENV TOOL_VERSION=$tool_version
ENV DEBIAN_FRONTEND=noninteractive

RUN \
  apk add wget && \
  wget -q https://github.com/BurntSushi/xsv/releases/download/$TOOL_VERSION/xsv-$TOOL_VERSION-x86_64-unknown-linux-musl.tar.gz && \
  tar -C / -zxf xsv-*.tar.gz xsv && \
  sha256sum xsv && \
  echo "271e798160472830d7151673383afaba4c37209673f5157cf37e8f5e308f1cac  xsv" | sha256sum -c

FROM alpine:latest as env
COPY --from=build /xsv /xsv

ARG tool_version
ENV TOOL_VERSION=$tool_version
ENV DEBIAN_FRONTEND=noninteractive

RUN chmod +x /xsv && \
    adduser -D appuser && \
    mkdir /home/appuser/tool

USER appuser
WORKDIR /home/appuser/tool
# meta.json should be kept as final modification for layers
COPY meta.json /opt/
ENTRYPOINT ["/xsv"]

