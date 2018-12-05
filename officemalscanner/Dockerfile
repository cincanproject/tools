FROM microsoft/windowsservercore:latest
SHELL ["powershell"]
ENV OFFICEMALSCNR_URL http://www.reconstructer.org/code/OfficeMalScanner.zip
RUN Write-Host ('Downloading {0} ...' -f $env:OFFICEMALSCNR_URL); \
	[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12; \
	Invoke-WebRequest -Uri $env:OFFICEMALSCNR_URL -OutFile 'officemalscnr.zip'; \
	Write-Host 'Expanding ...'; \
	Expand-Archive officemalscnr.zip -DestinationPath "."; \
	Write-Host 'Complete.'
RUN setx /M PATH $($env:PATH + ';C:\OfficeMalScanner')
