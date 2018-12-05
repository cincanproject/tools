FROM ubuntu:18.04
RUN apt-get update && apt-get install -y \
        python \
        python3 \
        wget \
        unzip
ENV DEBIAN_FRONTEND=noninteractive
RUN wget -O binwalk.zip https://github.com/ReFirmLabs/binwalk/archive/master.zip
RUN unzip binwalk.zip
WORKDIR binwalk-master
RUN sed -i 's/"${2:-$(lsb_release -r|cut -f 2|cut -c1-2)}"/18/g' deps.sh
RUN ./deps.sh --yes
RUN python setup.py install
RUN rm -rf /var/lib/apt/lists/*
ENTRYPOINT ["/usr/local/bin/binwalk"]
