ARG tool_version=511ecd59d54c6a3424178af6b99e4c1f699274c4
FROM debian:10 as build

LABEL MAINTAINER=cincan.io

ARG tool_version
ENV TOOL_VERSION=$tool_version

ENV DEBIAN_FRONTEND=noninteractive
# TODO remove forced safe exit after pip installation
# See https://github.com/pypa/pip/issues/8653
RUN apt-get update && \
    apt-get install --no-install-recommends -y \
        ca-certificates \
        wget \
        unzip \
        pypy \
	pypy-dev \
        libssl-dev \
        build-essential \
    && wget -q https://bootstrap.pypa.io/get-pip.py && \
    pypy get-pip.py "pip<20.2" --no-wheel || true && \
    pypy -m pip install setuptools --user && wget -q https://github.com/kirk-sayre-work/ViperMonkey/archive/$TOOL_VERSION.zip && \
    unzip -q $TOOL_VERSION.zip && \
    mv ViperMonkey-$TOOL_VERSION vipermonkey && \
    pypy -m pip install --user -r vipermonkey/requirements.txt

FROM debian:10-slim as env

ARG tool_version
ENV TOOL_VERSION=$tool_version

RUN  adduser --shell /sbin/nologin --disabled-login --gecos "" appuser

COPY --from=build /root/.local /home/appuser/.local
COPY --from=build /vipermonkey /home/appuser/vipermonkey

RUN apt-get update && \
    apt-get install --no-install-recommends -y pypy && \
    mkdir -p /home/appuser/tool && \
    chown -R appuser:appuser /home/appuser/

USER appuser
ENV PATH=/home/appuser/.local/bin:$PATH
WORKDIR /home/appuser/tool

ENTRYPOINT ["pypy", "/home/appuser/vipermonkey/vipermonkey/vmonkey.py"]
CMD ["--help"]
