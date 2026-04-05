@echo off
echo ----- Zero Install - by Rafaeltas -----
echo:
REM Upgrade All Softwares
winget upgrade
if %ERRORLEVEL% EQU 0 Echo Upgrade softwares successfully.
echo.

winget install Google.Chrome
if %ERRORLEVEL% EQU 0 Echo Google Chrome installed successfully.
echo.

powershell -Command "Invoke-WebRequest https://discord.com/api/downloads/distributions/app/installers/latest?channel=stable&platform=win&arch=x86 -Outfile "$env:userprofile\Downloads\discord.exe"
echo "Download Done!"
timeout 5
echo Installing Discord
start /wait "" "%userprofile%\Downloads\discord.exe"
if %ERRORLEVEL% EQU 0 Echo Discord Installation successfully.
DEL %userprofile%\Downloads\discord.exe
:: End Discord process.

::REM Discord
::winget install Discord.Discord --accept-source-agreements
::if %ERRORLEVEL% EQU 0 Echo Discord installed successfully.
::echo.
REM 7-ZIP
winget install 7zip.7zip --accept-source-agreements
if %ERRORLEVEL% EQU 0 Echo 7-ZIP installed successfully.
echo.
REM OBS
winget install OBSProject.OBSStudio --accept-source-agreements
if %ERRORLEVEL% EQU 0 Echo OBS Studio installed successfully.
echo.

REM LibreOffice
winget install LibreOffice
if %ERRORLEVEL% EQU 0 Echo LibreOffice installed successfully.
echo.
REM Spotify
winget install Spotify.Spotify --accept-source-agreements
if %ERRORLEVEL% EQU 0 Echo Spotify installed successfully.
echo.
REM qBittorrent
winget install qBittorrent.qBittorrent --accept-source-agreements
if %ERRORLEVEL% EQU 0 Echo qBittorrent installed successfully.
echo.
REM Stremio
winget install stremio --accept-source-agreements
if %ERRORLEVEL% EQU 0 Echo Stremio installed successfully.
echo.


::Download Nvidia app Beta is done directly by Nvidia server
powershell -Command "Invoke-WebRequest https://us.download.nvidia.com/nvapp/client/11.0.6.383/NVIDIA_app_v11.0.6.383.exe -Outfile "$env:userprofile\Downloads\nvidia_app.exe"
echo "Download Done!"
timeout 5
cls
echo Installing Nvidia App
start /wait "" "%userprofile%\Downloads\nvidia_app.exe"
if %ERRORLEVEL% EQU 0 Echo Nvidia app Beta Installation successfully.
DEL %userprofile%\Downloads\nvidia_app.exe
:: End Nvidia App Beta process.
REM Steam
winget install Valve.Steam
if %ERRORLEVEL% EQU 0 Echo Steam installed successfully.
echo.
echo "Download League of Legends"
::Download of League of Legends is done directly by riot server
powershell -Command "Invoke-WebRequest https://lol.secure.dyn.riotcdn.net/channels/public/x/installer/current/live.br.exe -Outfile "$env:userprofile\Downloads\lol.exe"
echo "Download Done!"
timeout 5
cls
echo Installing League of Legends
start /wait "" "%userprofile%\Downloads\lol.exe"
if %ERRORLEVEL% EQU 0 Echo League of Legends Installation successfully.
DEL %userprofile%\Downloads\lol.exe
:: Command cls clear the terminal.
REM PowerShell 7
start /wait D:\"! Instaladores"\"PC Hardware"\PowerShell-7.4.1-win-x64.msi
if %ERRORLEVEL% EQU 0 Echo PowerShell 7 installed successfully.
echo.
cls
:: Create folder temporate to save textures.
cd C:\
timeout 2
mkdir temp
timeout 1
::Invoke-Item "C:\Windows\Resources\Themes\themeA.theme"
echo ==========================================================
echo Script Done, press any key to close this window!
echo ==========================================================
pause >nul
