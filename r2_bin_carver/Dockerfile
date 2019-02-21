# "A script used to carve files from memory dumps."
# https://github.com/countercept/radare2-scripts

FROM radare/radare2:latest

USER root
RUN apt-get update && apt-get install -y \
	git \
	python3-pip

RUN pip3 install r2pipe \
	&& mkdir /r2 \
	&& cd /r2 \
	&& git clone https://github.com/countercept/radare2-scripts.git

VOLUME ["/r2"]
ENTRYPOINT ["/usr/bin/python3", "/r2/radare2-scripts/r2_bin_carver.py"]

