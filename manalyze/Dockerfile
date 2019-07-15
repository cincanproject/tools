# Usage:
# $ docker build <path/to/manalyze/>

FROM debian:9-slim

LABEL MAINTAINER=cincan.io

RUN apt update && apt-get install -y --no-install-recommends \
        libboost-regex-dev \
        libboost-program-options-dev \
        libboost-system-dev \
        libboost-filesystem-dev \
        libssl-dev \
        build-essential \
        cmake \
        git \
        ca-certificates \
    && rm -rf /var/lib/apt/lists/* \
    && git clone https://github.com/JusticeRage/Manalyze.git /root/Manalyze \
    && adduser --shell /sbin/nologin --disabled-login --gecos "" appuser

WORKDIR /root/Manalyze
RUN cmake . && make
ENV PATH="/root/Manalyze/bin:${PATH}"


