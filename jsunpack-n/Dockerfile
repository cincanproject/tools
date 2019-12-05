# Emulates browser functionality when visiting an URL. Detects browser exploits, scans PDF.
#
# docker run -v $(pwd):/input cincan/jsunpack-n /input/samples/testfile.pdf -V -d /input/samples/output/

FROM debian:8-slim AS builder

LABEL MAINTAINER=cincan.io

ENV VERSION="0.3.2c (beta)"

RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc=4:4.9.2-2 \
    g++=4:4.9.2-2 \
    make=4.0-8.1 \
    git=1:2.1.4-2.1+deb8u7 \
    ca-certificates=20141019+deb8u4 \
    python=2.7.9-1 \
    python-dev=2.7.9-1 \
    libpcap-dev=1.6.2-2+deb8u1 \
    pkg-config=0.28-1 \
    libgtk2.0-dev=2.24.25-3+deb8u2 \
    libnet1-dev=1.1.6+dfsg-3 \
    libpcre3=2:8.35-3.3+deb8u4 \
    python-pygraphviz=1.3~rc2-1 \
    libboost-dev=1.55.0.2 \
    wget=1.16-1+deb8u6 \
    && rm -rf /var/lib/apt/lists/* \
    && git clone https://github.com/urule99/jsunpack-n.git

WORKDIR /jsunpack-n/depends
RUN git checkout c01f406fd1ac113838f5e9ede8c04a63ef0acd5d \
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

FROM debian:8-slim AS production

COPY --from=builder /jsunpack-n /jsunpack-n
COPY --from=builder /etc/ld.* /etc/
COPY --from=builder /usr/local /usr/local

RUN apt-get update && apt-get install -y --no-install-recommends \
        python-magic=1:5.22+15-2+deb8u7 \ 
        python=2.7.9-1 \
        libpcap-dev=1.6.2-2+deb8u1 \
        libgtk2.0-dev=2.24.25-3+deb8u2 \
        libnet1-dev=1.1.6+dfsg-3 \
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
