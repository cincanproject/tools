# This docker image loads access.log to Jupyter Notebook for visualization, and then converts the output to html

ARG tool_version=1.0.0

FROM debian:10-slim

LABEL MAINTAINER=cincan.io

ARG tool_version
ENV TOOL_VERSION=${tool_version}

ENV ACCESS_LOG_PATH=/home/appuser

RUN apt-get update && apt-get install -y \
	python3.7 \
	python3-pip

RUN pip3 install pandas \
	jupyter \ 
	plotly \
	apache-log-parser \
	tqdm \
	&& adduser --shell /sbin/nologin --disabled-login --gecos "" appuser

COPY scripts/access-log.ipynb scripts/entrypoint.py scripts/testing.ipynb /home/appuser/

USER appuser

WORKDIR /home/appuser/

RUN jupyter migrate \
	&& jupyter nbconvert --to html --execute testing.ipynb --output testing.html

ENTRYPOINT ["/usr/bin/python3", "/home/appuser/entrypoint.py"]

