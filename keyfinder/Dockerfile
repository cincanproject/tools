FROM ubuntu:18.04
USER root

RUN apt-get update && apt-get install -y \
        git \
        python3-pip

RUN git clone https://github.com/CERTCC/keyfinder.git
RUN pip3 install androguard python-magic PyOpenSSL

ENTRYPOINT ["/usr/bin/python3", "keyfinder/keyfinder.py"]


