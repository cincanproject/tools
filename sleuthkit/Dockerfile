### Usage: docker run -it -v `pwd`/samples:/samples cincan/sleuthkit [tool from sleuthkit]

FROM debian

RUN apt-get update && apt-get install -y --no-install-recommends git build-essential autotools-dev autoconf automake libtool man ca-certificates

RUN git clone --depth 1 https://github.com/sleuthkit/sleuthkit.git

RUN cd /sleuthkit && ./bootstrap && ./configure && make && make install && cd .. && rm -r sleuthkit

CMD fls
