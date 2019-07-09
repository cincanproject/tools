FROM ubuntu:16.04
RUN apt-get update && apt-get install --no-install-recommends -y \
        fakeroot \
        software-properties-common \
        devscripts=2.16.2ubuntu3 \
        lintian=2.5.43 \
        dpkg-dev \
        debhelper=9.20160115ubuntu3\
        build-essential \
        python-software-properties \
        dh-python=2.20151103ubuntu1 \
        python-all \
        python-setuptools=20.7.0-1 \
        wget=1.17.1-1ubuntu1.5 \
        git \
        python \
        python-pip \
        python-magic \
        zlib1g-dev \
        liblzo2-dev=2.08-1.2 \
        liblzma-dev \
        e2tools=0.0.16-6.1 \
        squashfs-tools \
        zip=3.0-11 \
        unrar \
        cabextract=1.6-1 \
        unshield=1.0-1 \
        p7zip \
        p7zip-full \
        cpio \
        mtd-utils=1:1.5.2-1 \
        lzip=1.17-1 \
        lzop=1.03-3.2 \
        arj=3.10.22-14 \
        icoutils=0.31.0-3 \
        rpm \
        python-rpm \
        poppler-utils=0.41.0-0ubuntu1.14 \
        upx-ucl=3.91-1 \
        libxml2-utils \
        netpbm=2:10.0-15.3 \
        lrzip=0.621-1 \
        ncompress=4.2.4.4-15 \
        python-imaging=3.1.2-0ubuntu1.1 \
        vorbis-tools=1.4.0-7ubuntu1 \
        ctags \
        python-matplotlib=1.5.1-1ubuntu1 \
        python-pydot=1.0.28-2 \
        bsdiff=4.3-15 \
        python-reportlab=3.3.0-1 \
        fonts-liberation=1.07.4-1 \
        clamav \
        john=1.8.0-2 \
        python-psycopg2 \
        unzip &&\
        rm -rf /var/lib/apt/lists/*

RUN mkdir -p /tmp/bat/packages/ && \
    wget -O bat.zip https://github.com/armijnhemel/binaryanalysis/archive/master.zip && \
    wget -O bat-extratools.zip https://github.com/armijnhemel/bat-extratools/archive/master.zip && \
    wget -O /tmp/bat/packages/1-python-support.deb https://launchpad.net/ubuntu/+archive/primary/+files/python-support_1.0.15_all.deb && \
    unzip bat.zip && \
    unzip bat-extratools.zip
WORKDIR  /bat-extratools-master
RUN debuild -uc -us
WORKDIR /
RUN mv *.deb 2-bat-extratools.deb && \
    cp *.deb /tmp/bat/packages
WORKDIR /binaryanalysis-master/src
RUN debuild -uc -us
WORKDIR /binaryanalysis-master
RUN mv *.deb 3-bat.deb && \
    cp *.deb /tmp/bat/packages
WORKDIR /tmp/bat/packages
RUN for f in /tmp/bat/packages/*; do echo "Installing $f package" && dpkg -i $f; done

ENTRYPOINT ["/usr/bin/bat-scan", "-c", "/etc/bat/bat-scan.config"]
