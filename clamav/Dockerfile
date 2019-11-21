# Default alpine package has no JSON support
# Self-builded image to enable it

# NOTE: Package cannot be automatically build in GitLab currntly: problem when running docker in docker and using setattr command

FROM alpine:latest

LABEL MAINTAINER=cincan.io

ADD buildconf.tar.gz ./

ENV VERSION=0.102.0

RUN apk update && apk add --no-cache\
	alpine-sdk
	# git=2.20.1-r0

# Build ClamAv from source

RUN addgroup root abuild 

# Fix CI building by creating dummy getfattr
RUN echo "echo \"\"" > /usr/bin/getfattr && \
    chmod +x /usr/bin/getfattr && \
    echo "echo \"\"" > /bin/getfattr && \
    chmod +x /bin/getfattr

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

RUN echo "/root/packages" | tee -a /etc/apk/repositories && \
    apk update && \
    apk --no-cache add --repository /root/packages clamav && \
    apk --no-cache add --repository /root/packages clamav-daemon && \
    apk --no-cache add --repository /root/packages clamav-libunrar && \
    apk --no-cache add file && \
    apk add --no-cache jq  && \
    rm -rf /root/*

# Change permissions suitable for future user creation
RUN chown -R clamav:clamav /var/lib/clamav/ && \
    chown -R clamav:clamav /var/log/clamav/ && \
    chmod -R 775 /var/lib/clamav/ && \
    chmod -R 775 /var/log/clamav/
    
# Create user and add to clamav group
RUN addgroup -S appuser && \
    adduser -s /sbin/nologin --disabled-password -G appuser appuser && \
    addgroup appuser clamav

RUN touch /var/lib/clamav/clamd.sock && \
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