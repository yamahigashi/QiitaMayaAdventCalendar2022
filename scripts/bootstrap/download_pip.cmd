@echo off
setlocal

pushd
cd /D %~dp0\..\..\bin\python\win

powershell -Command "(New-Object System.Net.WebClient).DownloadFile('https://bootstrap.pypa.io/get-pip.py', 'get-pip.py')"
python get-pip.py

