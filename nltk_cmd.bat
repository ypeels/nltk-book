@echo off
rem Python Tutorial 2.2.4: could also setenv PYTHONSTARTUP to setup ".pythonrc.py" on system AND dir level
rem ... but i'm not gonna do that

rem nope, "from nltk.book import *" does NOT traverse the python path, like i thought it would
rem set PYTHONPATH=%CD% 

rem http://www.nltk.org/data.html - instead, set ANOTHER environment variable
set NLTK_DATA=%CD%\nltk_data

rem Yapari saikyou 
rem http://stackoverflow.com/questions/5811966/windows-batch-script-get-current-drive-name
set DRIVE=%~d0
doskey idle="%DRIVE%\Users\Jonathan\Documents\Qt\projs-2008\Portable-Python-2.7.3.2\IDLE-Portable.exe"

set QT_HOME=C:\Progra~2\QtSDK1.1\Desktop\Qt\4.7.3\msvc2008\bin\qtenv2.bat
set QT_WORK=C:\Progra~2\Qt\QtSDK1.1\Desktop\Qt\4.7.3\msvc2008\bin\qtenv2.bat
if exist %QT_HOME% (
	C:\Windows\System32\cmd.exe /A /Q /K %QT_HOME%
) else (
	C:\Windows\System32\cmd.exe /A /Q /K %QT_WORK%
)