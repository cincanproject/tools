ARG tool_version=7a0493c9724a6c4ee5bd188beb0f813494e379c8

FROM alpine:3.11

LABEL MAINTAINER=cincan.io

ARG tool_version
ENV TOOL_VERSION=$tool_version

RUN apk --update --no-cache \
	add python=2.7.16-r1 \
	python-dev=2.7.16-r1 \
	py2-pip=18.1-r0 \
	git=2.22.0-r0 \
	graphviz=2.40.1-r1 \
	g++=8.3.0-r0 \
	make=4.2.1-r2 \
	subversion=1.12.2-r0 \
	gcc=8.3.0-r0 \
	gfortran=8.3.0-r0 \
	ca-certificates=20190108-r0 \
	libpng-dev=1.6.37-r1 \
	freetype-dev=2.10.0-r0 \
	&& git clone https://github.com/MalwareCantFly/Vba2Graph.git

WORKDIR /Vba2Graph

RUN git checkout -b tool $TOOL_VERSION \
	&& pip install -U oletools==0.54.1 -r requirements.txt \
	&& adduser -s /sbin/login -D appuser

#USER appuser

ENTRYPOINT ["/usr/bin/python","/Vba2Graph/vba2graph.py"]
CMD ["-h"]
