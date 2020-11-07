ARG tool_version=c144a6ddd86f427c8abc4fda0af142417813f5f2

FROM alpine:latest AS builder

LABEL MAINTAINER=cincan.io

ARG tool_version
ENV TOOL_VERSION=$tool_version

RUN apk update && apk add --no-cache \
        python3 \
        py3-setuptools \
        git && \
    addgroup -S appuser && \
    adduser -s /sbin/nologin --disabled-password -G appuser appuser

USER appuser

RUN git clone https://github.com/dxa4481/truffleHog.git /home/appuser/truffleHog && \
    cd /home/appuser/truffleHog && \
    git checkout "$TOOL_VERSION" && \
    python3 setup.py install --user

FROM alpine:latest as runtime

RUN apk update && apk add --no-cache \
    git \
    python3 \
    py3-setuptools && \
    addgroup -S appuser && \
    adduser -s /sbin/nologin --disabled-password -G appuser appuser

COPY --from=builder /home/appuser/.local /home/appuser/.local

WORKDIR /home/appuser/tool
ENV PATH=/home/appuser/.local/bin:$PATH

USER appuser

ENTRYPOINT ["trufflehog"]
CMD ["-h"]
