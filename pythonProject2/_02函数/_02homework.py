# 1.编写一个函数参数传入一个秒数，返回时间字符串
# 传入：61
# 返回：00: 01:01
def get_time(seconds):
    h = seconds // 3600
    m = seconds % 3600 // 60
    s = seconds % 60
    return "%.2d:%.2d:%.2d"%(h, m, s)


print(get_time(3708))
# 2.编写不定长参数函数，传入n个正整数，返回最大公约数
def max_redice(*a):
    r = a[0]
    while True:
        all = True
        for i in a:
            if i % r != 0:
                all = False
                break
        if all:
            return r
        else:
            r -= 1


print(max_redice(4,12,16,7))

# 3.编写函数，传入一个字符串，打印如下图形：
# 传入：ABCDE
# 打印:
#        A
#       BAB
#      CBABC
#     DCBABCD
#    EDCBABCDE
def get_pohots(s:str):
    length = len(s)
    for i in range(1,length+1):
        print(" "*(length-i),end="")
        print(s[i-1:0:-1],end="")
        print(s[0:i])


get_pohots("ABCDE")
# 4.编写函数，传入三个数，返回三数的立方和
def get_sun(a,b,c):
    return a**3+b**3+c**3
print(get_sun(1,2,3))

# ➢马克思手稿中有一道趣味数学题:有30个人，其中有男人、女人和小孩，在一家饭馆里吃饭
# 共花了50先令，每个男人各花3先令，每个女人各花2先令，每个小孩各花1先令，问男人、
# 女人和小孩各有几人?
def get_people():
    for m in range(1,29):
        for w in range(1,30-m):
            for c in range(1, 31-m-w):
                if m*3+ w*2 + c == 50 and m+w+c == 30:
                    men, women, child = m, w, c
                    print("男人:{} 女人:{} 小孩:{}".format(men, women, child))
print(get_people())

# 解方程组
# 编写程序，采用穷举法求出结果。
# ➢编写程序，根据以下公式求e的值。要求用两种方法计算:
# 11111.
# 1
# 1) for循环，计算前50项
# 1!2!3!4!5!
# n!
# 2)while循环，直至最后一项的值小于10-4

# ➢从键盘中输入-个数字(不限位数)，用循环语句编程判断并输出这个数字的位数。
# ➢猴子吃桃子问题。猴子第一 天摘下若干个桃，当即只一半，又多吃-一个。第二天早上又将剩下
# 的一半吃掉- -半，双多吃-一个。以后每天早上都吃了前天剩下的- -半零一个，到第10 天早上
# 只剩下最后一个桃。问第一天摘了几个桃。

# ➢编程打印九九乘法表

# ➢青年歌手参加歌曲大奖赛， 有10个评委打分，试编程求选手的平均得分(去掉-一个最高分和
# -一个最低分)。.
