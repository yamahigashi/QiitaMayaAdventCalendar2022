@echo off


set REL_PATH=%~dp0..\bin\python-3.9\win
set ABS_PATH=

rem ////////////////////////////////////////////////////////////////////////////
rem // Save current directory and change to target directory
pushd %REL_PATH%

rem // Save value of CD variable (current directory)
set ABS_PATH=%CD%

set PATH=%CD%\Scripts;%CD%;%PATH%
set PYTHONHOME=%CD%

rem // Restore original directory
popd
rem ////////////////////////////////////////////////////////////////////////////

set REL_PATH=%~dp0..\rez-packages
set ABS_PATH=

rem // Save current directory and change to target directory
pushd %REL_PATH%

rem // Save value of CD variable (current directory)
set ABS_PATH=%CD%

set REZ_CONFIG_FILE=%CD%\rezconfig.py
set ALLZPARK_CONFIG_FILE=%CD%\allzparkconfig.py

popd
rem ////////////////////////////////////////////////////////////////////////////

rem call %~dp0py-venv\Scripts\activate.bat
