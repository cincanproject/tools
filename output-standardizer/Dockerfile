#docker run -v /samples:/samples cincan/output-standardizer json -i input.txt -o output.json -t <tool-name>
FROM ubuntu:18.04

LABEL MAINTAINER=cincan.io

RUN apt-get update && apt-get install -y \
            git \
            python3 \
            python3-pip \
    && apt-get autoclean \
    && git clone https://gitlab.com/CinCan/tools-output-standardization.git \
    && cd /tools-output-standardization \
    && pip3 install . \
    && adduser --shell /sbin/nologin --disabled-login --gecos "" appuser

USER appuser

WORKDIR /tools-output-standardization

ENTRYPOINT ["standardizer"]
CMD ["--help"]
