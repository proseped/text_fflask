#集合set
#集合中的数据是唯一的
#集合中的数据没有意义
#集合表示一个范围，用来判断一个数据是否从属于一个范围，因而对数据分类。

s = {1,3,4,5,6}
print(s)

s = set("hfdsivb")
print(s)

s = set(["jids","oo","idoihv"])
print(s)

s  = set((1,3,45,6,6,8,9))
print(s)

#可以遍历一个集合，但是没有意义
for i in s:
    print(i)

s = {1,3,4}
#判断一个数据是否属于这个集合
print(3 in s)
print(5 in s)

#添加元素
s.add(5)
print(s)
#随机删除一个元素
s.pop()
print(s)
#删除指定元素
print(s)
#清空
s.clear()
print(s)