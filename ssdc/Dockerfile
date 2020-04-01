FROM debian:10-slim

LABEL MAINTAINER=cincan.io

ENV VERSION=1.2.0
ENV SSDC_SHA256 451a6536eb482cd93abf7bc0cdb17dea177083f668a2dc36999b33306ed5c6d6

RUN apt-get update && apt-get install -y \
	curl \
	unzip \
	python \
	python-pip \
	python-dev \
	ssdeep \
	libfuzzy-dev \
	&& pip install pydeep \
    && curl -OL --fail https://github.com/bwall/ssdc/archive/"v${TOOL_VERSION}.zip"  \
    && echo "$SSDC_SHA256 *v${TOOL_VERSION}.zip" | sha256sum -c - \
	&& unzip "v${TOOL_VERSION}.zip" && cd "ssdc-${TOOL_VERSION}" \
	&& python setup.py build \
	&& python setup.py install \
	&& adduser --shell /sbin/nologin --disabled-login --gecos "" appuser \
	&& chown -R appuser:appuser "/ssdc-${TOOL_VERSION}" \
	&& apt-get purge curl unzip python-pip \
	&& apt-get clean \
	&& rm -rf /var/lib/apt/lists/* /var/cache/apt/archives /tmp/* /var/tmp/* || true

WORKDIR /home/appuser

USER appuser

ENTRYPOINT ["ssdc"]
CMD ["--help"]
