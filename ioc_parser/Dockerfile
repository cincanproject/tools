FROM debian:10-slim as build

LABEL MAINTAINER=cincan.io

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    build-essential \
    ca-certificates \
    python3-setuptools \
    python3-pip \
    python3-wheel \
    git

# TODO: change to own ioc_parser repo?
RUN pip3 install --user git+https://github.com/SteveClement/ioc_parser

FROM debian:10-slim as env

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    ca-certificates \
    python3 git

RUN adduser --shell /sbin/nologin --disabled-login --gecos "" appuser

COPY --from=build /root/.local /home/appuser/.local
RUN chown -R appuser:appuser /home/appuser/.local/

RUN git clone --depth 1 https://github.com/MISP/PyMISPWarningLists
WORKDIR PyMISPWarningLists
RUN git submodule update --init

COPY whitelistcheck.py whitelistcheck.py
RUN chmod 755 /PyMISPWarningLists/whitelistcheck.py

USER appuser
ENV PATH=/home/appuser/.local/bin:$PATH

ENTRYPOINT ["iocp"]
CMD ["-h"]
