# Default alpine package has no JSON support
# Self-builded image to enable it

# Package cannot be build in CI without dummy getfattr

FROM alpine:3.10

LABEL MAINTAINER=cincan.io

ADD buildconf.tar.gz ./

ENV VERSION=0.102.0

RUN apk update && apk add --no-cache\
	alpine-sdk=1.0-r0

# Build ClamAv from source

RUN addgroup root abuild 

# Fix CI building by creating dummy getfattr
# Alpine is using this to maintain extended attributes but they are not working in CI
# Does not affect functionality
RUN echo "echo \"\"" > /usr/bin/getfattr && \
    chmod +x /usr/bin/getfattr && \
    echo "echo \"\"" > /bin/getfattr && \
    chmod +x /bin/getfattr

RUN cd buildconf && \ 
    abuild-keygen -a -i && \
    abuild -R -F && \
    echo "Build finished"

# Copy binaries to actual image
FROM alpine:3.10
COPY --from=0 /root/packages /root/packages

# Copy build keys to make new binaries trusted
COPY --from=0 /etc/apk/keys /etc/apk/keys
COPY --from=0 /root/.abuild/ /root/.abuild/

RUN echo "/root/packages" | tee -a /etc/apk/repositories && \
    apk update && \
    apk --no-cache add --repository /root/packages clamav && \
    apk --no-cache add --repository /root/packages clamav-daemon && \
    apk --no-cache add --repository /root/packages clamav-libunrar && \
    apk --no-cache add file=5.37-r1 && \
    apk add --no-cache jq=1.6-r0  && \
    rm -rf /root/* && \
# Change permissions suitable for future user creation
    chown -R clamav:clamav /var/lib/clamav/ && \
    chown -R clamav:clamav /var/log/clamav/ && \
    chmod -R 775 /var/lib/clamav/ && \
    chmod -R 775 /var/log/clamav/ && \
# Create user and add to clamav group
    addgroup -S appuser && \
    adduser -s /sbin/nologin --disabled-password -G appuser appuser && \
    addgroup appuser clamav && \
# Make daemon to work
    touch /var/lib/clamav/clamd.sock && \
    chown clamav:clamav /var/lib/clamav/clamd.sock && \
    chmod 775 /var/lib/clamav/clamd.sock && \
    sed -i '/LocalSocket\b/c\LocalSocket /var/lib/clamav/clamd.sock' /etc/clamav/clamd.conf

USER appuser

RUN freshclam
# Database should be run once before starting the daemon, however daemon might have much
# use case here...
RUN clamd

WORKDIR /home/appuser/

ENTRYPOINT ["/usr/bin/clamscan"]
CMD ["--help"]

# Example command to run and generate JSON metadata
# docker run -v /home/cincan/Documents/CinCan/document-pipeline/test:/opt/test clamscan-dev:latest --gen-json --leave-temps --tempdir=/opt/test/tmp /opt/test/sample.pdf
