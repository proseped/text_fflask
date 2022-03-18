# l = list([123,4,5,6,6,7,8])
# print(l)
# l = list(range(10))
# print(l)
# l = list(range(1,10,1))
# print(l)
# #通过生成式创建列表
# #l[代表值的表达式 筛选值的条件语句 遍历值得循环语句]
# #筛选值得条件语句一般省略
# l = [i for i in range(1,10)]
# print(l)
# l = [i/2 for i in range(1,10,2)]
# print(l)
# l = [pow(i,2) for i in range(4)]
# print(l)
# import math
# #创建一个列表，其元素是半径为1,2,3，，，10的圆的面积
# l = [math.pi*i**2 for i in range(11)]
# lt =[]
# for j in l:
#     if j == 0:
#         break
#     else:
#         lt += j
# print(l)
#
# l = [i for i in range(1,100) if i % 7 == 0]
# print(l)
#
# l = [i ** 2 if i > 5 else i / 2 for i in range(1,10)]
# print(l)

#创建一个列表，其元素是半径为1,2,3，，，10的圆的面积,将面积大于50的值加入列表
l = [3.14*i**2 for i in range(1,11) if 3.14*i**2 >50]
print(l)

#遍历1——10内所有的数，奇数立方和，偶数平方和加入列表
l = [i**2 if i % 2 ==0 else i**3 for i in range(1,11)]
print(l)








