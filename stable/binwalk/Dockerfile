ARG tool_version=3154b0012e7dbaf2b20edd5c0a2350ec64009869

FROM debian:10-slim as build

LABEL MAINTAINER=cincan.io
ARG tool_version
ENV TOOL_VERSION=$tool_version

ENV DEBIAN_FRONTEND=noninteractive

ENV CRAMFS=http://ftp.debian.org/debian/pool/main/c/cramfs/cramfsprogs_1.1-6_amd64.deb
ENV CRAMFS_SHA256=ba2963849073766857f5d4cf7b21b09419019a2e07d9008c4af9fef6b48487bf

ENV STUFFIT=http://downloads.tuxfamily.org/sdtraces/stuffit520.611linux-i386.tar.gz
ENV STUFFIT_SHA256=69ccd8659000f7cdeba640157ed42e360b2e448c8e8333b1db491f2c4daf7998

ENV UBIREADER=0955e6b95f07d849a182125919a1f2b6790d5b51

RUN apt-get update && apt-get -y install --no-install-recommends \
    git sudo build-essential wget unzip ca-certificates \
    mtd-utils gzip bzip2 tar arj lhasa p7zip p7zip-full \
    cabextract util-linux cramfsswap squashfs-tools \
    zlib1g-dev liblzma-dev liblzo2-dev \
    sleuthkit fastjar lzop cpio \
    python-setuptools python-wheel python-crypto python-lzo python-lzma python-pip \
    python3-crypto python3-pip python3-setuptools python3-dev python3-wheel && \
    \
    wget -q -O cramfsprogs.deb $CRAMFS && \
    dpkg -i cramfsprogs.deb && \
    echo $CRAMFS_SHA256  cramfsprogs.deb | sha256sum -c && \
    rm cramfsprogs.deb && \
    \
    mkdir -p /usr/share/man/man1 && \
    wget https://github.com/ReFirmLabs/binwalk/archive/$TOOL_VERSION.zip -q -O binwalk.zip && \
    unzip -q binwalk.zip && \
    rm binwalk.zip && \
    mv binwalk-$TOOL_VERSION binwalk && \
    cd binwalk && \
    \
    pip3 install matplotlib capstone && \
    \
    git clone --depth=1 https://github.com/devttys0/sasquatch && \
    (cd sasquatch && ./build.sh) && \
    \
    git clone --depth=1 https://github.com/devttys0/yaffshiv && \
    (cd yaffshiv && python2 setup.py install) && \
    \
    git clone --depth=1 https://github.com/sviehb/jefferson && \
    (cd jefferson && pip3 install -r requirements.txt && python3 setup.py install) && \
    \
    mkdir -p unstuff && \
    (cd unstuff && \
    wget -q -O stuffit.tar.gz $STUFFIT && \
    echo $STUFFIT_SHA256  stuffit.tar.gz | sha256sum -c && \
    tar -xzf stuffit.tar.gz && \
    cp bin/unstuff /usr/local/bin/) && \
    \
    git clone https://github.com/jrspruitt/ubi_reader && \
    (cd ubi_reader && git reset --hard 0955e6b95f07d849a182125919a1f2b6790d5b51 && python setup.py install) && \
    \
    python3 setup.py install && \
    cd / && \
    rm -rf /binwalk/ && \
    apt remove -y git build-essential manpages manpages-dev python3-dev python2-dev python-pip python3-pip wget && \
    apt autoremove -y && \
    rm -rf /var/lib/apt/lists/* && \
    useradd -m -u 1000 -s /sbin/nologin appuser

WORKDIR /home/appuser
USER appuser

# dummy run because it creates some files on first run in home dir
RUN binwalk -h > /dev/null

ENTRYPOINT ["binwalk"]
