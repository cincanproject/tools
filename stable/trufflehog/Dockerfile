ARG tool_version=5d85bfb7a860b66cd94d03f9609a83bf6cbbf9c0

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

ARG tool_version
ENV TOOL_VERSION=$tool_version

# meta.json should be kept as final modification for layers
COPY meta.json /opt/
ENTRYPOINT ["trufflehog"]
CMD ["-h"]
