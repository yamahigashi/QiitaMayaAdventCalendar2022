@echo off
setlocal

rem https://www.python.org/downloads/release/python-3913/

pushd
cd /D %~dp0\..\..\rez-packages\third\github.com\mgear-dev\mgear\4.0.9

powershell -Command "(New-Object System.Net.WebClient).DownloadFile('https://github.com/mgear-dev/mgear4/releases/download/4.0.9/mgear_4.0.9.zip', 'mgear_4.0.9.zip')"
powershell -Command "Expand-Archive mgear_4.0.9.zip -DestinationPath ."

popd

