# "Shellcode2exe.py - Convert shellcodes into executable files for multiple platforms."
#
# build:
#  docker build -t cincan/shellcode2exe .
#
# usage:
#  docker run -v /samples:/samples shellcode2exe /samples/shellcode


FROM alpine:latest

RUN apk update && apk add \
	git \
	python \
	wget \
	py2-pip

RUN wget https://www.secureauth.com/sites/default/files/project/attachment/2018-10/InlineEgg-1.08.tar_.gz \
	&& tar zxvf InlineEgg-1.08.tar_.gz && cd InlineEgg-1.08 \
	&& python setup.py build && python setup.py install

RUN git clone https://github.com/MarioVilas/shellcode_tools.git

ENTRYPOINT ["/usr/bin/python","/shellcode_tools/shellcode2exe.py"]
