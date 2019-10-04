# NOTE: Package cannot be automatically build in GitLab currntly: problem when running docker in docker and using setattr command

FROM alpine:latest

LABEL MAINTAINER=cincan.io

ADD buildconf.tar.gz ./


RUN apk update && apk add --no-cache\
	alpine-sdk
	# git=2.20.1-r0

# Build ClamAv from source

RUN addgroup root abuild 

RUN cd buildconf && \ 
    abuild-keygen -a -i && \
    abuild -R -F && \
    echo "Build finished"

# Copy binaries to actual image
FROM alpine:latest
COPY --from=0 /root/packages /root/packages

# Copy build keys to make new binaries trusted
COPY --from=0 /etc/apk/keys /etc/apk/keys
COPY --from=0 /root/.abuild/ /root/.abuild/

# VOLUME [ “/sys/fs/cgroup” ]

RUN echo "/root/packages" | tee -a /etc/apk/repositories && \
    apk update && \
    apk --no-cache add --repository /root/packages clamav && \
    apk --no-cache add --repository /root/packages clamav-daemon && \
    apk --no-cache add --repository /root/packages clamav-libunrar && \
    apk --no-cache add file && \
    apk add openrc --no-cache && \
    apk add --no-cache jq

RUN touch /var/lib/clamav/clamd.sock && \
    chown clamav:clamav /var/lib/clamav/clamd.sock && \
    sed -i '/LocalSocket\b/c\LocalSocket /var/lib/clamav/clamd.sock' /etc/clamav/clamd.conf
RUN rc-update add clamd
RUN freshclam


ENTRYPOINT ["/usr/bin/clamscan"]
CMD ["--help"]

# Example command to run and generate JSON metadata
# docker run -v /home/cincan/Documents/CinCan/document-pipeline/test:/opt/test clamscan-dev:latest --gen-json --leave-temps --tempdir=/opt/test/tmp /opt/test/sample.pdf