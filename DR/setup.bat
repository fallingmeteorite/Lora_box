@echo
CALL activate %~dp0venv
pip list
pip uninstall 1.12.1+cu116 torchvision==0.13.1+cu116 -y
pip3 install numpy --pre torch[dynamo] torchvision torchaudio --force-reinstall --extra-index-url https://download.pytorch.org/whl/nightly/cu116
cd accelerate-main
python setup.py install
cd..
cd lion-pytorch-main
python setup.py install
cd..
pip install xformers-0.0.17+b89a493.d20230304-cp310-cp310-win_amd64.whl
pip install dynamo
pip install --use-pep517 --upgrade -r DE\requirements.txt --no-warn-script-location -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install basicsr==1.4.2
python tools\cudann_1.8_install.py
copy .\bitsandbytes_windows\*.dll .\venv\Lib\site-packages\bitsandbytes\
copy .\bitsandbytes_windows\cextension.py .\venv\Lib\site-packages\bitsandbytes\cextension.py
copy .\bitsandbytes_windows\main.py .\venv\Lib\site-packages\bitsandbytes\cuda_setup\main.py
accelerate config
pause
