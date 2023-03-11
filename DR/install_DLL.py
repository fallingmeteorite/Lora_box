import time
import zipfile
import shutil
import os
print("开始解压mwxKTEtelILoIbMbruuM.zip")
with zipfile.ZipFile(r"DR\mwxKTEtelILoIbMbruuM.zip") as zf:
    zf.extractall()
print("解压完成")
time.sleep(2)
print("开始移动文件")

origin_path_one=r'cudnn_windows\cudnn_adv_infer64_8.dll'
origin_path_two=r'cudnn_windows\cudnn_cnn_infer64_8.dll'
origin_path_three=r'cudnn_windows\cudnn_cnn_train64_8.dll'
origin_path_four=r'cudnn_windows\cudnn_ops_infer64_8.dll'
origin_path_five=r'cudnn_windows\cudnn_ops_train64_8.dll'
origin_path_six=r'cudnn_windows\cudnn64_8.dll'
new_file_name=r'DR'
try:
    shutil.move(origin_path_one, new_file_name)
    shutil.move(origin_path_two, new_file_name)
    shutil.move(origin_path_three, new_file_name)
    shutil.move(origin_path_four, new_file_name)
    shutil.move(origin_path_five, new_file_name)
    shutil.move(origin_path_six, new_file_name)
    print("移动文件完成")
except:
    print("已存在")
time.sleep(4)
print("删除源文件")
shutil.rmtree("cudnn_windows")
os.remove("DR\mwxKTEtelILoIbMbruuM.zip")
print("源文件删除完成")

