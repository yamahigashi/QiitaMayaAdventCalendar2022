@echo off
setlocal

rem https://www.python.org/downloads/release/python-3913/

pushd
cd /D %~dp0\..\..\rez-packages\third\github.com\pyblish\pyblish_base\1.8.10

powershell -Command "(New-Object System.Net.WebClient).DownloadFile('https://github.com/pyblish/pyblish-base/archive/refs/tags/1.8.10.zip', '1.8.10.zip')"
powershell -Command "Expand-Archive 1.8.10.zip -DestinationPath ."
rem move /Y pyblish-base-1.8.10\* .

popd


pushd
cd /D %~dp0\..\..\rez-packages\third\github.com\pyblish\pyblish_maya\2.1.10

powershell -Command "(New-Object System.Net.WebClient).DownloadFile('https://github.com/pyblish/pyblish-maya/archive/refs/tags/2.1.10.zip', '2.1.10.zip')"
powershell -Command "Expand-Archive 2.1.10.zip -DestinationPath ."
rem move /Y pyblish-maya-2.1.10\* .

popd


pushd
cd /D %~dp0\..\..\rez-packages\third\github.com\pyblish\pyblish_qml\1.11.4

powershell -Command "(New-Object System.Net.WebClient).DownloadFile('https://github.com/pyblish/pyblish-qml/archive/refs/tags/1.11.4.zip', '1.11.4.zip')"
powershell -Command "Expand-Archive 1.11.4.zip -DestinationPath ."
rem move /Y pyblish-qml-1.11.4\* .
popd

cd /D %~dp0\..\..\bin\python\win
python -m pip install pyblish_base==1.8.8 --upgrade
python -m pip install pyblish_qml==1.11.4 --upgrade
python -m pip install pyblish_maya==2.1.8 --upgrade
popd
