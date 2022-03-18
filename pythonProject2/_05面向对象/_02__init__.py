class Class01:
    longth, width, heigth = 0.0, 0.0 ,0.0

    def __init__(self,longth, width, heigth):   # 写init方法后调用类时必须传入参数
        self.longth,self.width,self.heigth = longth, width,heigth

    def get_area(self):
        return (self.longth + self.width)*self.heigth/2

    def change_line(self, longth, width, heigth):
        self.longth, self.width, self.heigth = longth,width,heigth


r = Class01(2,3,4)
print(r.get_area())
r.change_line(3,4,5)
print(r.get_area())
# r.change_line(2,3,4)
# print(r.get_area())