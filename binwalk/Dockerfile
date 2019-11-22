FROM debian:10-slim as build

LABEL MAINTAINER=cincan.io

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get -y install --no-install-recommends \
      binwalk arj bzip2 squashfs-tools python3-sip python3-matplotlib python3-olefile ncompress openssl \
      python3-crypto python3-nose binutils && \
      useradd -m -u 1000 -s /sbin/nologin appuser
RUN apt-get -y install wget && \
    wget http://ftp.debian.org/debian/pool/main/c/cramfs/cramfsprogs_1.1-6_amd64.deb && dpkg -i cramfsprogs*.deb && echo ba2963849073766857f5d4cf7b21b09419019a2e07d9008c4af9fef6b48487bf  cramfsprogs_1.1-6_amd64.deb | sha256sum -c && \
    mkdir -p /usr/share/man/man1 && \
    apt-get -y install --no-install-recommends mtd-utils gzip bzip2 tar arj lhasa p7zip p7zip-full cabextract cramfsswap squashfs-tools sleuthkit default-jdk lzop srecord

WORKDIR /home/appuser
USER appuser

ENTRYPOINT ["/usr/bin/binwalk"]
