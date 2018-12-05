FROM microsoft/windowsservercore:latest
SHELL ["powershell"]
RUN Set-ExecutionPolicy Bypass -Scope Process -Force
RUN iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))
RUN choco install processhacker -y
RUN setx /M PATH $($env:PATH + ';C:\Program Files\Process Hacker 2')
