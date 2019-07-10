FROM debian:stretch-slim

RUN     apt-get update && apt-get install --no-install-recommends -y \
        build-essential libffi-dev python3 libssl-dev python3-magic git python3-dev python3-pip libfuzzy-dev \
        && rm -rf /var/lib/apt/lists/* \
#        alpine-sdk linux-headers upx perl openssl-dev pcre-dev pce build-base bsd-compat-headers musl-dev libc-dev && \
        && mkdir build && mkdir samples
COPY    pev.tar.gz /build
WORKDIR /build
RUN     tar xf pev.tar.gz && cd pev && make && make install
COPY    trid.tar.gz /build 
WORKDIR /build
RUN     tar xf trid.tar.gz -C /usr/bin
#COPY salsa.tar.gz /build
#COPY pefile.py /build
#COPY pev.py /build
#RUN cd /build && tar xf salsa.tar.gz

ENV     EXIFTOOL 11.16
ENV     SSDEEP 2.14.1
ENV     LIBDIR /usr/local/lib

COPY    Image-ExifTool-11.16.tar.gz /build/exiftool.tar.gz
COPY    ssdeep-2.14.1.tar.gz /build

WORKDIR /build
RUN     tar xf exiftool.tar.gz && cd Image-ExifTool-$EXIFTOOL \
	    && perl Makefile.PL && make test && make install

WORKDIR /build
RUN     git clone git://github.com/smarnach/pyexiftool.git \
	    && cd pyexiftool && python3 setup.py install

WORKDIR /build
RUN     tar xzf ssdeep-$SSDEEP.tar.gz

WORKDIR /build/ssdeep-$SSDEEP
RUN     ./configure \
  	    && make \
	    && make install

RUN     pip3 install --upgrade setuptools \
        && pip3 install wheel \
        && pip3 install hashfile \
        && pip3 install ssdeep \
        && pip3 install python-magic

RUN     ln -s /usr/local/lib/libpe.so.1.0 /usr/lib/libpe.so.1 && ldconfig

COPY entrypoint.py /build

ENTRYPOINT ["/usr/bin/python3", "/build/entrypoint.py","/samples/sample"]

#COPY entrypoint.py /build

#docker run -t -i --rm -v /path/to/the.exe:/samples/sample pe_test:latest
