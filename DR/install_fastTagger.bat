CALL activate %~dp0venv
python install_fasttagger.py
cd font-roboto
pip install setup.py install
pause
