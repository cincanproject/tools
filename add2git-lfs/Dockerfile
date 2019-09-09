FROM alpine:3.10

LABEL MAINTAINER=cincan.io

RUN apk update && apk add --no-cache \
    git=2.22.0-r0 \
    wget=1.20.3-r0 \
    git-lfs=2.7.2-r0

WORKDIR /add2git-lfs

RUN wget https://github.com/saguywalker/add2git-lfs/releases/download/0.1.8/add2git-lfs \
    && chmod +x add2git-lfs

WORKDIR /samples
EXPOSE 12358
ENTRYPOINT ["/add2git-lfs/add2git-lfs"]
