# 创建一个长方体的类，包括长宽高。编写成员函数，返回长方体的表面积、体积。
class Rectangle:

    def __init__(self, length, wild, height):
        self.length, self.wild, self.height = length, wild, height

    def get_area_volume(self):
        return [(self.height * self.length + self.height * self.wild + self.wild * self.length) * 2,
                self.height * self.height * self.wild]


t = Rectangle(3, 4, 5)
# print("面积，体积",t.get_area_volume())
print(t.get_area_volume())
