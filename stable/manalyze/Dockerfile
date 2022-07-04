ARG tool_version=42e91de76ac2161a1eced915cc42f4fba36043a3

FROM debian:10-slim as build
LABEL MAINTAINER=cincan.io

ARG tool_version
ENV TOOL_VERSION=$tool_version

RUN apt-get update && apt-get install -y --no-install-recommends \
    libboost-regex-dev \
    libboost-program-options-dev \
    libboost-system-dev \
    libboost-filesystem-dev \
    libssl-dev \
    build-essential \
    cmake \
    git \
    ca-certificates

RUN git clone --depth=1 https://github.com/JusticeRage/Manalyze.git /Manalyze && \
    cd /Manalyze && \
    git checkout -b tool "${TOOL_VERSION}" && cmake . && make && make install

FROM debian:10-slim as env

ARG tool_version
ENV TOOL_VERSION=$tool_version

COPY --from=build /usr/local/bin /usr/local/bin
COPY --from=build /usr/local/lib /usr/local/lib
COPY --from=build /etc/manalyze /etc/manalyze

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    libboost-regex1.67-dev \
    libboost-program-options1.67.0 \
    libboost-system1.67.0 \
    libboost-filesystem1.67.0 \
    libssl1.1 && \
    ldconfig && \
    adduser --shell /sbin/nologin --disabled-login --gecos "" appuser && \
    mkdir -p /home/appuser/tool

USER appuser
WORKDIR /home/appuser/tool

COPY meta.json /opt/

ENTRYPOINT ["manalyze"]
CMD ["--help"]
