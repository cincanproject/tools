ARG tool_version=0.7.3
FROM python:3.5-alpine

LABEL MAINTAINER=cincan.io

ARG tool_version
ENV TOOL_VERSION=$tool_version

RUN pip install python-whois=="$TOOL_VERSION" \
        PySocks==1.6.8 \
    && adduser -s /sbin/login -D appuser

ADD query.py .

USER appuser
WORKDIR /home/appuser

ENTRYPOINT ["/query.py"]
CMD ["--help"]
