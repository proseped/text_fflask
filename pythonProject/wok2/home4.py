#4、输入一个整数代表秒数，转换成h小时m分钟s秒形式。例如输入4225，转换成1小时10分25秒并输出。
import math

h = int(input("请输入一个整数："))
a = h // 3600
b = (h-a * 3600) // 60
c = h % 3600 % 60

print("共需要",a,"小时",b,"分",c,"秒")