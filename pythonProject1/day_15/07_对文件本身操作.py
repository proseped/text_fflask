import os
import shutil

path = r'D:\BaiduNetdiskDownload\python学习整套'
ls = os.listdir(path)
print(ls)

# 判断路径下，是否存在文件或文件夹
ret = os.path.exists(path + r"\第一部分")
print(ret)

# 判断指定路径下文件，是文件还是文件夹

path += r"\第二部分"
if os.path.isdir(path):
    print("是文件夹")
elif os.path.isfile(path):
    print("是文件")

# 在指定文件下创建一个文件夹
# path = r'D:\BaiduNetdiskDownload\python学习整套'
# path += r"\dir"
# os.makedirs(path)

path = r'D:\BaiduNetdiskDownload\python学习整套\dir\新建文本文档.txt'
# 获取文件大小
print(os.path.getsize(path))

# 复制一个文件，导入头文件shutil
# shutil.copyfile(path, path+"b")

# 修改一个文件的名字
# os.renames(path + 'b',path + '-copy')

# 移动一个文件，..表示上一级文件
path = 'D:\BaiduNetdiskDownload\python学习整套\dir'
shutil.move(path + r'\file',path + r"\..\file")