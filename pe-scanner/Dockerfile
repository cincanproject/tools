FROM alpine:3.10

LABEL MAINTAINER=cincan.io

RUN apk add --update --no-cache \
        python \
        alpine-sdk \
        upx \
        linux-headers \
        openssl-dev \
        pcre-dev \
        pcre \
        build-base \
        bsd-compat-headers \
        musl-dev libc-dev \
    && mkdir build \
    && mkdir samples

COPY pev.tar.gz /build
COPY trid.tar.gz /build 
COPY salsa.tar.gz /build
COPY entrypoint.py /build
COPY pefile.py /build
COPY pev.py /build

WORKDIR /build
RUN tar xf pev.tar.gz \
    && tar xf trid.tar.gz -C /usr/bin \
    && tar xf salsa.tar.gz
WORKDIR /build/pev 
RUN make \
    && make install

WORKDIR /build
RUN ln -s /usr/local/lib/libpe.so.1.0 /usr/lib/libpe.so.1 \
    && ldconfig /etc/ld.so.conf.d \
    && adduser -s /sbin/login -D appuser

USER appuser

ENTRYPOINT ["/usr/bin/python", "/build/entrypoint.py","/samples/sample"]


#docker run -t -i --rm -v /path/to/the.exe:/samples/sample pe_test:latest
