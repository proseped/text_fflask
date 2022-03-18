s1 = {1,2,3}
s2 = {2,3,4}
print(s2 & s1)  #与
print(s2 | s1)  #或
print(s2 ^ s1)  #抑或
print(s2 - s1)  #差

#判断一个集合是否是一个集合的子集
print({1, 2, 3}.issubset({1, 2, 3, 4}))
#判断一个集合是否是另一个集合的超集
print({1, 2, 3, 4}.issuperset({1, 2, 3}))