#方式一
s = "姓名：{}，年龄：{}，身高：{}，体重：{}".format("张三",15,158,62)
print(s)
#方式二
s = "姓名：%s,年龄：%d,身高：%f,体重：%f"%("李四",15,152,56)
print(s)

#进制转换
a = 23
print("%d"%a)#十进制
print("%o"%a)#八进制
print("%x"%a)#十六进制

#保留小数位数
print("%f"%1.235)
print("%.2f"%1.2355)
print("%.10f"%1.26555)

#整形对齐
h,m,s = 14,7,35
print("%d:%d:%d"%(h,m,s))
print("%2d:%2d:%2d"%(h,m,s))
print("%-2d:%-2d:%-2d"%(h,m,s))
print("%.2d:%.2d:%.2d"%(h,m,s))

#修改print函数最后字符
for i in range(1,10):
    for j in range(1,i+1):
        print("{}*{}={}".format(j,i,j*i),end="\t\t")
    print()



