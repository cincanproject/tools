ARG tool_version=0.102.4+dfsg-0+deb10u1

FROM debian:buster-slim

LABEL MAINTAINER=cincan.io

ARG tool_version
ENV TOOL_VERSION=$tool_version

RUN apt-get update && apt-get install -y clamav="$TOOL_VERSION" jq && \
    rm -rf /var/lib/apt/lists/* /var/cache/apt/archives /tmp/* /var/tmp/*  &&\
    # Change permissions suitable for future user creation
    chown -R clamav:clamav /var/lib/clamav/ && \
    chown -R clamav:clamav /var/log/clamav/ && \
    chmod -R 775 /var/lib/clamav/ && \
    chmod -R 775 /var/log/clamav/ && \
    groupadd -g 1000 appuser && \
    useradd -u 1000 -g appuser -s /sbin/nologin appuser \
    && usermod -a -G clamav appuser

USER appuser

RUN freshclam 

WORKDIR /home/appuser/
COPY meta.json /opt/

ENTRYPOINT ["/usr/bin/clamscan"]
CMD ["--help"]

# Example command to run and generate JSON metadata
# docker run -v /home/cincan/Documents/CinCan/tools/clamav/test:/opt/test clamav:latest --gen-json --leave-temps --tempdir=/opt/test/tmp /opt/test/sample.pdf
