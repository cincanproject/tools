FROM debian:9-slim

LABEL MAINTAINER=cincan.io

ENV DEBIAN_FRONTEND=noninteractive

RUN mkdir -p /usr/share/man/man1 \
    && mkdir -p /usr/share/man/man1 \
    && apt-get update && apt-get install --no-install-recommends -y \
        wget ca-certificates git build-essential \
        libqt4-opengl \
        mtd-utils=1:2.0.0-1 \ 
        gzip=1.6-5+b1 \
        bzip2=1.0.6-8.1 \
        tar=1.29b-1.1 \
        arj=3.10.22-15 \
        lhasa=0.3.1-2+b1 \
        p7zip \
        p7zip-full \
        cabextract=1.6-1+b1 \
        cramfsswap=1.4.1-1.1 \
        squashfs-tools \
        zlib1g-dev \
        default-jdk \
        liblzma-dev=5.2.2-1.2+b1 \
        liblzo2-dev=2.08-1.2+b2 \
        sleuthkit=4.4.0-5 \
        lzop=1.03-4+b1 \
        srecord=1.58-1.1+b2 \
        cpio \
        python-crypto=2.6.1-7 \
        python-dev \
        python-lzo=1.08-1 \
        python-lzma=0.5.3-3 \
        python-pip \
        python-tk=2.7.13-1 \
        python3-crypto=2.6.1-7 \
        python3-pip \
        python3-tk=3.5.3-1 \
        python-setuptools=33.1.1-1 \
        python=2.7.13-2 \
        python3=3.5.3-1 \
        unzip=6.0-21+deb9u2 && \
        rm -rf /var/lib/apt/lists/* \
    && wget -O binwalk.zip https://github.com/ReFirmLabs/binwalk/archive/master.zip \
    && unzip binwalk.zip
WORKDIR binwalk-master
RUN sed -i 's/"${2:-$(lsb_release -r|cut -f 2|cut -c1-2)}"/18/g' deps.sh \
    && ./deps.sh --yes \
    && python setup.py install \
    && adduser --shell /sbin/nologin --disabled-login --gecos "" appuser

USER appuser

ENTRYPOINT ["/usr/local/bin/binwalk"]
