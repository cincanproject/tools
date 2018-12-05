# 1. docker build . -tag jakstab
# 2. docker run -it -m 4GB jakstab powershell
# 3. Expand-Archive "./jakstab.zip" -DestinationPath "./jakstab"
# 4. cd ./jakstab/jkinder-jakstab-20cc4fa
# 5. .\compile.bat
# 6. $env:PATH+="C:/jakstab/jkinder-jakstab-20cc4fa;"
# 7. .\jakstab.bat

FROM microsoft/windowsservercore:latest

SHELL ["powershell", "-Command", "$ErrorActionPreference = 'Stop'; $ProgressPreference = 'SilentlyContinue';"]

ENV JAVA_HOME C:\\openjdk-12
RUN $newPath = ('{0}\bin;{1}' -f $env:JAVA_HOME, $env:PATH); \
	Write-Host ('Updating PATH: {0}' -f $newPath); \
	setx /M PATH $newPath

ENV JAVA_VERSION 12-ea+17
ENV JAVA_URL https://download.java.net/java/early_access/jdk12/17/GPL/openjdk-12-ea+17_windows-x64_bin.zip
ENV JAVA_SHA256 c12daec9fa6bab9797c35cb01f282914f5bed0850647307a6e1117a0b855cd22

RUN Write-Host ('Downloading {0} ...' -f $env:JAVA_URL); \
	[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12; \
	Invoke-WebRequest -Uri $env:JAVA_URL -OutFile 'openjdk.zip'; \
	Write-Host ('Verifying sha256 ({0}) ...' -f $env:JAVA_SHA256); \
	if ((Get-FileHash openjdk.zip -Algorithm sha256).Hash -ne $env:JAVA_SHA256) { \
		Write-Host 'FAILED!'; \
		exit 1; \
	}; \
	Write-Host 'Expanding ...'; \
	New-Item -ItemType Directory -Path C:\temp | Out-Null; \
	Expand-Archive openjdk.zip -DestinationPath C:\temp; \
	Move-Item -Path C:\temp\* -Destination $env:JAVA_HOME; \
	Remove-Item C:\temp; \
	Write-Host 'Verifying install ...'; \
	Write-Host '  java --version'; java --version; \
	Write-Host '  javac --version'; javac --version; \
	Write-Host 'Removing ...'; \
	Remove-Item openjdk.zip -Force; \
	Write-Host 'Complete.'

ENV JAKSTAB_URL https://github.com/jkinder/jakstab/zipball/master
RUN Write-Host ('Downloading {0} ...' -f $env:JAKSTAB_URL); \
	[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12; \
	Invoke-WebRequest -Uri $env:JAKSTAB_URL -OutFile 'jakstab.zip';
