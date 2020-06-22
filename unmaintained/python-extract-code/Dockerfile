FROM ubuntu:18.04

LABEL MAINTAINER=cincan.io

RUN apt-get update && apt-get install -y \
	    git=1:2.17.1-1ubuntu0.4  \
	    python3=3.6.7-1~18.04 \
	    python3-pip=9.0.1-2.3~ubuntu1.18.04.1 \
    && apt-get autoclean

COPY files python-exe-analysis

RUN cd python-exe-analysis/ \
    && pip3 install requests -r requirements.txt \
    && adduser --shell /sbin/nologin --disabled-login --gecos "" appuser \
    && chown -R appuser:appuser /python-exe-analysis

USER appuser

WORKDIR /python-exe-analysis

ENTRYPOINT ["/usr/bin/python3","extract_code.py"]
CMD ["-h"]
