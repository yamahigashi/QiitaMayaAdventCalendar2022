@echo off

pushd %~dp0
call ..\scripts\set_python_env.bat
python ..\scripts\launch_allzpark.py
popd

exit /b %errorlevel%
