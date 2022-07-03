ARG tool_version=1.16.0
FROM debian:10-slim as build
LABEL MAINTAINER=cincan.io

ARG tool_version
ENV TOOL_VERSION=$tool_version
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install --no-install-recommends -y python3-pip && \
    pip3 install --no-cache-dir --user eml-parser==$TOOL_VERSION

FROM debian:10-slim as env

ARG tool_version
ENV TOOL_VERSION=$tool_version

COPY --from=build /root/.local /home/appuser/.local
COPY eml2json.py /home/appuser/.local/bin/eml2json

RUN apt-get update && \
    apt-get install --no-install-recommends -y python3 && \
    adduser --shell /sbin/nologin --disabled-login --gecos "" appuser && \
    mkdir -p /home/appuser/tool && \
    chown -R appuser:appuser /home/appuser/ && \
    rm -rf /var/lib/apt/lists/*

USER appuser
ENV PATH=/home/appuser/.local/bin:$PATH
WORKDIR /home/appuser/tool

COPY meta.json /opt/

ENTRYPOINT ["eml2json"]
CMD ["--help"]
