ARG tool_version=1.11.6
FROM python:3-slim-buster as build

LABEL MAINTAINER=cincan.io

ARG tool_version
ENV TOOL_VERSION=$tool_version
ENV DEBIAN_FRONTEND=noninteractive

RUN pip3 install --user eml-parser==$TOOL_VERSION

FROM python:3-slim-buster as env

ARG tool_version
ENV TOOL_VERSION=$tool_version

RUN  adduser --shell /sbin/nologin --disabled-login --gecos "" appuser

COPY --from=build /root/.local /home/appuser/.local
COPY eml_to_json.py /home/appuser/.local/bin/eml2json

RUN mkdir -p /home/appuser/tool && \
    chown -R appuser:appuser /home/appuser/ && \
    chmod +x /home/appuser/.local/bin/eml2json

USER appuser
ENV PATH=/home/appuser/.local/bin:$PATH
WORKDIR /home/appuser/tool

ENTRYPOINT ["eml2json"]
CMD ["--help"]
