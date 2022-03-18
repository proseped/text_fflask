# 六个数据结构 number str tuples list dict set 前三不可变，后三可变
s = "姓名:{} 年龄:{} 升高:{}".format("张三", 18, 1.15)
print(s)
s = "姓名:%s 年龄:%d 升高:%f"%("张三", 18, 1.15)
print(s)
y, m, d = 1995, 12, 5
print("%.2d:%.2d:%.2d" % (y, m, d))

# 打印九九乘法表
for i in range(1,10):
    for j in range(1,i+1):
        print("{}x{}={}".format(j, i, j*i), end="\t")
    print("")