# "TruffleHog Searches through git repositories for accidentally committed secrets!".
#
# build:
# docker build -t cincan/trufflehog .
#
# usage:
# docker run -v /samples:/samples cincan/trufflehog file:///samples/<GIT-DIR>/ <OPTIONS>
#   or
# docker run cincan/trufflehog https://github.com/<USERNAME>/sample.git <OPTIONS>
#
# Some <OPTIONS>:
# --json        Output in JSON
# --regex       High signal regex checks


FROM alpine:latest
RUN apk update && apk upgrade && apk --no-cache add \
        python3 \
        git
RUN pip3 install trufflehog
ENTRYPOINT ["trufflehog"]
CMD ["-h"]
