# This docker image loads access.log to Jupyter Notebook for visualization, and then converts the output to html

FROM debian:10-slim

LABEL MAINTAINER=cincan.io

ENV VERSION=1.0.0

ENV ACCESS_LOG_PATH=/home/appuser

RUN apt-get update && apt install -y \
	python3.7=3.7.3-2 \
	python3-pip=18.1-5

RUN pip3 install pandas==0.24.2 \
	jupyter==1.0.0 \ 
	plotly==3.10.0 \
	apache-log-parser==1.7.0 \
	tqdm==4.32.2 \
	&& adduser --shell /sbin/nologin --disabled-login --gecos "" appuser

COPY scripts/access-log.ipynb scripts/entrypoint.py scripts/testing.ipynb /home/appuser/

USER appuser

WORKDIR /home/appuser

RUN jupyter migrate \
	&& jupyter nbconvert --to html --execute testing.ipynb --output testing.html

ENTRYPOINT ["/usr/bin/python3", "/home/appuser/entrypoint.py"]

