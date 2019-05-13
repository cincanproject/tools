FROM python:3.7-alpine

LABEL MAINTAINER=cincan.io

RUN pip install dnspython==1.16.0

ADD gatherdns.py query.py ./

ENTRYPOINT ["python", "query.py"]
CMD ["--help"]
