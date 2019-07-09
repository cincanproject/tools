#FROM ubuntu:18.04
#USER root

#RUN apt-get update && apt-get install -y \
#        python3 \
#        python3-pip


#RUN pip3 install jupyter plotly apache-log-parser pandas tqdm

FROM python:3.7-slim

RUN pip3 install pandas==0.24.2 jupyter==1.0.0 plotly==3.10.0 apache-log-parser==1.7.0 tqdm==4.32.2

ENTRYPOINT ["/usr/local/bin/jupyter", "nbconvert", "--to", "html", \
        "--execute", \
        "/samples/access-log.ipynb", "--output", "/samples/output.html", "--ExecutePreprocessor.timeout=3600"]
