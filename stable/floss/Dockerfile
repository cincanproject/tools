ARG tool_version=1.6.1

FROM python:2.7-buster as build 
LABEL maintainer=cincan.io

ARG tool_version
ENV TOOL_VERSION=$tool_version
ENV DOWNLOAD_URL=https://github.com/fireeye/flare-floss/archive/v$TOOL_VERSION.zip

RUN apt-get update && apt-get -y install \
    unzip \
    wget

RUN mkdir /floss \
    && cd /floss \
    && wget ${DOWNLOAD_URL} \
    && unzip v${TOOL_VERSION}.zip \
    && groupadd -g 1000 appuser \
    && useradd -m -u 1000 -g appuser appuser 

USER appuser

RUN cd /floss && pip install flare-floss-${TOOL_VERSION}/. --user 

FROM python:2.7-buster as runtime

ARG tool_version
ENV TOOL_VERSION=$tool_version


RUN groupadd -g 1000 appuser && \
    useradd -m -u 1000 -g appuser -s /sbin/nologin appuser

COPY --from=build /home/appuser/.local /home/appuser/.local

ENV PATH=/home/appuser/.local/bin:$PATH
WORKDIR /home/appuser/
USER appuser

ENTRYPOINT ["floss"]
CMD ["--help"]
