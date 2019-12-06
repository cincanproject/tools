FROM debian:8-slim AS builder

LABEL MAINTAINER=cincan.io
ENV VERSION=0.6

RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc=4:4.9.2-2 \
    g++=4:4.9.2-2 \
    make=4.0-8.1 \
    git=1:2.1.4-2.1+deb8u7 \
    ca-certificates=20141019+deb8u4 \
    pkg-config=0.28-1 \
    libboost-dev=1.55.0.2 \
    wget=1.16-1+deb8u6

RUN git clone https://gitlab.com/akihe/radamsa.git &&\
    cd radamsa &&\
    make && make install

FROM debian:8-slim AS production

COPY --from=builder /radamsa /radamsa

RUN ls -l /radamsa

ENTRYPOINT ["/radamsa/bin/radamsa"]

RUN groupadd -g 1000 appuser && \
    useradd -u 1000 -g appuser -s /sbin/nologin appuser

USER appuser
WORKDIR /home/appuser

CMD ["--help"]
