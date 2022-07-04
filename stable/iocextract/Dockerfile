ARG tool_version="1.13.1"
FROM python:alpine as builder

LABEL MAINTAINER=cincan.io

ARG tool_version
ENV TOOL_VERSION=$tool_version

RUN apk update && apk add --no-cache \
    alpine-sdk \
    && pip install iocextract==$TOOL_VERSION --prefix=/install

FROM python:alpine as runtime

ARG tool_version
ENV TOOL_VERSION=$tool_version

COPY --from=builder /install /usr/local

RUN adduser -s /sbin/login -D appuser

WORKDIR /home/appuser/

USER appuser

COPY meta.json /opt/

ENTRYPOINT ["iocextract"]
CMD ["--help"]

