FROM microsoft/windowsservercore:latest
SHELL ["powershell"]
RUN Get-PackageProvider
RUN Get-PackageSource
RUN Register-PackageSource -Name "NuGet" -Trusted -Force -Location "https://www.nuget.org/api/v2" -Provider "NuGet"
RUN Get-PackageSource
RUN Install-Package Microsoft.CodeAnalysis.Binskim -Source "NuGet" -Force
RUN setx /M PATH $($env:PATH + ';C:\Program Files\PackageManagement\NuGet\Packages\Microsoft.CodeAnalysis.Binskim.1.5.1\tools\netcoreapp2.0\win-x64')