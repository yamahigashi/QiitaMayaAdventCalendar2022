@echo off
setlocal

rem https://www.python.org/downloads/release/python-3913/

pushd
cd /D %~dp0\..\..\bin

if not exist "python-3.9" ^
mkdir python-3.9
mkdir python-3.9\win

cd /D python-3.9\win
if not exist "python-3.9.13-embed-amd64.zip" ^
echo downloading python3.9.13...
powershell -Command "(New-Object System.Net.WebClient).DownloadFile('https://www.python.org/ftp/python/3.9.13/python-3.9.13-embed-amd64.zip', 'python-3.9.13-embed-amd64.zip')"
powershell -Command "Expand-Archive python-3.9.13-embed-amd64.zip -DestinationPath ."
mkdir Lib
mkdir Lib\site-packages
echo Lib\site-packages>> python39._pth

set PATH=%_PATH%
popd
