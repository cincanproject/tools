# docker build -t cincan/jsunpack-n .
#
# File scan:
# docker run -v /samples:/samples cincan/jsunpack-n /samples/input/sample.pdf -d /samples/output
#
# Url scan:
# docker run -v /samples:/samples cincan/jsunpack-n -u https://<TARGET.URL> -d /samples/output -V

FROM ubuntu:16.04

RUN apt-get update && apt-get install -y \
	python \
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
	libboost1.58-all-dev \
	wget 

RUN git clone https://github.com/urule99/jsunpack-n.git

WORKDIR jsunpack-n/depends
RUN tar xvfz pynids-0.6.1.tar.gz && cd pynids-0.6.1 && python setup.py build && python setup.py install \
	&& cd /jsunpack-n/depends && tar xvfz js-1.8.0-rc1-src.tar.gz \
	&& cd /jsunpack-n/depends/js-1.8.0-rc1-src && make BUILD_OPT=1 -f Makefile.ref && echo "export $PATH=" && make BUILD_OPT=1 JS_DIST=/usr/local -f Makefile.ref export \
	&& cd /jsunpack-n/depends && tar xvfz yara-1.6.tar.gz && cd yara-1.6 && ./configure && make && make install && echo "/usr/local/lib" >> /etc/ld.so.conf && ldconfig \
	&& cd /jsunpack-n/depends && tar xvfz yara-python-1.6.tar.gz && cd yara-python-1.6 && python setup.py build && python setup.py install \
	&& cd /jsunpack-n/depends && tar xvzf BeautifulSoup-3.2.0.tar.gz && cd BeautifulSoup-3.2.0 && python setup.py build && python setup.py install \
	&& cd /jsunpack-n/depends && tar xvzf pycrypto-2.4.1.tar.gz && cd pycrypto-2.4.1 && python setup.py build && python setup.py install \
	&& cd /jsunpack-n/depends && wget https://storage.googleapis.com/google-code-archive-downloads/v2/code.google.com/yapgvb/yapgvb-1.2.3-source.tar.gz \
	&& tar zxvf yapgvb-1.2.3-source.tar.gz && cd yapgvb-1.2.3-source \
	&& sed -i 's/use_boost = True/use_boost = False/g' config_linux2.py && python setup.py build && python setup.py install

WORKDIR /jsunpack-n
ENTRYPOINT ["/usr/bin/python","jsunpackn.py"]

