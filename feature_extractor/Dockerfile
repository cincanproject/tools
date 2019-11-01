#docker run -v /samples:/samples cincan/feature-extractor /samples/input
# --injsonl = takes jsonl as input

FROM ubuntu:18.04

LABEL MAINTAINER=cincan.io

RUN apt-get update && apt-get install -y \
	    git \
	    python3 \
	    python3-pip \
    && apt-get autoclean \ 
    && git clone https://gitlab.com/CinCan/wp1.git \
    && cd wp1/feature_extractor/ \
    && pip3 install -r requirements.txt \
    && adduser --shell /sbin/nologin --disabled-login --gecos "" appuser

USER appuser

WORKDIR /wp1/feature_extractor/

ENTRYPOINT ["/usr/bin/python3","analyze_parallel.py"]
CMD ["--injsonl"]
