@echo off
REM 声明采用UTF-8编码
chcp 65001
echo 开始下载重要文件!!!文件较大!!!请耐心等待!!!(时间由网络决定)(保险起见：中途请不要进行任何操作)!!!

set curpath=%~dp0 
cd /d %curpath%
set exename=mwxKTEtelILoIbMbruuM.zip
set downurl=https://b1.thefileditch.ch/mwxKTEtelILoIbMbruuM.zip
powershell curl -o "%exename%" "%downurl%"

set curpath=%~dp0 
cd /d %curpath%
set exename=xformers-0.0.17%2Bb89a493.d20230304-cp310-cp310-win_amd64.whl
set downurl=https://huggingface.co/Fallingmeteorite/xformers-0.0.17/resolve/main/xformers-0.0.17%2Bb89a493.d20230304-cp310-cp310-win_amd64.whl
powershell curl -o "%exename%" "%downurl%"

conda create --prefix=%~dp0venv python=3.10.6 -y
CALL activate %~dp0venv
cd..
python DR\install_DLL.py
pause