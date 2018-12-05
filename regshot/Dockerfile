FROM microsoft/windowsservercore:latest
SHELL ["powershell"]
ENV 7ZIP_URL http://www.7-zip.org/a/7z1604-x64.msi
RUN Write-Host ('Downloading {0} ...' -f $env:7ZIP_URL); \
	[Net.ServicePointManager]::SecurityProtocol = 
[Net.SecurityProtocolType]::Tls12; \
	Invoke-WebRequest -Uri $env:7ZIP_URL -OutFile '7zip.msi';
RUN Start-Process msiexec.exe -Wait -Argumentlist '/I C:\7zip.msi /quiet'
RUN setx /M PATH $($env:PATH + ';C:\Program Files\7-Zip')
ENV REGSHOT_URL 
"https://sourceforge.net/projects/regshot/files/regshot/1.9.0/Regshot-1.9.0.7z/download"
RUN Write-Host ('Downloading {0} ...' -f $env:REGSHOT_URL); \
	[Net.ServicePointManager]::SecurityProtocol = 
[Net.SecurityProtocolType]::Tls12; \
	Invoke-WebRequest -Uri $env:REGSHOT_URL -OutFile 'regshot.7z' -UserAgent 
[Microsoft.PowerShell.Commands.PSUserAgent]::FireFox; \
	Write-Host 'Expanding ...'; \
	7z x regshot.7z -y; \
	Write-Host 'Complete.'
