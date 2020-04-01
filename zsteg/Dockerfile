ARG tool_version=0.2.2

FROM alpine:latest

LABEL MAINTAINER=cincan.io

ARG tool_version
ENV TOOL_VERSION=$tool_version

ENV SHA_CHECK 108ed106e8ef663f9a2bd1d1552ac30c8b65e38e2c49ba5a468942fb31ec867e

RUN apk update && apk add --no-cache \
	curl-dev \
	ruby-dev \
	ruby \
	ruby-io-console \
	ruby-bundler \
	build-base

RUN wget -q -O "zsteg-${TOOL_VERSION}.zip" "https://github.com/zed-0xff/zsteg/archive/v${TOOL_VERSION}.zip" \
	&& echo "${SHA_CHECK}  zsteg-${TOOL_VERSION}.zip"| sha256sum -c - \
	&& unzip zsteg-${TOOL_VERSION}.zip \
	&& gem install bundler rake \
	&& addgroup -S appuser \
	&& adduser -s /sbin/nologin --disabled-password -G appuser appuser \
	&& cd zsteg-${TOOL_VERSION} \
	&& bundle install

USER appuser

WORKDIR /home/appuser

ENTRYPOINT ["/zsteg-0.2.2//bin/zsteg"]
CMD ["--help"]
