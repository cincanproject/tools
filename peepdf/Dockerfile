# docker run -v /samples:/samples cincan/peepdf /samples/sample.pdf
FROM ubuntu:16.04

RUN apt-get update && apt-get install -y \
	git \
	python \
	libboost1.58-all-dev \
	pkg-config \
	autoconf \
	python-libemu \
	python-pil \
    && apt-get autoclean \ 
    && git clone https://github.com/buffer/pyv8.git \
    && git clone --recursive https://github.com/buffer/pylibemu.git \
    && git clone https://github.com/jesparza/peepdf.git

WORKDIR $HOME/pyv8
RUN python setup.py build && python setup.py install
WORKDIR $HOME/pylibemu
RUN python setup.py build && python setup.py install 

ENTRYPOINT ["/usr/bin/python","/peepdf/peepdf.py"]

