# Emulates browser functionality when visiting an URL. Detects browser exploits, scans PDF.
#
# docker run -v $(pwd):/input cincan/jsunpack-n /input/samples/testfile.pdf -V -d /input/samples/output/

ARG tool_version="c01f406fd1ac113838f5e9ede8c04a63ef0acd5d"

FROM debian:8-slim AS builder

LABEL MAINTAINER=cincan.io

ARG tool_version
ENV TOOL_VERSION=$tool_version

RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    g++ \
    make \
    git \
    ca-certificates \
    python \
    python-dev \
    libpcap-dev \
    pkg-config \
    libgtk2.0-dev \
    libnet1-dev \
    libpcre3 \
    python-pygraphviz \
    libboost-dev \
    wget \
    && rm -rf /var/lib/apt/lists/* \
    && git clone https://github.com/urule99/jsunpack-n.git

WORKDIR /jsunpack-n/depends
RUN git checkout $TOOL_VERSION \
    && tar xvfz pynids-0.6.1.tar.gz \
    && tar xvfz js-1.8.0-rc1-src.tar.gz \
    && tar xvfz yara-1.6.tar.gz \
    && tar xvfz yara-python-1.6.tar.gz \
    && tar xvzf BeautifulSoup-3.2.0.tar.gz \
    && tar xvzf pycrypto-2.4.1.tar.gz \
    && wget https://storage.googleapis.com/google-code-archive-downloads/v2/code.google.com/yapgvb/yapgvb-1.2.3-source.tar.gz \
    && tar zxvf yapgvb-1.2.3-source.tar.gz

WORKDIR /jsunpack-n/depends/yara-1.6
RUN ./configure \
    && make \
    && make install \
    && echo "/usr/local/lib" >> /etc/ld.so.conf \
    && ldconfig

WORKDIR /jsunpack-n/depends/pynids-0.6.1
RUN python setup.py build \
    && python setup.py install

WORKDIR /jsunpack-n/depends/js-1.8.0-rc1-src
RUN make BUILD_OPT=1 -f Makefile.ref \
    && echo "export $PATH=" \
    && make BUILD_OPT=1 JS_DIST=/usr/local -f Makefile.ref export

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

FROM debian:10-slim AS production

ARG tool_version
ENV TOOL_VERSION=$tool_version

COPY --from=builder /jsunpack-n /jsunpack-n
COPY --from=builder /etc/ld.* /etc/
COPY --from=builder /usr/local /usr/local

RUN apt-get update && apt-get install -y --no-install-recommends \
        python-magic \ 
        python \
        libpcap-dev \
        libgtk2.0-dev \
        libnet1-dev \
        && rm -rf /var/lib/apt/lists/* \
        && adduser --shell /sbin/nologin --disabled-login --gecos "" appuser \
        && chown -R appuser:appuser /jsunpack-n \
        && chmod +x /jsunpack-n/jsunpackn.py

COPY options.config /jsunpack-n/options.config

# Some inline hacks for python to make it work from everywhere...
# Project has not not been updated for years, so maybe this is OK
RUN sed -i -e "/fin = open('rules', 'r')/c\ \ \ \ fin = open('/jsunpack-n/rules', 'r')" \
    -e "/fin = open('rules.ascii', 'r')/c\ \ \ \ fin = open('/jsunpack-n/rules.ascii', 'r')"  \
    # -e "/fin = open(file, 'rb')/c\ \ \ \ \ \ \ \ \ \ \ \ fin = open('/home/appuser/' + file, 'rb')" \
    /jsunpack-n/jsunpackn.py

ENV PATH "$PATH:/jsunpack-n/"

WORKDIR /jsunpack-n/depends/pynids-0.6.1
RUN python setup.py install \
    && echo "/usr/local/lib" >> /etc/ld.so.conf \
    && ldconfig

WORKDIR /home/appuser
USER appuser

ENTRYPOINT ["jsunpackn.py", "-c", "/jsunpack-n/options.config"]
CMD ["--help"]
