
@REM admin Powershell
@REM start-process PowerShell -verb runas


@REM install chocolety
@"%SystemRoot%\System32\WindowsPowerShell\v1.0\powershell.exe" -NoProfile -InputFormat None -ExecutionPolicy Bypass -Command "[System.Net.ServicePointManager]::SecurityProtocol = 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))" && SET "PATH=%PATH%;%ALLUSERSPROFILE%\chocolatey\bin"

@REM  install quietly
choco install nodejs -y

@REM install vlc
choco install vlc -y

@REM install peerflix in nodejs
npm install -g peerflix

@REM install qbittorrent
choco install qbittorrent -y





