# "Upload a PDF to www.pdfexaminer.com/pdfapi.php and get results."
ARG tool_version=

FROM python:3-alpine

LABEL MAINTAINER=cincan.io

COPY /files .

RUN pip install -r requirements.txt \
    && adduser -s /sbin/login -D appuser

USER appuser

ENTRYPOINT ["python", "sendfile.py"]
