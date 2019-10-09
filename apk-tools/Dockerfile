#Analyzes Android apk files using apk tool and

#Build: 
#docker build -t cincan/apk-tools

 
FROM 

LABEL MAINTAINER=cincan.io
LABEL io.cincan.input= ""
LABEL io.cincan.output=""

COPY cincan /cincan

RUN

USER appuser 

ENTRYPOINT ["apktools"]
CMD["--help"]
