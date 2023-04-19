# DreamBooth_with_Lora

这个整合包是给一些新手小白使用的.

# 提醒
提醒：一些特殊版本会在releases放出

# 说明
它也可以解决一些人因为环境问题而装不上的问题.

警告：这个整合包适用于windows10及其以上系统，

如果在其他系统上使用，出现问题，概不负责！

由于平时时间较少,更新较慢,不能及时的上传新功能.

在新功能出来时，请多注意这个项目.在新功能出来时，

我会尽快更新，并配置好新功能.

每一个发布的版本，一般都会说明更新了什么,

会说明存在问题,新增的有什么用.

# 使用要求

电脑必须安装Anaconda软件,这是必须的!

Anaconda软件官方网站：https://www.anaconda.com/

如果下载太慢可以使用清华镜像源

清华镜像源官方网站：https://mirrors.tuna.tsinghua.edu.cn/help/anaconda/

# 整合文件来源
这个整合包的训练代码来源：https://github.com/bmaltais/kohya_ss

Github加速器来源：https://github.com/dotnetcore/FastGithub

# 配置Anaconda软件

直接点击开始安装
图片来源于网上
![1](https://user-images.githubusercontent.com/86793086/221332894-352ef507-1fa3-4504-8c21-8647dfa11271.png)

一般来说，大家的电脑只有一个账户，默认选择Just me，如果你的电脑有多个账户，那就选择All Users
![2](https://user-images.githubusercontent.com/86793086/221332917-60219916-4d15-4445-a161-be4ff1d957a5.png)

选择安装区域时，如果你的C盘足够大，可以直接默认不用修改，默认安装到C盘也可以避免后续可能出现的众多小问题。

![3](https://user-images.githubusercontent.com/86793086/221332935-a7c7effd-6599-4f75-9be9-3f0295a974f8.png)

不过大部分人C盘空间不足，需要修改位置，这时要注意：要新建一个空文件夹；文件夹名称不要包含中文字符

比如，我在D盘创建了一个空文件夹，重命名为Anaconda，也推荐大家和我一样，方便后续的步骤操作

![4](https://user-images.githubusercontent.com/86793086/221332955-b3fc06af-2f1f-425f-a269-5759bb9933da.png)

不需要勾线第一个，网上有些教程中建议勾选，但这样容易出现污染环境变量等各种小问题，为了保险起见，还是不勾选这个，后续进行人工设置。

![5](https://user-images.githubusercontent.com/86793086/221332980-e440a5ef-bf7e-43da-bbbb-08e3cf18e505.png)

接下来就是等待，直到安装成功

![6](https://user-images.githubusercontent.com/86793086/221332998-696b2085-7799-4502-93fc-7053ec952681.png)

安装成功！

![7](https://user-images.githubusercontent.com/86793086/221333005-4aaeb3ac-f9a1-4819-b010-d40c2599b34d.png)

# 配置环境变量

进入环境变量设置中

![7](https://user-images.githubusercontent.com/86793086/221333058-aa20c4c3-5cd7-4570-84c0-2865d0b423ab.png)

系统变量中的Path

![1](https://user-images.githubusercontent.com/86793086/221333081-a58a7edb-2230-464d-b99c-d5fb3496a1a7.png)

如果你前面和我在D盘创建了名称一样的文件夹，那么直接粘贴即可

# 新建环境变量

D:\Anaconda

D:\Anaconda\Scripts

D:\Anaconda\Library\mingw-w64\bin D:\Anaconda\Library\usr\bin

D:\Anaconda\Library\bin

如果你前面和我在D盘创建了名称一样的文件夹，那么直接粘贴即可

![2](https://user-images.githubusercontent.com/86793086/221333127-3e21d4aa-e798-4208-92d8-3457a43bafcd.png)

上面的格式为：

你安装的盘+你的文件夹名称+后面不变的内容

例如：你把Anaconda安装到了E盘中名为Python的文件夹，那么你的格式为

E:\Python\Library\mingw-w64\bin

其余的类似这样，只需修改前面的内容

最后点击确定逐个退出即可

# 测试是否安装成功

在命令行中输入 conda

看是否有报错，没有就正常.

# 开始下载

在目标文件夹打开cmd

输入对应的克隆代码

进入克隆的文件夹,观看里面的使用说明

# 如何更新

在目标文件夹打开cmd

输入 git pull或在启动器中更新
