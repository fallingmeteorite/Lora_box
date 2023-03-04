set curpath=%~dp0 
cd /d %curpath%
set exename=fastTagger.zip
set downurl=https://huggingface.co/Fallingmeteorite/xformers-0.0.17/resolve/main/fastTagger.zip
powershell curl -o "%exename%" "%downurl%"
python install_fasttagger.py
pause