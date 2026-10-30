@echo off
chcp 65001 >nul
cd /d "%~dp0"
set "msg=%~1"
if "%msg%"=="" set /p "msg=提交说明: "
if "%msg%"=="" set "msg=update"
echo.
echo [1/3] git add .
git add .
echo [2/3] git commit
git commit -m "%msg%"
echo [3/3] git push
git push
echo.
echo 完成。按任意键关闭。
pause >nul
