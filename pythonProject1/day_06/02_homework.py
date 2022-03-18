# 1.
# 编写一个函数参数传入一个秒数，返回时间字符串
# 传入：61
# 返回：00: 01:01
# def print_s(s):
#     h,m = 0,0
#     while s >= 60:
#         s = s - 60
#         m += 1
#         while m >= 60:
#             m = m -60
#             h += 1
#             while h >= 24:
#                 h = 0
#     print("%.2d:%.2d：%.2d" % (h, m, s))
# print_s(61)
#

# 2.
# 编写不定长参数函数，传入n个正整数，返回最大公约数
# def max_reduce(*n):
#     r = n[0]
#     while True:
#         all = True
#         for i in n:
#             if i % r != 0:
#                 all = False
#                 break
#         if all:
#             return r
#         else:
#             r -= 1
# print(max_reduce(4,8,12,16,27,56))

# 3.
# 编写函数，传入一个字符串，打印如下图形：
# 传入：ABCDE
# 打印:
# A
# BAB
# CBABC
# DCBABCD
# EDCBABCDE
# 4.
# def print_str(s:str):
#     l = len(s)
#     for i in range(1,l+1):
#         print(" "*(l-i),end="")
#         print(s[i-1:0:-1],end="")
#         print(s[0:i])
# print_str("ABCDE")

# 编写函数，传入三个数，返回三数的立方和
# def print_count(a,b,c):
#     a = a**3
#     b = b**3
#     c = c**3
#     sum = a+b+c
# #    return sum
#     print(sum)
#
# print_count(1,2,3)


#➢马克思手稿中有一道 趣味数学题:有30个人，其中有男人、女人和小孩，在一家饭馆里吃饭共花了50先令，
# 每个男人各花3先令，每个女人各花2先令，每个小孩各花1先令，问男人、女人和小孩各有几人?
# m + w + c == 30
# 3 * m + 2 * w + c ==50
# print(m,w,c)
# def num_people():
#     for m in range(1,29):
#         for w in range(1, 29):
#             for c in range(1, 29):
#                 if m*3 + w*2 + c == 50 and m + w + c == 30:
#                     print("男人:{} 女人:{} 小孩:{}".format(m,w,c))
# num_people()

# 解方程组
#
# 编写程序，采用穷举法求出结果。
#
# ➢编写程序，根据以下公式求e的值。要求用两种方法计算: .
#
# 1
#
# e≈1+-+-+-+-
#
# 1) for循环， 计算前50项1!2!3!4!5!
#
# n!
#
# 2)while循环，直至最后-项的值小于10-4
#
# ➢从键盘中输入- -个数字(不限位数)，用循环语句编程判断并输出这个数字的位数。
#
# ➢猴子吃桃子问题。猴子第一 天摘下若干个桃，当即只一半，又多吃- -个。第二天早上又将剩下的一半吃掉- -半，
# 双多吃一-个。以后每天早上都吃了前天剩下的-半零一个，到第10 天早上只剩下最后一一个桃。问第一天摘了 几个桃。
# x = 1
#
# for i in range(10):
#     sum = x*2 +1
# print(sum)

# ➢编程打印九九乘法表
# for i in range(1,10):
#     for j in range(1,i+1):
#         print("%.2d * %.2d = %.2d"%(j,i,j*i),end="\t\t")
#     print()


# ➢青年歌手参加歌曲大奖赛，有10个评委打分，试编程求选手的平均得分(去掉一 个最高分和-个最低分)。
#
#
#
#
#
#
