#"PDFID will scan a file to look for certain PDF keywords, allowing you to 
# identify PDF documents that contain (for example) JavaScript or execute 
# an action when opened. PDFiD will also handle name obfuscation."
#
#build:
# docker build -t cincan/pdfid .
#
#basic usage:
# docker run -v /samples:/samples cincan/pdfid /samples/sample.pdf
#
#run with triage-plugin:
# docker run -v /samples:/samples cincan/pdfid /samples/sample.pdf -p plugin_triage
#
#Plugins list:
# plugin_embeddedfile.py
# plugin_nameobfuscation.py
# plugin_triage.py

FROM alpine:latest
RUN apk update && apk add \
	python \
	wget \
	unzip \
	git

RUN wget didierstevens.com/files/software/pdfid_v0_2_5.zip \
    && unzip pdfid_v0_2_5.zip -d /pdfid \
    && rm *.zip

ENTRYPOINT ["/usr/bin/python", "pdfid/pdfid.py"]

