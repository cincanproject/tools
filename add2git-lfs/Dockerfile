FROM alpine:3.9

LABEL MAINTAINER=cincan.io

RUN apk update && apk add --no-cache\
    git=2.20.1-r0 \
    curl=7.64.0-r2 \
    wget=1.20.3-r0

WORKDIR /add2git-lfs

RUN wget https://github.com/saguywalker/add2git-lfs/releases/download/0.1.7/add2git-lfs \
    && chmod +x add2git-lfs \
    && curl -s https://packagecloud.io/install/repositories/github/git-lfs/script.deb.sh \
    && apk add git-lfs \
    && git lfs install
WORKDIR /samples
EXPOSE 12358
ENTRYPOINT ["/add2git-lfs/add2git-lfs"]
