FROM centos:latest

RUN yum install -y epel-release 
RUN yum install -y git gcc clang cmake make gcc-c++  python2  libpcap yara python-pip jq
RUN pip install plyara
RUN mkdir -p /usr/local/include/ && \
cd /usr/local/include/ && \
        curl -O http://www.colm.net/files/ragel/ragel-6.9.tar.gz && \
        tar -zxf ragel-6.9.tar.gz && cd ragel-6.9 && ./configure && make && make install && \
        cd /usr/local/include/ && \
		curl -L -O https://dl.bintray.com/boostorg/release/1.68.0/source/boost_1_68_0.tar.gz && \
        tar -zxf boost_1_68_0.tar.gz && cd /usr/local/include/boost_1_68_0/tools/build && ./bootstrap.sh && ./b2 install --prefix=/usr/local/include/boost && \
        cd /usr/local/include/ && \
	    git clone https://github.com/intel/hyperscan.git && \
        ln -s /usr/local/include/boost_1_68_0/boost /usr/local/include/hyperscan/include/boost && \
	mkdir /usr/local/include/hs && \
        cd /usr/local/include/hs && \
        #HotFix for boost 1.68.0
        sed -i '983s/distance/std::distance/' /usr/local/include/hyperscan/src/nfa/limex_compile.cpp && \
        sed -i '1010s/distance/std::distance/' /usr/local/include/hyperscan/src/nfa/limex_compile.cpp && \

        cmake /usr/local/include/hyperscan

RUN cd /usr/local/include/hs && \
        cmake --build .

