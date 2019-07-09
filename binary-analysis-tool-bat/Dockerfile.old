FROM ubuntu:16.04
RUN apt-get update && apt-get install -y \
        software-properties-common \
        devscripts \
        lintian \
        nano \
        dpkg-dev \
        debhelper \
        build-essential \
        python-software-properties \
        debhelper \
        dh-python \
        python-all \
        python-setuptools \
        wget \
        git \
        python \
        python-pip \
        python-magic \
        zlib1g-dev \
        liblzo2-dev \
        liblzma-dev \
        e2tools \
        squashfs-tools \
        zip \
        unrar \
        cabextract \
        unshield \
        p7zip \
        p7zip-full \
        cpio \
        mtd-utils \
        lzip \
        lzop \
        arj \
        icoutils \
        rpm \
        python-rpm \
        poppler-utils \
        upx-ucl \
        libxml2-utils \
        netpbm \
        lrzip \
        ncompress \
        python-imaging \
        vorbis-tools \
        ctags \
        python-matplotlib \
        python-pydot \
        bsdiff \
        python-reportlab \
        fonts-liberation \
        clamav \
        john \
        python-psycopg2 \
        unzip &&\
        rm -rf /var/lib/apt/lists/*

RUN apt-get update
RUN mkdir -p /tmp/bat/packages/
RUN wget -O bat.zip https://github.com/armijnhemel/binaryanalysis/archive/master.zip
RUN wget -O bat-extratools.zip 
https://github.com/armijnhemel/bat-extratools/archive/master.zip
RUN wget -O /tmp/bat/packages/1-python-support.deb 
https://launchpad.net/ubuntu/+archive/primary/+files/python-support_1.0.15_all.deb
RUN unzip bat.zip
RUN unzip bat-extratools.zip
WORKDIR  /bat-extratools-master
RUN debuild -uc -us
WORKDIR /
RUN mv *.deb 2-bat-extratools.deb
RUN cp *.deb /tmp/bat/packages
WORKDIR /binaryanalysis-master/src
RUN debuild -uc -us
WORKDIR /binaryanalysis-master
RUN mv *.deb 3-bat.deb
RUN cp *.deb /tmp/bat/packages
WORKDIR /tmp/bat/packages
RUN for f in /tmp/bat/packages/*; do echo "Installing $f package" && dpkg -i $f; done
WORKDIR /
ENTRYPOINT ["/usr/bin/bat-scan", "-c", "/etc/bat/bat-scan.config"]
