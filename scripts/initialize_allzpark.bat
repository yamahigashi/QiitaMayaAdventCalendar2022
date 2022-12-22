@echo off
setlocal

pushd
cd /D %~dp0

call bootstrap\download_python.cmd
call bootstrap\download_pip.cmd
call bootstrap\download_pyqt5.cmd
call bootstrap\download_allzpark.cmd
call bootstrap\download_package_pyblish.cmd
call bootstrap\download_package_mgear.cmd
popd
