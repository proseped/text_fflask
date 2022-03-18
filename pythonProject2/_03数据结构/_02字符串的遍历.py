s = "天生我材必有用,sky borb me must have road!"
for i in s:
    print(i,end="")
print("\n==============")
for i in range(0,len(s),2):
    print(s[i],end="")
print("\n==============")
for i in s[::2]:
    print(i,end="")
print("\n==============")

for i in range(len(s)-1,-1,-1):
    print(s[i],end="")
print("\n==============")
for i in s[::-1]:
    print(i,end="")
print("\n==============")

# 随机找出部分字符
import random
x = random.sample("abcdefg",3)
print(x,end="")