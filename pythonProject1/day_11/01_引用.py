class Rect:
    def __init__(self):
        self.length, self.width = 1, 2


# 引用装了对象的地址，对象装了内存空间的门牌号

r1 = Rect()
# r1不是对象，但可以通过r1，可以找到对象，可以使用/访问对象。
r1.length = 5
r2 = r1 # 存了同一个内存地址
print(r2.length)
r2.length = 10
print(r1.length)
