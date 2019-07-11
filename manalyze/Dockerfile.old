# Usage:
# $ docker build <path/to/manalyze/>

FROM ubuntu:18.04
USER root

RUN apt update
RUN apt-get install -y libboost-regex-dev libboost-program-options-dev libboost-system-dev libboost-filesystem-dev libssl-dev build-essential cmake git

RUN git clone https://github.com/JusticeRage/Manalyze.git /root/Manalyze && cd /root/Manalyze && cmake . && make
ENV PATH="/root/Manalyze/bin:${PATH}"
