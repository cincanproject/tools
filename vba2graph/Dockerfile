FROM alpine:latest

RUN apk --update --no-cache \
        add python \
        py-pip \
        git \
        graphviz

RUN git clone https://github.com/MalwareCantFly/Vba2Graph.git
RUN pip install -U oletools

RUN apk add g++ make subversion gcc gfortran ca-certificates python-dev libpng-dev freetype-dev
RUN ln -s /usr/include/locale.h /usr/include/xlocale.h
RUN python -m pip install matplotlib
RUN cd /Vba2Graph && pip install -r requirements.txt

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

