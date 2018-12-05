FROM alpine:latest
RUN apk update && apk upgrade && apk --no-cache add \
        python3 \
        git
RUN pip3 install trufflehog
ENTRYPOINT ["trufflehog"]
CMD ["-h"]
