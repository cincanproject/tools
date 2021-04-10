#docker run -v $(pwd):/data cincan/feature_extractor --injsonl /data/jsonl_input --path /data/
ARG tool_version=0.2

FROM python:3.6-slim-buster

LABEL MAINTAINER=cincan.io

ARG tool_version
ENV TOOL_VERSION=$tool_version

RUN apt update && apt install -y \
	git=1:2.20* \
	&& git clone https://gitlab.com/CinCan/feature_extractor.git --branch ${TOOL_VERSION}\
	&& cd feature_extractor/ \
	&& pip install -r requirements.txt \
	&& adduser --shell /sbin/nologin --disabled-login --gecos "" appuser \
	&& chown -R appuser:appuser /feature_extractor

USER appuser

WORKDIR /home/appuser

COPY meta.json /opt/

ENTRYPOINT ["/usr/local/bin/python","/feature_extractor/analyze_parallel.py","--confpath", "/feature_extractor"]

CMD ["-h"]
