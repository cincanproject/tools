# "A script to carve files from memory dumps."
# https://github.com/countercept/radare2-scripts

FROM alpine:3.9

LABEL MAINTAINER=cincan.io

RUN apk update && apk add --no-cache \
	git=2.20.2-r0 \
	py-setuptools=40.6.3-r0 \
	py2-pip=18.1-r0 \
	radare2=2.9.0-r1

RUN pip install r2pipe==1.2.0 \
	&& git clone https://github.com/countercept/radare2-scripts.git

WORKDIR /radare2-scripts

RUN git checkout 6587867fc7f4a8df50b1f940b1dbfa407a42448d \
	&& adduser -s /sbin/nologin -D appuser

USER appuser

ENTRYPOINT ["/usr/bin/python","/radare2-scripts/r2_bin_carver.py"]
CMD ["--help"]
