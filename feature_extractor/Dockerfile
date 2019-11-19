#docker run -v /samples:/samples cincan/feature-extractor /samples/input
# --injsonl = takes jsonl as input

FROM ubuntu:18.04

LABEL MAINTAINER=cincan.io

RUN apt-get update && apt-get install -y \
	    git=1:2.17.1-1ubuntu0.4  \
	    python3=3.6.7-1~18.04 \
	    python3-pip=9.0.1-2.3~ubuntu1.18.04.1 \
    && apt-get autoclean \ 
    && git clone https://gitlab.com/CinCan/wp1.git \
    && cd wp1/feature_extractor/ \
    && pip3 install -r requirements.txt \
    && adduser --shell /sbin/nologin --disabled-login --gecos "" appuser \
    && chown -R appuser:appuser /wp1

USER appuser

WORKDIR /wp1/feature_extractor/

ENTRYPOINT ["/usr/bin/python3","analyze_parallel.py"]
CMD ["--injsonl"]
