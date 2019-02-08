#"Searches through git repositories for high entropy strings and secrets, 
# digging deep into commit history"
#
#build:
#docker build -t cincan/trufflehog .
#
#usage:
#docker run cincan/trufflehog https://<GIT>/<USERNAME>/sample.git <OPTIONS>
#  or
#docker run -v /samples:/samples cincan/trufflehog file:///samples/<GIT-DIR>/ <OPTIONS>
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
