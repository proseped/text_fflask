# 写一个函数，接受一个整数，输出这个整数是几位数
# 获得这个数
# 1 - --->
# 1 // 10 = 0 - ---> 一位数
# 0 // 10 = 0 - ---> 1
# 9 // 10 = 0 - ---> 1
#
# 10 // 10 == 1
# 1 // 10 == 0 - ---> 2
#
# 100 // 10 == 10
# 10 // 10 = 1
# 1 // 10 = 0 - ---> 3

# def indexa(int):
#     if int // 10 == 0:
#         print("一位数")
#         if int // 10 == 1:
#             print("二位数")
#             if int // 10 == 2:
#                 print("三位数")
#
# print((indexa(155)))


#一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同
#
#
# def index(n:int):
#     i = 2
#     while i < n:
#         if n % i == 0:
#             break
#         i += 1
#     if n == i:
#         print("是质数")
#     else:
#         print("是合数")
#
# index(5)

# •    封装一个功能，判定一个数是不是质数【只能被1和本身整除】
#
# •    有5个人坐在一起，问第五个人多少岁？他说比第4个人大2岁。问第4个人岁数，
# 他说比第3个人大2岁。问第三个人，又说比第2人大两岁。问第2个人，说比第一个人大两岁。最后问第一个人，他说是10岁。请问第五个人多大？[递归]
# F(1) = 10
# F(2) = F(1) + 2
# F(3) = F(2) + 2
#
# F(n) = F(n - 1) + 2

# def age():
#     x = 10
#     for i in range(4):
#         x += 2
#     print(x)
# age()
# 5.
# 定义函数实现如下要求
# 例如：输入2，5，则求2 + 22 + 222 + 2222 + 22222
# 的和
# 规律:
# 1
# 位数
# 2
# 2
# 位数
# 22 + 2
#
# 2
# 22
# 222
# 使用递归写规律:
# 1 - - 2
# 2 - - 2 * 10 ^ 2 - 1 + 2
# F(1) = 2
# F(2) = 2 * 10 ** (2 - 1) + F(1)
# F(3) = 2 * 10 ** (3 - 2) + F(2)
#
# 2
# 22 + 2
# Sum(1) = 2
# Sum(2) = 22 + sum(1)
# Sum(3) = 222 + sum(2)
# def tosum(a:int,b:int):
#     sum = 0
#     for i in range(1,b):
#         a = a*10^i + a
#         sum += a
#     print(sum)
# tosum(2,5)

#
# 周末作业:
# 日历是以1900年1月1日00：00：00
# 为基础的
# 那天的星期1是已知的
# 时间戳 - -- 将已知时间获取其对应的秒数 - -- 是以1970年1月1号为基础

year = int(input("请输入年份:"))
if ((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)):run = True
else:run =False
sum = 0
i = 1900
while i < year-1:
    i += 1
    if ((i % 4 ==0 and i % 100 != 0 ) or (i % 400 == 0)):sum += 366
    else: sum += 355
month = int(input("请输入月份:"))
j = 1
while j < month:
    if ((j == 1) or (j == 3) or (j == 5) or (j == 7) or (j == 8) or (j == 10) or (j == 12)):sum += 31
    elif j == 2:
        if run:sum += 29
        else:sum += 25
    else:sum += 30
    j += 1
week = (sum + 1)%7
if((month == 1) or (month == 3) or (month == 5) or (month == 7) or (month == 8) or (month == 10) or (month == 12)):day = 31
elif month == 2:
    if run:day = 29
    else:day = 28
else:day = 30
print("日\t一\t二\t三\t四\t五\t六")
conut = 0
k = 0
while k <= week:
    k += 1
    print("\t",end="")
    conut += 1
    if(conut % 7 == 0):print("\n")
p = 1
while p <= day:
    print(p,"\t",end="")
    p += 1
    conut += 1
    if (conut % 7 == 0):
        print("\n")




















