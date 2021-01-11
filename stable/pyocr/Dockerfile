ARG tool_version=0.8.0

FROM debian:10-slim as build

ARG tool_version
ENV TOOL_VERSION=$tool_version

RUN apt-get update && \
    apt-get install --no-install-recommends -y \
	python3-dev \
        python3-pip \
        python3-wheel \
        python3-setuptools \
   	build-essential && \ 
    pip3 install --user pyocr==$TOOL_VERSION Pillow wand opencv-python numpy

FROM debian:10-slim as env

ARG tool_version
ENV TOOL_VERSION=$tool_version

RUN apt-get update && \
    apt-get install --no-install-recommends -y \
        python3 \
        libmagickwand-dev \
        ghostscript \
        tesseract-ocr=4.0.0-2 \
        tesseract-ocr-fin && \
    rm -rf /var/lib/apt/lists/*

COPY --from=build /root/.local /home/appuser/.local

RUN mkdir -p /home/appuser/tool && \
    adduser --shell /sbin/nologin --disabled-login --gecos "" appuser && \
    chown -R appuser:appuser /home/appuser/

USER appuser
WORKDIR /home/appuser/tool

COPY ocr.py /home/appuser/ocr.py

ENTRYPOINT ["/home/appuser/ocr.py"]

CMD ["-h"]
