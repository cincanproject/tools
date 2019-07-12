FROM python:3.5.7-alpine3.10

RUN apk update && apk add --no-cache \
    git \
    graphviz \
    g++ \
    make \
    subversion \
    gcc \
    ca-certificates \
    python3-dev \
    libpng-dev \
    freetype-dev \
    libffi-dev \
    openssl-dev \
    musl-dev \
    linux-headers \
    && git clone https://github.com/MalwareCantFly/Vba2Graph.git \
    && ln -s /usr/include/locale.h /usr/include/xlocale.h \
    && pip3 install -U oletools \
    && python3 -m pip --no-cache-dir install matplotlib

WORKDIR /Vba2Graph
RUN pip3 install -r requirements.txt

ENTRYPOINT ["/usr/bin/python","/Vba2Graph/vba2graph.py"]
CMD ["-h"]




#Ubuntu-version, faster to build, but bigger by ~100Mb
#
#FROM ubuntu:16.04
#RUN apt-get update && apt-get install -y \
#        python-pip \
#        git \
#        graphviz
#
#RUN git clone https://github.com/MalwareCantFly/Vba2Graph.git
#RUN pip install -U oletools && cd /Vba2Graph && pip install -r requirements.txt
#ENTRYPOINT ["/usr/bin/python","/Vba2Graph/vba2graph.py"]
#CMD ["-h"]

