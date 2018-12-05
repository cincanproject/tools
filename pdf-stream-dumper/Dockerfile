FROM microsoft/windowsservercore:latest
SHELL ["powershell"]
ENV PDFSTREAMDUMPER_URL http://sandsprite.com/CodeStuff/PDFStreamDumper_Setup.exe
RUN Write-Host ('Downloading {0} ...' -f $env:PDFSTREAMDUMPER_URL); \
	[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12; \
	Invoke-WebRequest -Uri $env:PDFSTREAMDUMPER_URL -OutFile 'pdfstrmdmpr.zip'; \
	Write-Host 'Expanding ...'; \
	Expand-Archive pdfstrmdmpr.zip -DestinationPath "."; \
	Write-Host 'Complete.'
RUN setx /M PATH $($env:PATH + ';C:\pdfstrmdmpr')
