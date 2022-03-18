class Cube:
    def __init__(self, l, w):
        self.__l, self.__w = l, w
    @property
    def get_w(self):
        return self.__w

    @get_w.setter
    def get_w(self,w):
        self.__w = w

r = Cube(1,2)
print(r.get_w)
r.get_w = 10
print(r.get_w)
