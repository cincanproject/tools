ARG tool_version=0.2.4

FROM alpine:latest

LABEL MAINTAINER=cincan.io

ARG tool_version
ENV TOOL_VERSION=$tool_version

ENV SHA_CHECK 52a8ed71c5f5efaae121aa0bcbbcfa55bf67b7ba7a7822ac337dcdfa31135ed9

RUN apk update && apk add --no-cache \
	curl-dev \
	ruby-dev \
	ruby \
	ruby-io-console \
	ruby-bundler \
	build-base

RUN wget -q -O "zsteg.zip" "https://github.com/zed-0xff/zsteg/archive/v${TOOL_VERSION}.zip" \
	&& echo "${SHA_CHECK}  zsteg.zip"| sha256sum -c - \
	&& unzip zsteg.zip && mv zsteg-${TOOL_VERSION} zsteg \
	&& gem install bundler rake \
	&& addgroup -S appuser \
	&& adduser -s /sbin/nologin --disabled-password -G appuser appuser \
	&& cd zsteg \
	&& bundle install

USER appuser

WORKDIR /home/appuser

# meta.json should be kept as final modification for layers
COPY meta.json /opt/
ENTRYPOINT ["/zsteg/bin/zsteg"]
CMD ["--help"]
