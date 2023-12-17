@echo off
setlocal enabledelayedexpansion
:: Получить текущий диск, на котором находится скрипт
for %%i in ("%~dp0") do set currentDrive=%%~di

:: Запустить скрипт на текущем диске
cmd /k "cd /d !currentDrive!\PythonProjects\Amanda-Lizard\venv\Scripts & activate & cd /d !currentDrive!\PythonProjects\Amanda-Lizard & python main.py"
@REM pause
