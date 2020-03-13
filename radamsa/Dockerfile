FROM debian:10-slim AS builder

LABEL MAINTAINER=cincan.io
ENV VERSION=0.6

RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    g++ \
    make \
    git \
    ca-certificates \
    pkg-config \
    libboost-dev \
    wget

RUN git clone https://gitlab.com/akihe/radamsa.git &&\
    cd radamsa &&\
    make && make install

FROM debian:10-slim AS production

COPY --from=builder /radamsa /radamsa

RUN ls -l /radamsa

ENTRYPOINT ["/radamsa/bin/radamsa"]

RUN groupadd -g 1000 appuser && \
    useradd -u 1000 -g appuser -s /sbin/nologin appuser

USER appuser
WORKDIR /home/appuser

CMD ["--help"]
