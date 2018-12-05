FROM centos:latest


RUN yum install -y epel-release 
RUN yum install -y git gcc clang cmake make gcc-c++ upx openssl-devel pcre-dev pcre python2 libpcap yara python-pip jq

#RUN apk add --update alpine-sdk upx openssl-dev pcre-dev pcre build-base bsd-compat-headers musl-dev libc-dev
RUN mkdir build && mkdir samples
COPY pev.tar.gz /build
RUN cd /build && tar xf pev.tar.gz && cd pev && make && make install
COPY trid.tar.gz /build 
RUN cd /build && tar xf trid.tar.gz -C /usr/bin
COPY salsa.tar.gz /build
COPY entrypoint.py /build
COPY pefile.py /build
COPY pev.py /build
RUN cd /build && tar xf salsa.tar.gz
RUN ln -s /usr/local/lib/libpe.so.1.0 /usr/lib/libpe.so.1 && ldconfig
ENTRYPOINT ["/usr/bin/python", "/build/entrypoint.py","/samples/sample"]


#docker run -t -i --rm -v /path/to/the.exe:/samples/sample pe_test:latest