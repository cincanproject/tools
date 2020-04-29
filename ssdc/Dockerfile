ARG tool_version=1.2.0

FROM debian:10-slim

LABEL MAINTAINER=cincan.io

ARG tool_version
ENV TOOL_VERSION=$tool_version
ENV SSDC_SHA256 451a6536eb482cd93abf7bc0cdb17dea177083f668a2dc36999b33306ed5c6d6

RUN apt-get update && apt-get install -y \
	curl=7.64.0* \
	unzip=6.0-23* \
	python=2.7.16* \
	python-pip=18.1* \
	python-dev=2.7.16* \
	ssdeep=2.14.1* \
	libfuzzy-dev=2.14* \
	&& pip install pydeep==0.4 \
	&& echo https://github.com/bwall/ssdc/archive/"v${TOOL_VERSION}.zip" \
	&& curl -OL --fail https://github.com/bwall/ssdc/archive/"v${TOOL_VERSION}.zip"  \
	&& echo "$SSDC_SHA256 *v${TOOL_VERSION}.zip" | sha256sum -c - \
	&& unzip "v${TOOL_VERSION}.zip" && cd "ssdc-${TOOL_VERSION}" \
	&& python setup.py build \
	&& python setup.py install \
	&& adduser --shell /sbin/nologin --disabled-login --gecos "" appuser \
#	&& chown -R appuser:appuser "/ssdc-${TOOL_VERSION}" \
	&& apt-get purge curl unzip python-pip \
	&& apt-get clean \
	&& rm -rf /var/lib/apt/lists/* /var/cache/apt/archives /tmp/* /var/tmp/* || true

WORKDIR /home/appuser

USER appuser

ENTRYPOINT ["ssdc"]
CMD ["--help"]
