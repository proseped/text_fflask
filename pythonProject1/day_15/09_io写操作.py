path = r'D:\BaiduNetdiskDownload\python学习整套\dir\haha.txt'
# file = open(path, 'w', encoding="GBK")
# # 这样打开文件，会将数据全部清空
# file.write("我是一个粉刷匠！")
# file.close()

# 追加写入，不会清空数据，追加指针在文件末尾
file = open(path, 'a', encoding="GBK")
file.write("粉刷本领强！")
file.write("粉刷本领强！")

# r 只读方式打开，读写指针在文件首
# w 清空文件并以只写方式打开，读写指针在文件首也是文件尾
# a 以只写的方式打开，读写指针在文件尾
# r+ 在只读方式中，添加写权限。可读可写，读写指针在文件首。
# w+ 在w的方式中，增加读权限，可读可写，内容清空
# a+ 在a的方式中，增加读权限，可读可写，读写指针在文件尾。
# rb 跟r基本一样，但是读取的文件是任何文件，读到的是二进制码
# wb 。。。
# ab 。。。
# rb+ 。。。
# wb+ 。。。
# ab+ 。。。
