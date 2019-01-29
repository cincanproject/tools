# docker run -v /samples:/samples cincan/peepdf /samples/sample.pdf -f

FROM ubuntu:16.04

RUN apt-get update && apt-get install -y \
	git \
	python \
	libboost1.58-all-dev \
	pkg-config \
	autoconf \
	python-libemu \
	python-pil

RUN git clone https://github.com/buffer/pyv8.git \
	&& cd pyv8 && python setup.py build && python setup.py install \
	&& cd / && git clone --recursive https://github.com/buffer/pylibemu.git \
	&& cd pylibemu && python setup.py build && python setup.py install \
	&& cd / && git clone https://github.com/jesparza/peepdf.git

ENTRYPOINT ["/usr/bin/python","/peepdf/peepdf.py"]

