@echo off
setlocal

pushd
cd /D %~dp0\..\..\bin\python\win
python -m pip install PyQt5 --upgrade
popd
