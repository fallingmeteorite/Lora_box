import os
import sys
import requests
import time

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

print(r'检测是否存在所需文件')
if os.path.exists('mwxKTEtelILoIbMbruuM.zip') == False:
    while True:
        print(r'所需文件并未存在')
        print(r'以下有两种方法')
        print(r' 1 自动下载(速度较快)')
        print(r' 2 手动用下载器下载(速度最快)')
        buer_three = input('你的选择是？(输入方法前面的数字):')
        if buer_three == '2':
            print(r'https://huggingface.co/Fallingmeteorite/xformers-0.0.17/resolve/main/xformers-0.0.17%2Bb89a493.d20230304-cp310-cp310-win_amd64.whl')
            print(r'https://b1.thefileditch.ch/mwxKTEtelILoIbMbruuM.zip')
            print(r'https://huggingface.co/Fallingmeteorite/fastTagger/resolve/main/fastTagger.zip')
            print(r'这是所需文件的下载地址,复制并粘贴到下载器')
            print(r'下载完成后，将文件放入DR文件夹中重新运行：启动安装依赖程序,严禁修改文件名')
            print(r'等待检测通过,若未通过请检查文件是否放对')
            input(r'确认并开始下载后,按下回车退出程序')
            print(r'4秒后退出')
            print(4)
            time.sleep(1)
            print(3)
            time.sleep(1)
            print(2)
            time.sleep(1)
            print(1)
            time.sleep(1)
            exit()
        elif buer_three == '1':
            print(r'请保证网络畅通，即将开始下载文件')
            print(r'花费时间根据网速决定')
            print(r'下载xformers-0.0.17')
            download("https://huggingface.co/Fallingmeteorite/xformers-0.0.17/resolve/main/xformers-0.0.17%2Bb89a493.d20230304-cp310-cp310-win_amd64.whl","xformers-0.0.17+b89a493.d20230304-cp310-cp310-win_amd64.whl")
            print(r'下载mwxKTEtelILoIbMbruuM.zip')
            download("https://b1.thefileditch.ch/mwxKTEtelILoIbMbruuM.zip","mwxKTEtelILoIbMbruuM.zip")
            print(r'下载标注器')
            download("https://huggingface.co/Fallingmeteorite/fastTagger/resolve/main/fastTagger.zip","fastTagger.zip")
            break
        else:
            print(r'输入错误，或未输入，请重新选择')
else:
    print(r'文件已存在，无需下载')
