FROM ubuntu:16.04
USER root
RUN apt-get update && apt-get install -y \
        curl \
        build-essential
RUN curl https://sh.rustup.rs -sSf >> /tmp/rustup && sh /tmp/rustup -y
ENV PATH="/root/.cargo/bin:${PATH}"
RUN cargo install twiggy

ENTRYPOINT ["twiggy"]
