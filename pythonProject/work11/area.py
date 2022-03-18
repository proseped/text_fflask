class Rectangle:
    def __init__(self):
        self.width = 0
        self.height = 0
    def set_size(self, size):
        self.width, self.height = size
    def get_size(self):
        return self.width, self.height
    #旧式getter/setter做法
    size = property(get_size, set_size)

    #标注改写的getter/setter
    @property
    def edges(self):
        return self.width, self.height

    @edges.setter
    def edges(self, values):
        self.width, self.height = values

    @edges.deleter
    def edges(self):
        del self.width, self.height

    #另一个演示仅有getter
    @property
    def area(self):
        return self.width * self.height
r = Rectangle()
r.width = 10
r.height = 5
print(r.size)
r.size = 150, 100
print(r.width)
print(r.area)

r.edges = 5, 8
print(r.size)
print(r.edges)

#del r.edges
print(r.edges)
