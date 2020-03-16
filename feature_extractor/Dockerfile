#docker run -v $(pwd):/data cincan/feature_extractor --injsonl /data/jsonl_input --path /data

FROM python:3.6-slim-buster

LABEL MAINTAINER=cincan.io

RUN apt update && apt install -y \
	git \
	&& git clone https://gitlab.com/CinCan/wp1.git \
	&& cd wp1/feature_extractor/ \
	&& pip install -r requirements.txt \
	&& adduser --shell /sbin/nologin --disabled-login --gecos "" appuser \
	&& chown -R appuser:appuser /wp1

USER appuser

WORKDIR /wp1/feature_extractor/

ENTRYPOINT ["/usr/local/bin/python","analyze_parallel.py"]
