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
    && git clone https://github.com/JusticeRage/Manalyze.git /Manalyze \
    && adduser --shell /sbin/nologin --disabled-login --gecos "" appuser

WORKDIR /Manalyze
RUN cmake . && make
ENV PATH="/Manalyze/bin:${PATH}"

USER appuser

ENTRYPOINT ["manalyze"]
CMD ["--help"]
