FROM alpine:latest
RUN apk update && apk upgrade && apk add \
        python3
RUN pip3 install flawfinder
ENTRYPOINT ["flawfinder"]
