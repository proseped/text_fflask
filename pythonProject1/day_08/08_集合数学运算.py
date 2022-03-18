#集合可以进行数学运算
s1 = {1,2,3}
s2 = {2,3,4}
#求交集
s = s1.intersection(s2) #生成新的交集，原来的集合不变
print(s)

s1.intersection_update(s2)  #交集变为s1
print(s1)
print(s2)

#求并集
s1 = {1,2,3}
s2 = {2,3,4}
s3 = s1.union(s2)
print(s3)

s1.update(s2)
print(s1)
print(s2)

#求非交集
s1 = {1,2,3}
s2 = {2,3,4}
s = s1.symmetric_difference(s2)
print(s)

s1.symmetric_difference_update(s2)
print(s1)
print(s2)

#求差集    在第一个里面有的，在第二个里面没有
s1 = {1,2,3}
s2 = {2,3,4}
s = s1.difference(s2)
print(s)

s1.difference_update(s2)
print(s1)
print(s2)







