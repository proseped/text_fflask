#3、输入3个整数h,m,s，代表h小时m分钟s秒，计算总共多少秒并输出。例如1小时10分25秒是3600+600+25＝4225秒。
h = int(input("请输入一个整数："))
m = int(input("请输入一个整数："))
s = int(input("请输入一个整数："))
sum = h*3600 + m*60 + s
print(sum)