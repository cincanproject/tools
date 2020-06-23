FROM centos:latest


RUN yum -y groupinstall "Development Tools" && yum install -y epel-release 
RUN yum install -y git gcc clang cmake make gcc-c++ upx openssl-devel pcre-dev pcre python2 libpcap yara python-pip jq perl-devel libffi-devel python-devel python-pip automake autoconf libtool libffi-devel python-devel python-pip ssdeep-devel ssdeep-libs

RUN pip install python-magic

#RUN apk add --update alpine-sdk upx openssl-dev pcre-dev pcre build-base bsd-compat-headers musl-dev libc-dev
RUN mkdir build && mkdir samples
COPY pev.tar.gz /build
RUN cd /build && tar xf pev.tar.gz && cd pev && make && make install
COPY trid.tar.gz /build 
RUN cd /build && tar xf trid.tar.gz -C /usr/bin
#COPY salsa.tar.gz /build
#COPY pefile.py /build
#COPY pev.py /build
#RUN cd /build && tar xf salsa.tar.gz

ENV EXIFTOOL 11.16
ENV SSDEEP 2.14.1
ENV LIBDIR /usr/local/lib

COPY Image-ExifTool-11.16.tar.gz /build/exiftool.tar.gz
COPY ssdeep-2.14.1.tar.gz /build

RUN cd /build && tar xf exiftool.tar.gz && cd Image-ExifTool-$EXIFTOOL \
	&& perl Makefile.PL && make test && make install

RUN cd /build && git clone git://github.com/smarnach/pyexiftool.git \
	&& cd pyexiftool && python setup.py install

RUN cd /build && tar xzf ssdeep-$SSDEEP.tar.gz \
  	&& cd ssdeep-$SSDEEP \
  	&& ./configure \
  	&& make \
	&& make install

RUN pip install --upgrade setuptools && pip install ssdeep && pip install hashfile

RUN ln -s /usr/local/lib/libpe.so.1.0 /usr/lib/libpe.so.1 && ldconfig
ENTRYPOINT ["/usr/bin/python", "/build/entrypoint.py","/samples/sample"]

COPY entrypoint.py /build

#docker run -t -i --rm -v /path/to/the.exe:/samples/sample pe_test:latest