FROM microsoft/windowsservercore:latest
SHELL ["powershell"]
ENV CNVRTSHELLCODE_URL https://sourceforge.net/projects/convertshellcode/files/latest/download
RUN Write-Host ('Downloading {0} ...' -f $env:CNVRTSHELLCODE_URL); \
	[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12; \
	Invoke-WebRequest -Uri $env:CNVRTSHELLCODE_URL -OutFile 'convertshellcode.zip' -UserAgent [Microsoft.PowerShell.Commands.PSUserAgent]::FireFox; \
	Write-Host 'Expanding ...'; \
	New-Item -ItemType Directory -Path C:\convertshellcode | Out-Null; \
	Expand-Archive convertshellcode.zip -DestinationPath "C:\convertshellcode"; \
	Write-Host 'Complete.'
RUN setx /M PATH $($env:PATH + ';C:\convertshellcode')
