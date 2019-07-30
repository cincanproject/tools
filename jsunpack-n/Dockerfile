# docker build -t cincan/jsunpack-n .
#
# File scan:
# docker run -v /samples:/samples cincan/jsunpack-n /samples/input/sample.pdf -d /samples/output
#
# Url scan:
# docker run -v /samples:/samples cincan/jsunpack-n -u https://<TARGET.URL> -d /samples/output -V

FROM debian:9-slim

LABEL MAINTAINER=cincan.io

RUN apt-get update && apt-get install -y --no-install-recommends \
	    python \
        gcc \
        g++ \
        make \
        python-dev \
        git \
	    libpcap-dev \
	    pkg-config \
	    python-dev \
	    libgtk2.0-dev \
	    libnet1-dev \
	    libpcre3 \
	    libpcre3-dev \
	    python-magic \
	    python-pygraphviz \
        libboost-all-dev \
	    wget \
        ca-certificates \ 
    && rm -rf /var/lib/apt/lists/* \
    && git clone https://github.com/urule99/jsunpack-n.git

WORKDIR /jsunpack-n/depends
RUN tar xvfz pynids-0.6.1.tar.gz \
    && tar xvfz js-1.8.0-rc1-src.tar.gz \
    && tar xvfz yara-1.6.tar.gz \
    && tar xvfz yara-python-1.6.tar.gz \
    && tar xvzf BeautifulSoup-3.2.0.tar.gz \
    && tar xvzf pycrypto-2.4.1.tar.gz \
    && wget https://storage.googleapis.com/google-code-archive-downloads/v2/code.google.com/yapgvb/yapgvb-1.2.3-source.tar.gz \
	&& tar zxvf yapgvb-1.2.3-source.tar.gz \
    && adduser --shell /sbin/nologin --disabled-login --gecos "" appuser

WORKDIR /jsunpack-n/depends/pynids-0.6.1 
RUN python setup.py build \
    && python setup.py install

WORKDIR /jsunpack-n/depends/js-1.8.0-rc1-src
RUN make BUILD_OPT=1 -f Makefile.ref \
    && echo "export $PATH=" \
    && make BUILD_OPT=1 JS_DIST=/usr/local -f Makefile.ref export 

WORKDIR /jsunpack-n/depends/yara-1.6
RUN  ./configure \
    && make \
    && make install \
    && echo "/usr/local/lib" >> /etc/ld.so.conf \
    && ldconfig

WORKDIR /jsunpack-n/depends/yara-python-1.6
RUN python setup.py build \
    && python setup.py install

WORKDIR /jsunpack-n/depends/BeautifulSoup-3.2.0
RUN python setup.py build \
    && python setup.py install

WORKDIR /jsunpack-n/depends/pycrypto-2.4.1
RUN python setup.py build \    
    && python setup.py install

WORKDIR /jsunpack-n/depends/yapgvb-1.2.3-source
RUN sed -i 's/use_boost = True/use_boost = False/g' config_linux2.py \
    && python setup.py build \
    && python setup.py install

#USER appuser

WORKDIR /jsunpack-n
ENTRYPOINT ["/usr/bin/python","jsunpackn.py"]

