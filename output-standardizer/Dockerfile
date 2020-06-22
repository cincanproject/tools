#docker run -v /samples:/samples cincan/output-standardizer json -i input.txt -o output.json -t <tool-name>
ARG tool_version=1.0.0

FROM ubuntu:18.04

LABEL MAINTAINER=cincan.io

ARG tool_version
ENV TOOL_VERSION=$tool_version

RUN apt-get update && apt-get install -y \
            git  \
            python3.8 \
            python3-pip \
    && apt-get autoclean \
    && git clone https://gitlab.com/CinCan/tools-output-standardization.git --branch $TOOL_VERSION \
    && cd /tools-output-standardization \
    && python3.8 -m pip install -r requirements.txt \
    && python3.8 -m pip install . \
    && adduser --shell /sbin/nologin --disabled-login --gecos "" appuser \
    && chown appuser:appuser /tools-output-standardization

USER appuser

WORKDIR /tools-output-standardization

ENTRYPOINT ["standardizer"]
