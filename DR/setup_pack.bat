CALL activate %~dp0venv
pip install requests==2.28.2
python install_data.py
cd..
python DR\install_DLL.py
cd DR
python setup_pack.py
copy .\bitsandbytes_windows\*.dll .\venv\Lib\site-packages\bitsandbytes\
copy .\bitsandbytes_windows\cextension.py .\venv\Lib\site-packages\bitsandbytes\cextension.py
copy .\bitsandbytes_windows\main.py .\venv\Lib\site-packages\bitsandbytes\cuda_setup\main.py
copy distributed_c10d.py .\venv\Lib\site-packages\torch\distributed
pause