# "Upload a PDF to www.pdfexaminer.com/pdfapi.php and get results."
# 
# build:
# docker build -t cincan/pdfexaminer .
#
# usage:
# docker run -v /samples:/samples cincan/pdfexaminer /samples/input/sample.pdf [options]
#
# [options] = output format (default json)

FROM python:3.6-alpine

COPY /files .

RUN pip install -r requirements.txt

ENTRYPOINT ["python", "sendfile.py"]
