FROM microsoft/windowsservercore:latest
SHELL ["powershell"]
ENV PYTHON_URL https://www.python.org/ftp/python/2.7.15/python-2.7.15.amd64.msi
RUN Write-Host ('Downloading {0} ...' -f $env:PYTHON_URL); \
	[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12; \
	Invoke-WebRequest -Uri $env:PYTHON_URL -OutFile 'python.msi';
RUN Start-Process msiexec.exe -Wait -Argumentlist '/I C:\python.msi /quiet'
RUN setx /M PATH $($env:PATH + ';C:\Python27;C:\Python27\Scripts')
RUN setx /M PYTHONIOENCODING "UTF-8"
ENV PDFPARSER_URL https://didierstevens.com/files/software/pdf-parser_V0_6_9.zip
RUN Write-Host ('Downloading {0} ...' -f $env:PDFPARSER_URL); \
	[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12; \
	Invoke-WebRequest -Uri $env:PDFPARSER_URL -OutFile 'pdfparser.zip'; \
	Write-Host 'Expanding ...'; \
	New-Item -ItemType Directory -Path C:\pdfparser | Out-Null; \
	Expand-Archive pdfparser.zip -DestinationPath C:\pdfparser; \
	Write-Host 'Complete.'
