# "Upload a PDF to www.pdfexaminer.com/pdfapi.php and get results."
ARG tool_version=1.0.1

FROM python:3-alpine

LABEL MAINTAINER=cincan.io

ARG tool_version
ENV TOOL_VERSION=$tool_version

RUN apk update && apk add \
	git>2.24.3  \
	&& git clone https://gitlab.com/CinCan/pdfexaminer.git \
	&& cd pdfexaminer/ \
	&& pip install -r requirements.txt \
	&& adduser -s /sbin/login -D appuser

USER appuser

WORKDIR /home/appuser

ENTRYPOINT ["python", "/pdfexaminer/pdfexaminer.py"]
CMD ["-h"]
