FROM microsoft/windowsservercore:latest
SHELL ["powershell"]
ENV SYSINTERNALS_URL https://download.sysinternals.com/files/SysinternalsSuite.zip
RUN Write-Host ('Downloading {0} ...' -f $env:SYSINTERNALS_URL); \
	[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12; \
	Invoke-WebRequest -Uri $env:SYSINTERNALS_URL -OutFile 'sysinternals.zip'; \
	Write-Host 'Expanding ...'; \
	New-Item -ItemType Directory -Path 'C:\sysinternals' | Out-Null; \
	Expand-Archive 'sysinternals.zip' -DestinationPath 'C:\sysinternals'; \
	Write-Host 'Complete.'
