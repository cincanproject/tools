FROM python:3.5-alpine

LABEL MAINTAINER=cincan.io

RUN pip install python-whois==0.7.1 PySocks==1.6.8

ADD query.py .

ENTRYPOINT ["./query.py"]
CMD ["--help"]
