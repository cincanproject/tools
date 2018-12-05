# Use pestudiox.exe for CLI
FROM microsoft/windowsservercore:latest
SHELL ["powershell"]
ENV PESTUDIO_URL https://www.winitor.com/tools/pestudio/current/pestudio.zip
RUN Write-Host ('Downloading {0} ...' -f $env:PESTUDIO_URL); \
	[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12; \
	Invoke-WebRequest -Uri $env:PESTUDIO_URL -OutFile 'pestudio.zip'; \
	Write-Host 'Expanding ...'; \
	Expand-Archive pestudio.zip -DestinationPath "."; \
	Write-Host 'Complete.'
RUN setx /M PATH $($env:PATH + ';C:\pestudio')
