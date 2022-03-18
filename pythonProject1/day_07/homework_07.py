# ※※※1.编写函数传入两个正整数，求两个数的最大公约数
# def do_max_count(*n):
#     x = n[0]
#     while True:
#         all = True
#         for i in n:
#             if i % x != 0:
#                 all = False
#                 break
#         if all:
#             return x
#         else:
#             x -= 1
#
# print(do_max_count(2,4))

# ※※※※2.编写函数传入一个正奇数，打印下列图形
# 传入5
# 打印
#   *
#  ***
# *****
# def print_count(s):
#     l = [i for i in range(1,s+1) if i % 2 != 0]
#     for j in l:
#         print(" "*((s-j)//2),end = "")
#         print("*"*j)
# print_count(5)
# # ※3.编写函数传入一个字符串，将他逆序返回
# 传入 abc
# 打印 cba
#def print_str(s:str):
    # lt = [s]
    # for i in s:
    #     lt += i
    # lt.reverse()
    # print(lt)

# def resver(s):
#     return s[::-1]
# print(resver("difjios"))

#print_str("123456")
#我能怎么办，我也很绝望啊


# ※※※※4.编写函数传入一个字符串，打印如下图形
# 传入 abcdefg
# 打印
# abcdefg
#      f
#     e
#    d
#   c
#  b
# abcdefg
# def print_picture(s:str):
#     print(s)
#     l = len(s) - 2
#     for i in s[-2:0:-1]:
#         print(" " * l, end="")
#         print(i)
#         l -= 1
#     print(s)
# print_picture("abcdefg")
# ※※5.编写函数传入一个字符串，将字符串中的所有数字都去掉
# 传入 abc123d4h4
# 返回 abcdh
# def count_del(s:str):
#     ls = ""
#     for i in s:
#         if i not in "0123456789":
#             ls += i
#     return ls


#print(count_del("abc123d4h4"))
#print(len("1234"))
# ※※6.编写函数传入一个字符串，和一个数字n，将字符串全部字符左移n位，最左侧的字符移到右侧
# 传入 abcdefg 3
# 返回 defgabc
# def remove(s:str,n:int):
# def jf(s:str):
#     ls = []
#     for i in s:
#         ls += i
#     print(ls)
# jf("sfhsfsk")
# def remone(s:str,n):
#     n %= len(s)
#     n_s = s[n:] + s[:n]
#     return n_s
# print(remone("abcdefg",3))
# ※※7.编写函数传入一个字符串，将重要信息放在[]之间，找出重要信息
# 传入 我是一个[好人]
# 返回 好人
# def get_impotant(s:str):
#     index1 = s.find("[")
#     index2 = s.find("]")
#     if index2 < 0 or index1 < 0 or index1 > index2:
#         return None
#     return s[index1+1:index2]
# print(get_impotant("我是一个[好人]"))

# ※8.编写函数传入一个字符串，判断字符串中abc出现了多少次
# def get_count(s:str):
#     count = 0
#     for i in s:
#         if i in "abc":
#             count += 1
#     print(count)
# get_count("aaccbbjoireo")
# ※※※9.编写函数传入一个字符串，判断字符串中有多少aba
# 传入 ababa
# 返回 2
# def get_count(s:str,cs:str):
#     count = 0
#     while True:
#         ret = s.find(cs)
#         if ret >= 0:
#             count += 1
#             s = s[ret+1:]
#         else:return count
# print(get_count("abababababa","aba"))
# ※※※※※10.编写函数传入两个字符串，打印出最长的公有部分，如果出现并列最长，以第一个字符串首次出现为准
# 传入 abcdefg cdefghi
# 返回 cdefg
# 传入 abcdefg defgabc
# 返回 defg
# 传入 abcdefxyzhi  cdefqqxyzhxx
# 返回 cdef
# def get_max(s:str,s2:str):
#     longest = 0
#     lstr = None
#     for i in range(0,len(s)):
#         count = 0
#         for j in range(i+1,len(s)+1):
#             if s[i:j] in s2:
#                 count += 1
#                 continue
#             else:break
#         if longest < count:
#             longest = count
#             lstr = s[i:i+count]
#     return lstr
# print(get_max("abcdefxyzhi"," cdefqqxyzhxx"))
#


# ※11.编写函数传入一段英文文字，没有标点，单词间用单空格隔开，求，有多少个单词
# def get_count(s:str):
#     ls = []
#     for i in s:
#         ls += i
# print(len(ls))
# ※※12.编写函数在上一题基础上，将每个单词首字母大写
# 传入 hello world
# 返回 Hello World.编写函数
# def get_max(s:str):
#     s.title()
#     ls = s.split()
#     return len(ls)
# print(get_max("hello world"))

# 作业：
# 1.编写函数※传入一段英文文字，没有标点，单词间用单空格或多空格隔开，求，有多少个单词
# def get_count(s:str,s2:str):
#     count = 0
#     for i in s:
#         if i in s2:
#             count += 1
#     print(count)
# get_count("adfs  ff","abcdefghijklmnopqrstuvwxyz")

# 2.编写函数※※传入10个数字，10个数字都用空格隔开，将10个数字从大到小返回
# [字符串分割]
# def get_max(*a):
#     ls = []
#     for i in a:
#         ls += [i]
#     ls.sort(reverse=True)
#     print(ls)
# get_max(3,4,6,7,9,8,2,1,5,0)

# 3.编写函数※※传入三个单词，用空格隔开，将三个单词，用[]进行包裹
# 传入 hello world good
# 返回 [hello][world][good]
# def split_word(s:str):
#     ls = s.split(" ")
#     while "" in ls:
#         ls.remove("")
#     return "[" + "][".join(ls) + "]"
# print(split_word("hello  world   world"))

# 4.编写函数※※※传入一个带中括号的时间，将时间转成秒数
# 传入[00:01:03]你是我的心
# 返回63->你是我的心
# def _s(s:str):
#     index1 = s.find("[")
#     index2 = s.find("]")
#     timr_str = s[index1 + 1:index2]
#     l = timr_str.split(":")
#     seconds = int(l[0])*3600 +int(l[1])*60 + int(l[2])
#     return "{} -> {}".format(seconds,s[:index1]+s[index2+1:])
# print(_s("违反了[00:01:06]我是你飞行"))


# 5.编写函数※※传入10个时间，找出最大的一个传入格式[00:00:00]

# 6.编写函数※传入一个单词和一个语句，找出单词在语句中出现的次数
# def get_count(s:str,s2:str):
#     count = 0
#     for i in s2:
#         if s == i:
#             count += 1
#     print(count)
# get_count("the","you are the biutful one the the")

# 7.编写函数※传入一个语句，由单词和空格组成，将每个单词逆序再拼回一个字符串
# 传入：hello world
# 返回：olleh dlrow
# def resver(s:str):
#     ls = s.split(" ")
#     l = []
#     for i in ls:
#         l.append(i[::-1])
#     return " ".join(l)
# print(resver("hello world"))


# 8.编写函数※※传入多个单词，用空格分割，打印最长的一个单词，或多个单词
# def get_max(s:str):
#     ls = s.split()
#     longest = 0
#     for i in ls:
#         if len(i) > longest :
#             longest = len(i)
#     for j in ls :
#         if len(j) == longest:
#             print(j)
# get_max("hello world goood")







