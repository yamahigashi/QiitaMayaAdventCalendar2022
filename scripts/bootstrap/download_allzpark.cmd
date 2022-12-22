@echo off
setlocal

pushd
cd /D %~dp0\..\..\bin\python\win
python -m pip install allzpark==1.2.183 --upgrade
python -m pip uninstall PySide2 -y
popd
