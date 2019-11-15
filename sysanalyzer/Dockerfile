FROM mcr.microsoft.com/windows/servercore:ltsc2019
SHELL ["powershell"]
ENV SYSANALZR_URL http://sandsprite.com/CodeStuff/SysAnalyzer_Setup.exe
RUN Write-Host ('Downloading {0} ...' -f $env:SYSANALZR_URL); \
	[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12; \
	Invoke-WebRequest -Uri $env:SYSANALZR_URL -OutFile 'sysanalyzer.exe'; \
	Write-Host 'Complete.'
RUN Start-Process -FilePath "C:\sysanalyzer.exe" -ArgumentList '/S /v/qn' -PassThru
RUN setx /M PATH $($env:PATH + ';C:\iDEFENSE\SysAnalyzer')
