# 创建一个圆的类，用init设置半径，set可以修改半径，求其表面积和周长
class cicle():
    r = 0.0

    def __init__(self, r):
        self.r = r

    def get_cicle(self):
        return 3.14 *self.r**2, 2*3.14*self.r

    def chang_r(self,r):
        self.r = r


ret = cicle(2)
print(ret.get_cicle())
ret.chang_r(4)
print(ret.get_cicle())