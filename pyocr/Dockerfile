FROM debian:10-slim as build

RUN apt-get update && \
    apt-get install --no-install-recommends -y \
        python3-pip \
        python3-wheel \
        python3-setuptools && \
    \
    pip3 install --user pyocr Pillow wand

FROM debian:10-slim as env

RUN apt-get update && \
    apt-get install --no-install-recommends -y \
        python3 \
        libmagickwand-dev \
        ghostscript \
        tesseract-ocr \
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
