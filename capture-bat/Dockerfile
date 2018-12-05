FROM microsoft/windowsservercore:latest
SHELL ["powershell"]
ENV CBAT_URL https://www.honeynet.org/files/CaptureBAT-Setup-2.0.0-5574.exe
RUN Write-Host ('Downloading {0} ...' -f $env:CBAT_URL); \
	[Net.ServicePointManager]::SecurityProtocol = 
[Net.SecurityProtocolType]::Tls12; \
	Invoke-WebRequest -Uri $env:CBAT_URL -OutFile 'cbat.exe'; \
	Write-Host 'Complete.'
RUN Start-Process -FilePath "C:\cbat.exe" -ArgumentList '/S /v/qn' -PassThru
RUN setx /M PATH $($env:PATH + ';C:\Program Files (x86)\Capture')
