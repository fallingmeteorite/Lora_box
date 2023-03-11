import os
import time

net_one=(r'https://pypi.tuna.tsinghua.edu.cn/simple')
net_two=(r'http://mirrors.aliyun.com/pypi/simple/')
net_three=(r'https://pypi.mirrors.ustc.edu.cn/simple/')
net_four=(r'http://pypi.douban.com/simple/')
while True:
    print(r' 1 清华镜像源')
    print(r' 2 阿里云镜像源')
    print(r' 3 中国科技大学镜像源')
    print(r' 4 豆瓣镜像源')
    buer_one = input(r'你想要使用的镜像源是：(请输入前面的数字):')
    if buer_one == '1':
        print(r'已选择：清华镜像源')
        net = (r'https://pypi.tuna.tsinghua.edu.cn/simple')
        break
    elif buer_one == '2':
        print(r'已选择：阿里云镜像源')
        net = (r'http://mirrors.aliyun.com/pypi/simple/')
        break
    elif buer_one == '3':
        print(r'已选择：中国科技大学镜像源')
        net = (r'https://pypi.mirrors.ustc.edu.cn/simple/')
        break
    elif buer_one == '4':
        print(r'已选择：豆瓣镜像源')
        net = (r'http://pypi.douban.com/simple/')
        break
    else:
        print(r'输入错误，或未输入，请重新选择')
    time.sleep(4)

print(r'开始安装依赖包')
os.system(r'python -V')
os.system(r'pip install numpy --pre torch[dynamo] torchvision torchaudio --force-reinstall --extra-index-url https://download.pytorch.org/whl/nightly/cu116')
os.system(r'pip install --use-pep517 --upgrade -r DE\requirements.txt --no-warn-script-location -i '+net)
os.system(r'pip install xformers-0.0.17+b89a493.d20230304-cp310-cp310-win_amd64.whl')
os.system(r'pip install dynamo==0.1.1')
os.system(r'pip install triton-2.0.0-cp310-cp310-win_amd64.whl')
os.system(r"python tools\cudann_1.8_install.py")
print(r'运行完成')
print(r'4秒后退出')
time.sleep(4)
print(r'移动文件')
