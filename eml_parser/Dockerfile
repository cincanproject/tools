FROM python:3-slim-buster as build

LABEL MAINTAINER=cincan.io

ENV DEBIAN_FRONTEND=noninteractive

RUN pip3 install --user eml-parser==1.11.6

FROM python:3-slim-buster as env

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
