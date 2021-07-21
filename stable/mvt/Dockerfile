ARG tool_version=v1.0.11

FROM python:3-slim-buster

ARG tool_version
ENV TOOL_VERSION=$tool_version

LABEL MAINTAINER=cincan.io

RUN apt-get update && apt-get install libusb-1.0-0 && \
    pip3 install mvt==${TOOL_VERSION} && \
    groupadd -g 1000 appuser && \
    useradd -u 1000 -g appuser -s /sbin/nologin -m appuser && \
    rm -rf /var/lib/apt/lists/* /var/cache/apt/archives /tmp/* /var/tmp/*

WORKDIR /home/appuser/
COPY entrypoint.sh .
COPY meta.json /opt/

USER appuser

WORKDIR /home/appuser/tool

ENTRYPOINT [ "bash", "/home/appuser/entrypoint.sh" ]
CMD ["--help"]