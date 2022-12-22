@echo off

pushd %~dp0
if not exist "python" ^
call ..\scripts\initialize_allzpark.bat

call ..\scripts\set_python_env.bat
python ..\scripts\launch_allzpark.py
popd

exit /b %errorlevel%
