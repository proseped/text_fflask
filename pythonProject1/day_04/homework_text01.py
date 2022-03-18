# 作业：
# *1.1！+2！+3！+4!+5!+6! = ?
#迭代法
# for i in range(6):
#     y = y + 1
#     x = x * y
#     n = n + x
# print(n)

# 2.任意输入两个数，从较小的数，加到较大的数，求和
# 如输入：4 64
# 输出 15			（4 + 5 + 6）
# a =int(input("请输入第一个数："))
# b = int(input("请输入第二个数："))
# if a > b:
#     for i in range(b,a+1):
#         sum = sum + i
#         print(sum)

# 3.输入起始值，结束值和步数（step）数数
# 如输入：1 9 2
# 输出 1 3 5 7 9
# a = int(input("请输入起始值："))
# b = int(input("请输入结束值："))
# c = int(input("请输入step:"))
# for i in range(a ,b+1, c):
#     print(i)

# 4.输入任意多的数，用0结尾，求这些数的和
# s = 0
# while True:
#     x = int(input())
#
#     if x == 0:
#         break
#     s += x
# print(s)

# 5.输入一个正整数，判断这个数是不是偶数
# a = int(input('请输入一个正整数:'))
# if a > 0 & a % 2 == 0:
#     print("a是偶数")
# elif a <= 0:
#     print("请重新输入一个正整数")
# else:
#     print("输入错误！")


# 6.输入一个正整数，判断这个数是不是奇数

# *7.输入一个正整数，判断这个数是不是2的幂数
# a = int(input('请输入一个正整数:'))
# if a > 0 & a // 2 == 0:
#     print("a是二的幂数")
# elif a <= 0:
#     print("请重新输入一个正整数")
# else:
# #     print("输入错误！")

# *8.输入一个正整数，判断这个数是否是质数
# n = int(input())
# i = 2
# while i < n:
#     if n % i == 0:
#         break
#     i += 1
# if n == i:
#     print("是质数")
# else:
#     print("是合数")
# *9.输入一个正整数，分解质因数

# 如输入 90
# 输出 90=2X3X3X5
# a = int(input("请输入一个正整数："))
# lt = []
# b = a
# while a > 1:
#     for i in range(2,a+1):
#         if a % i == 0:
#             a = a // i
#             lt.append(str(i))
#             break
# if len(lt) == 1:
#     print(b,"1*",b)
# else:
#     s = "*".join(lt)
#     print(b,"=",s)


# 10.输入1个大于1的正整数，求如果将这个数拆成两个正整数的和，如何拆使两数的乘积最大
# 比如5 可以拆成 1 + 4 或 2 + 3
# 输出乘积
# a = int(input("请输入一个大于一的正整数："))
# m = 0
# for i in range(1,a//2 + 1):
#     b = a - i
#     if i * b > m:
#         循环，出现跟大的数将m更新
#         m = i*b
# print(m)

# for i in range(1,a):90

#     b = a - i
#     c = max(i*b)
#     print(c)

# 11.输入两个数，求两个数的阶乘和
#import math
# sum = 0
# f = 1
# a = int(input("请输入第一个数字："))
# b = int(input("请输入第二个数字："))
# for i in range(1,a+1):
#     f = f*i
#     sum += f
#     print("阶乘之和：",sum)
#     break


# 12.输入十分秒，打印这个时间往后，1小时的所有秒数
# 如输入：23：12：13
# 输出：23：12：14
# 	23：12：15
# 	...
# h,m,s = int(input()),int(input()),int(input())
# for i in range(60*60):
#     s += 1
#     if s == 60:
#         m += 1
#         s = 0
#         if m == 60:
#             h += 1
#             m = 0
#             if h == 24:
#                 h = 0
#     print(h,":",m,":",s)
#
