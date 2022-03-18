# 2.设计一个分数的类，包含属性：
# 分子
# 分母
# 包含方法：
# 修改分子和分母
# 按照 分子/分母 方式输出
# 约分
# class Number:
#     def __init__(self, son, mother):
#         self.son, self.mother = son, mother
#
#     def change_number(self, son, mother):
#         self.son, self.mother = son, mother
#
#     def show(self):
#         print("{} / {}".format(self.son, self.mother))
#
#     def print_number(self):
#         sign = 1
#         if self.son * self.mother < 0:
#             sign = -1
#         self.son = abs(self.son)
#         self.mother = abs(self.mother)
#
#         _min = min(self.son, self.mother)
#         while True:
#             if self.son % _min == 0 and self.mother % _min == 0:
#                 break
#             else:
#                 _min -= 1
#         self.son //= _min * sign
#         self.mother //= _min
#
#
# t = Number(-6, 21)
# t.print_number()
# t.show()

# 3.设计一个账户信息的类
# 包含属性：
# 用户名
# 密码
# 昵称
# 注册时间：
# 最后访问时间：
# 包含方法：
# 访问（修改最后访问时间）
# 修改密码(要求传入旧密码和新密码，旧密码正确才能修改)
# 打印账户信息
# class Account:
#     def __init__(self, username, secret, name, fist, finally_time):
#         self.username, self.secret, self.name, self.fist, self.finally_time = username, secret, name, fist, finally_time
#
#     def change_finally_time(self, finally_time):
#         self.finally_time = finally_time
#
#     def change_secret(self, a, b):
#
#         if a == self.secret:
#             self.secret = b
#
#     def print_count(self):
#         return "用户名：%s 密码:%s 昵称:%s 注册时间%s 最后访问时间%s" %(self.username, self.secret, self.name, self.fist, self.finally_time)
#
#
# c =Account("0911",45556,"小科","2020.01.05","2020.01.08")
#
# print(c.print_count())
# c.change_finally_time("2020.01.18")
# c.change_secret(45556,94646)
# print(c.print_count())



# 4.设置矩形类，包含长和宽
# 方法：
# 返回面积
# 返回周长
# class Rectangle:
#     def __init__(self, long, wild):
#         self.long, self.wild = long, wild
#
#     def get_area(self):
#         return self.wild*self.long
#
#     def get_all_long(self):
#         return self.wild*2 + self.long*2
#
#
# c = Rectangle(9,3)
# print(c.get_area())
# print(c.get_all_long())
