#docker run -v /samples:/samples cincan/output-standardizer json -i input.txt -o output.json -t <tool-name>
FROM ubuntu:18.04

LABEL MAINTAINER=cincan.io

RUN apt-get update && apt-get install -y \
            git=1:2.17.1-1ubuntu0.4  \
            python3=3.6.7-1~18.04 \
            python3-pip=9.0.1-2.3~ubuntu1.18.04.1 \
    && apt-get autoclean \
    && git clone https://gitlab.com/CinCan/tools-output-standardization.git \
    && cd /tools-output-standardization \
    && pip3 install . \
    && adduser --shell /sbin/nologin --disabled-login --gecos "" appuser \
    && chown appuser:appuser /tools-output-standardization

USER appuser

WORKDIR /tools-output-standardization

ENTRYPOINT ["standardizer"]
CMD ["--help"]
