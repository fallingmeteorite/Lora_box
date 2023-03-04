import zipfile

print("开始解压fastTagger.zip")
with zipfile.ZipFile(r"fastTagger.zip") as zf:
    zf.extractall()
print("解压完成")
