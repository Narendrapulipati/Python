@echo off
 
title Test batch script


start chrome.exe https://geeks3d.com/dl/show/803
set DOWNLOAD_URL=https://geeks3d.com/downloads/2025/fm2/FurMark_2.8.0.0_win64.zip
set OUTPUT_FILE=%~dp0file.zip
powershell -Command "Invoke-WebRequest -Uri '%DOWNLOAD_URL%' -OutFile '%OUTPUT_FILE%'"
echo Download complete!

python "C:\Users\npulipat\Documents\Batch_script\run.py"
echo Running the test for 30sec
timeout /t 30 /nobreak >nul
echo closing the application
taskkill /f /im FurMark.exe
taskkill /f /im FurMark_GUI.exe

exit
pause