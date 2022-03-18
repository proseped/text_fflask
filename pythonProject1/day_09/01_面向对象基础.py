# class Rectangle:
#     #成员变量，描述对象的特征
#     length,wild = 0.0,0.0
#     #成员函数，也称成员方法，描述对象的行为
#     def get_arae(self):#成员函数自带一个参数self
#         return self.length*self.wild
# r = Rectangle()
# r.length = 50
# r.wild = 10
# # ret = r.get_arae()
# # print(ret)
# print(r.get_arae())
class Fraction:
    def __init__(self, s, m):
        self.m, self.s = m, s

    def set_info(self, s, m):
        self.m, self.s = m, s

    def show(self):
        print("{}/{}".format(self.s, self.m))

    def reduce(self):
        # 先求出最大公约数
        sign = 1
        if self.s * self.m < 0:
            sign = -1           # 结果是负数
        self.s = abs(self.s)
        self.m = abs(self.m)    # 全都变成绝对值

        _min = min(self.s, self.m)
        while True:
            if self.s % _min == 0 and self.m % _min == 0:
                break
            else:
                _min -= 1
        self.s //= _min * sign   # 最后将符号给分子
        self.m //= _min


f = Fraction(4, -8)
f.reduce()
f.show()