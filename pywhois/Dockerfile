FROM python:3.5-alpine

LABEL MAINTAINER=cincan.io
LABEL io.cincan.input="ip"

COPY commands.json /cincan/commands.json

RUN pip install python-whois==0.7.1 \
        PySocks==1.6.8 \
    && adduser -s /sbin/login -D appuser

ADD query.py .

USER appuser

ENTRYPOINT ["./query.py"]
CMD ["--help"]
