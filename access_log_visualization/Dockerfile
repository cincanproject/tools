FROM python:3.7-slim

LABEL MAINTAINER=cincan.io

RUN pip3 install pandas==0.24.2 \
        jupyter==1.0.0 \ 
        plotly==3.10.0 \
        apache-log-parser==1.7.0 \
        tqdm==4.32.2 \
    && adduser --shell /sbin/nologin --disabled-login --gecos "" appuser

USER appuser

ENTRYPOINT ["/usr/local/bin/jupyter", "nbconvert", "--to", "html", \
        "--execute", \
        "/samples/access-log.ipynb", "--output", "/samples/output.html", "--ExecutePreprocessor.timeout=3600"]
