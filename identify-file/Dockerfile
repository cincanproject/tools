FROM debian:9-slim

LABEL MAINTAINER=cincan.io

RUN apt-get update && apt-get install --no-install-recommends -y \
        build-essential \
        libffi-dev \
        python3 \
        libssl-dev \
        python3-magic \
        git \ 
        python3-dev \
        python3-pip \
        libfuzzy-dev \
        && rm -rf /var/lib/apt/lists/* \
        && mkdir build && mkdir samples

COPY pev.tar.gz /build
WORKDIR /build
RUN tar xf pev.tar.gz && cd pev && make && make install
COPY trid.tar.gz /build 
WORKDIR /build
RUN tar xf trid.tar.gz -C /usr/bin

ENV EXIFTOOL 11.16
ENV SSDEEP 2.14.1
ENV LIBDIR /usr/local/lib

COPY Image-ExifTool-11.16.tar.gz /build/exiftool.tar.gz
COPY ssdeep-2.14.1.tar.gz /build

WORKDIR /build
RUN tar xf exiftool.tar.gz && cd Image-ExifTool-$EXIFTOOL \
	&& perl Makefile.PL && make test && make install

WORKDIR /build
RUN git clone git://github.com/smarnach/pyexiftool.git \
	&& cd pyexiftool && python3 setup.py install

WORKDIR /build
RUN tar xzf ssdeep-$SSDEEP.tar.gz

WORKDIR /build/ssdeep-$SSDEEP
RUN ./configure \
    && make \
    && make install \
    && pip3 install --upgrade setuptools \
    && pip3 install wheel \
    && pip3 install \
        hashfile \
        ssdeep \
        python-magic \
    && ln -s /usr/local/lib/libpe.so.1.0 /usr/lib/libpe.so.1 \
    && ldconfig \
    && adduser --shell /sbin/nologin --disabled-login --gecos "" appuser

COPY entrypoint.py /build

USER appuser

ENTRYPOINT ["/usr/bin/python3", "/build/entrypoint.py","/samples/sample"]


#docker run -t -i --rm -v /path/to/the.exe:/samples/sample pe_test:latest
