FROM debian:10-slim as build

LABEL MAINTAINER=cincan.io

RUN apt-get update && \
    apt-get install --no-install-recommends -y \
        ca-certificates \
        git \
        python3-dev \
        python3-pip \
        python3-setuptools \
    \
    && pip3 install --user androguard==3.3.5 \
         python-magic==0.4.15 \
         PyOpenSSL==19.1.0 \
    && git clone https://github.com/CERTCC/keyfinder.git

FROM debian:10-slim as env

COPY --from=build /keyfinder /keyfinder
COPY --from=build /root/.local /home/appuser/.local

RUN apt-get update && apt-get install -y \
        python3 \
   && rm -rf /var/lib/apt/lists/* \
   && adduser --shell /sbin/nologin --disabled-login --gecos "" appuser \
   && chown -R appuser:appuser /home/appuser/

USER appuser
WORKDIR /home/appuser

ENTRYPOINT ["python3", "/keyfinder/keyfinder.py"]
CMD ["-h"]
