FROM rust:1.36-slim

LABEL MAINTAINTER=cincan.io

RUN cargo install twiggy \
    && adduser --shell /sbin/nologin --disabled-login --gecos "" appuser

USER appuser

ENTRYPOINT ["twiggy"]
