#### Fixed

* __dotnetdecompile__
    * distro: mcr.microsoft.com/dotnet/core/sdk:2.2-alpine3.9
    * errors:
        * wrong string in assert, fixed
* __manalyze__
    * distro: debian:9-slim
    * errors:
        * `E       assert False`
        * sometimes passes, assert should be correct
* __flawfinder__
    * distro: alpine:3.10
    * errors:
        * `E               docker.errors.BuildError: The command '/bin/sh -c apk update && apk add --no-cache python3=3.7.3-r0     && pip3 install flawfinder==2.0.10     && adduser -s /sbin/nologin -D appuser' returned a non-zero code: 1`
        * `ERROR: unsatisfiable constraints: python3-3.7.4-r0: breaks: world[python3=3.7.3-r0]`
            * dependency error, fixed by changing python3 requirement to python3=3.7.4-r0
* __snowman-decompile__
    * distro: debian:9-slim
    * errors:
        * `E: Version '6.0-21+deb9u1' for 'unzip' was not found`
        * Changed requirement to 6.0-21+deb9u2, now builds correctly

#### to-do

* __hyperscan__
    * distro: centos:latest
    * errors:
        * `E               docker.errors.BuildError: The command '/bin/sh -c yum install -y git gcc clang cmake make gcc-c++  python2  libpcap yara python-pip jq' returned a non-zero code: 1`
            * Caused possibly by centos:latest updating to Centos 8 (there is no build for Yara in epel with 8)
        * Hyperscan won't build: ```/usr/local/include/hyperscan/src/nfa/limex_compile.cpp:983:32: error: 'std::std' has not been declared
         return verify_u32(std::std::distance(squash.begin(), it));
                                ^
/usr/local/include/hyperscan/src/nfa/limex_compile.cpp: In function 'u32 ue2::{anonymous}::addReports(const ue2::flat_set<unsigned int>&, std::vector<unsigned int>&, ue2::{anonymous}::ReportListCache&)':
/usr/local/include/hyperscan/src/nfa/limex_compile.cpp:1010:38: error: 'std::std' has not been declared
         u32 offset = verify_u32(std::std::distance(begin(reports), it));
                                      ^
gmake[2]: *** [CMakeFiles/hs_compile.dir/src/nfa/limex_compile.cpp.o] Error 1
gmake[1]: *** [CMakeFiles/hs_compile.dir/all] Error 2
gmake: *** [all] Error 2
The command '/bin/sh -c cd /usr/local/include/hs &&         cmake --build .' returned a non-zero code: 2```

#### Broken by Microsoft

* __regshot__
    * distro: microsoft/windowsservercore:latest
    * errors:
        * `E       docker.errors.APIError: 500 Server Error: Internal Server Error ("ENV must have two arguments")`
        * newlines in Dockerfile without \ 
            * fixed
        * Microsoft deprecated `latest` tag from its distributions, fixed but cannot test on Linux
* __capture-bat__
    * distro: microsoft/windowsservercore:latest
    * errors:
        * `E       docker.errors.APIError: 400 Client Error: Bad Request ("Dockerfile parse error line 6: unknown instruction: [NET.SECURITYPROTOCOLTYPE]::TLS12;")`
            * newlines in Dockerfile without \ 
            * fixed
        * Microsoft deprecated `latest` tag from its distributions, fixed but cannot test on Linux
* __sysanalyzer__
    * distro: microsoft/windowsservercore:latest
    * errors:
        * `E       docker.errors.APIError: 400 Client Error: Bad Request ("Dockerfile parse error line 6: unknown instruction: [NET.SECURITYPROTOCOLTYPE]::TLS12;")`
            * newlines in Dockerfile without \ 
            * fixed
        * Microsoft deprecated `latest` tag from its distributions, fixed but cannot test on Linux

