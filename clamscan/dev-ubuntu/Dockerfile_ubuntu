FROM ubuntu:18.10

RUN apt update && apt install -qqy clamav

RUN freshclam
  
ENTRYPOINT ["/usr/bin/clamscan"]
CMD ["--help"