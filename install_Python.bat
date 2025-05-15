@echo off
setlocal

python --version 2>nul | findstr /i "3.13" >nul
if %errorlevel% neq 0 (
    echo Python 3.13 is not installed. Downloading and installing Python 3.13...
    powershell -Command "Invoke-WebRequest -Uri https://www.python.org/ftp/python/3.13.3/python-3.13.3-amd64.exe -OutFile python-3.13.3-amd64.exe"
    echo Installing Python 3.13...
    python-3.13.3-amd64.exe /quiet InstallAllUsers=1 PrependPath=1

    python --version 2>nul | findstr /i "3.13" >nul
    if %errorlevel% neq 0 (
        echo Python 3.13 installation failed. Please install it manually.
        exit /b
    )

    del python-3.13.3-amd64.exe
    echo Python 3.13 installation completed successfully.
) else (
    echo Python 3.13 is already installed.
)

pause
