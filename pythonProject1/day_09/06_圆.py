# 创建一个圆的类，拥有字段半径，通过set修改半径，计算圆的面积和周长。
import math


class Circle:

    def __init__(self, r):
        self.r = r

    def get_area(self):
        return math.pi*self.r**2

    def get_long(self):
        return math.pi*2*self.r

    def set_r(self, r):
        self.r = r


t = Circle(2)

print("面积：", t.get_area())
print("周长：", t.get_long())
t.set_r(3)
print("面积：", t.get_area())
print("周长：", t.get_long())
