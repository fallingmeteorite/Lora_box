CALL activate %~dp0venv
python install_fasttagger.py
cd font-roboto
python setup.py install
pause
