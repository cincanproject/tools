FROM debian:10
LABEL MAINTAINER=cincan.io
ENV VERSION=0.13.0

# stage 1
ARG DEBIAN_FRONTEND=noninteractive
RUN \
  apt-get update && \
  apt-get -q -y install wget && \
  wget -q https://github.com/BurntSushi/xsv/releases/download/0.13.0/xsv-0.13.0-x86_64-unknown-linux-musl.tar.gz && \
  tar -C / -zxf xsv-*.tar.gz xsv && \
  cd / && \
  sha256sum /xsv && \
  echo "271e798160472830d7151673383afaba4c37209673f5157cf37e8f5e308f1cac  xsv" | sha256sum -c

# stage 2
FROM busybox:latest
COPY --from=0 /xsv /bin/xsv
RUN chown root:root /bin/xsv && chmod 555 /bin/xsv
USER 4242
ENTRYPOINT ["/bin/xsv"]

