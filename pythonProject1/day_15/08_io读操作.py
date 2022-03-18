# I/O input, output.对文件内容的操作
# 从磁盘到内存为读，打开文件，加载模型。
# 从内存到磁盘为写。保存，容器。

path = r'D:\BaiduNetdiskDownload\python学习整套\dir\haha.txt'
file = open(path, 'r', encoding="GBK")

# 全部读入
s = file.read()
print(s)

# 在文件操作中有一个虚拟的读写指针，记录着读写的进度，下次读写只能接着读写。
# 重定向读写指针。参数是字节数
file.seek(0)
s = file.read()
print(s)