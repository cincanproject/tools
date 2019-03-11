FROM ubuntu:18.04
USER root

RUN apt-get update && apt-get install -y \
        python3 \
        python3-pip

RUN pip3 install jupyter plotly apache-log-parser pandas tqdm

ENTRYPOINT ["/usr/local/bin/jupyter", "nbconvert", "--to", "html", \
        "--execute", \
        "/samples/access-log.ipynb", "--output", "/samples/output.html", "--ExecutePreprocessor.timeout=3600"]
