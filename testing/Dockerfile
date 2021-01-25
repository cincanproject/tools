FROM alpine:latest

LABEL MAINTAINER=cincan.io
ENV TOOL_VERSION=1.0

RUN addgroup -S appuser && \
    adduser -s /sbin/nologin --disabled-password -G appuser appuser

WORKDIR /home/appuser

CMD ["echo", "Hello, world!"]
