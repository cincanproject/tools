ARG tool_version=0.56

FROM python:3-alpine as build

# olevba latest installation in python3

ARG tool_version
ENV TOOL_VERSION=$tool_version

LABEL MAINTAINER=cincan.io

RUN apk update && \
	apk add --no-cache \
		openssl-dev \
		gcc \
		libffi-dev \
		libc-dev

RUN pip3 wheel --wheel-dir=/oletools oletools=="$TOOL_VERSION"

FROM python:3-alpine as runtime

ARG tool_version
ENV TOOL_VERSION=$tool_version

RUN addgroup -S appuser && \
	adduser -s /sbin/nologin --disabled-password -G appuser appuser

COPY --from=build /oletools /oletools_tmp

USER appuser

RUN pip3 install \
	--no-index \
	--find-links=/oletools_tmp \
	--user \
    oletools

USER root

# Remove tmp files and olebrowse - it is requiring GUI
RUN rm -rf /oletools_tmp && rm /home/appuser/.local/bin/olebrowse

COPY entrypoint.sh /oletools/entrypoint.sh
RUN chmod +x /oletools/entrypoint.sh

# Following variable is used in entrypoint.sh as well
ENV OLETOOLS_HOME /home/appuser/.local/bin
ENV PATH="$OLETOOLS_HOME":"$PATH"
ADD Oletools-license /oletools/
USER appuser

WORKDIR /home/appuser/

ENTRYPOINT ["sh", "/oletools/entrypoint.sh"]
CMD ["--help"]
