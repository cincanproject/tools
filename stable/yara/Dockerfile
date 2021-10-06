ARG tool_version=v4.1.2
FROM debian:buster-slim as build

LABEL MAINTAINER=cincan.io

ARG tool_version
ENV TOOL_VERSION=$tool_version

RUN apt-get update && apt-get install -y \
    git  \
    automake \
    libtool \
    make \
    gcc \
    pkg-config \
    libssl-dev \
    libmagic-dev \
    libjansson-dev \
    flex \
    && git clone --depth 1 --branch "${TOOL_VERSION}" https://github.com/VirusTotal/yara.git /yara \
    && git clone --depth 1 https://github.com/Yara-Rules/rules.git /rules \
    && cd /yara \
    && ./bootstrap.sh \
    && ./configure --enable-cuckoo --enable-magic --enable-dotnet \
    && make && make install && make check \
    && apt-get --purge autoremove -y git automake libtool make gcc pkg-config \
    && apt-get clean \
    && rm -rf /yara /var/lib/apt/lists/* /var/cache/apt/archives /tmp/* /var/tmp/* \
    && groupadd -g 1000 appuser  \
    && useradd -u 1000 -g appuser -s /sbin/nologin appuser

USER appuser
WORKDIR /home/appuser

# meta.json should be kept as final modification for layers
COPY meta.json /opt/
ENTRYPOINT [ "yara" ]
CMD [ "--help" ]
