FROM python:3.7-alpine

LABEL MAINTAINER=cincan.io

RUN pip install dnspython==1.16.0 \
    && adduser -s /sbin/login -D appuser

ADD gatherdns.py query.py ./

USER appuser

ENTRYPOINT ["python", "query.py"]
CMD ["--help"]
