l = list(range(1,10,2))
print(l)

l = [i for i in range(1,10,2)]
print(l)

l = [i/2 for i in range(1,10,2)]
print(l)

# 练习 创建一个列表，其半径是1,2,3.。。的圆的面积
l = [3.14*(i**2) for i in range(1, 11) if i > 3]
print(l)

# 遍历1-10，奇数求立方加列表，偶数求平方加列表
l = [i**2 if i % 2 == 0 else i**3 for i in range(1,11)]
print(l)