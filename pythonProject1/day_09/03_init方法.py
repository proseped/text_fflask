class Trapezoid:
    # top, bottom, height = 0.0, 0.0, 0.0,init会自动添加

    def __init__(self, top, bottom, height,):
        self.top, self.bottom, self.height = top, bottom, height

    def get_area(self):
        return (self.top + self.bottom) * self.height / 2

    def set_top_bottom_height(self, top, bottom, height):
        self.top, self.bottom, self.height = top, bottom, height


t = Trapezoid(4, 5, 6)  # 有init必须传参
print(t.get_area())

t.set_top_bottom_height(5, 6, 7)
print(t.get_area())
