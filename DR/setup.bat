@echo
CALL activate %~dp0venv
pip list
pip uninstall 1.12.1+cu116 torchvision==0.13.1+cu116
pip install torch==1.13.1+cu117 torchvision==0.14.1+cu117 --extra-index-url https://download.pytorch.org/whl/
cd accelerate-main
python setup.py install
cd..
cd lion-pytorch-main
python setup.py install

pip install --use-pep517 --upgrade -r DE\requirements.txt --no-warn-script-location -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install xformers-0.0.16-cp310-cp310-win_amd64.whl
python tools\cudann_1.8_install.py
copy .\bitsandbytes_windows\*.dll .\venv\Lib\site-packages\bitsandbytes\
copy .\bitsandbytes_windows\cextension.py .\venv\Lib\site-packages\bitsandbytes\cextension.py
copy .\bitsandbytes_windows\main.py .\venv\Lib\site-packages\bitsandbytes\cuda_setup\main.py
cd lion-pytorch
python setup.py install
cd..
accelerate config
pause
