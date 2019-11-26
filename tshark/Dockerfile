FROM alpine:3.10

LABEL MAINTAINER=cincan.io
ENV VERSION=3.0.4-r0

RUN apk update && apk add --no-cache tshark=${VERSION}

ENTRYPOINT ["tshark"]
CMD ["--help"]

# Add an user
RUN mkdir -p /home/appuser \
    && adduser -D appuser \
    && chown -R appuser:appuser /home/appuser

USER appuser
WORKDIR /home/appuser
