import zipfile
import os
import sys
import requests
import time
import urllib3
buer = input("是否已下载fastTagger.zip(yes/no):")

while True:
    if buer == "no":
        print("开始下载fastTagger.zip")
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


        def download(url, file_path):
            # 重试计数
            count = 0
            # 第一次请求是为了得到文件总大小
            r1 = requests.get(url, stream=True, verify=False)
            total_size = int(r1.headers['Content-Length'])

            # 判断本地文件是否存在，存在则读取文件数据大小
            if os.path.exists(file_path):
                temp_size = os.path.getsize(file_path)  # 本地已经下载的文件大小
            else:
                temp_size = 0

            # 对比一下，是不是还没下完
            print(temp_size)
            print(total_size)

            # 开始下载
            while count < 10:
                if count != 0:
                    temp_size = os.path.getsize(file_path)
                # 文件大小一致，跳出循环
                if temp_size >= total_size:
                    break
                count += 1
                print(
                    "第[{}]次下载文件,已经下载数据大小:[{}],应下载数据大小:[{}]".format(
                        count, temp_size, total_size))
                # 重新请求网址，加入新的请求头的
                # 核心部分，这个是请求下载时，从本地文件已经下载过的后面下载
                headers = {"Range": f"bytes={temp_size}-{total_size}"}
                # r = requests.get(url, stream=True, verify=False)
                r = requests.get(url, stream=True, verify=False, headers=headers)

                # "ab"表示追加形式写入文件
                with open(file_path, "ab") as f:
                    if count != 1:
                        f.seek(temp_size)
                    for chunk in r.iter_content(chunk_size=1024 * 64):
                        if chunk:
                            temp_size += len(chunk)
                            f.write(chunk)
                            f.flush()
                            ###这是下载实现进度显示####
                            done = int(100 * temp_size / total_size)
                            sys.stdout.write("\r[%s%s] %d%%" % (
                                '█' * done, ' ' * (100 - done), 100 * temp_size / total_size))
                            sys.stdout.flush()
                print("\n")
            return file_path


        download("https://huggingface.co/Fallingmeteorite/fastTagger/resolve/main/fastTagger.zip", "fastTagger.zip")
        break
    elif buer == "yes":
        break

    else:
        print(r'输入错误，或未输入，请重新选择')

print("开始解压fastTagger.zip")
with zipfile.ZipFile(r"fastTagger.zip") as zf:
    zf.extractall()
print("解压完成")
os.remove("fastTagger.zip")
print("源文件删除完成")
print(r'安装依赖')
os.system(r'pip install basicsr==1.4.2')
os.system(r'pip install GitPython==3.1.31')
os.system(r'pip install piexif==1.1.3')
os.system(r'pip install fonts==0.0.3')
os.system(r'pip install omegaconf==2.3.0')
os.system(r'pip install open_clip_torch==2.16.0')
os.system(r'pip install lark==1.1.5')
os.system(r'pip install blendmodes==2022')
os.system(r'pip install jsonmerge==1.9.0')
os.system(r'pip install clean_fid==0.1.35')
os.system(r'pip install clip==0.2.0')
os.system(r'pip install resize_right==0.0.2')
os.system(r'pip install torchdiffeq==0.2.3')
os.system(r'pip install torchsde==0.2.5')
print(r'完成')