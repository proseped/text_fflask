class Father:
    def __init__(self, a):
        self.__a = a
        self.__b = a ** 2
        self.x = 10

    def show(self):
        print("Father", self.__a, self.__b)


class Mother:
    def __init__(self, b, c):
        self.__b = b
        self.__c = c
        self.x = 11

    def show(self):
        print("Mother", self.__b, self.__c)


class Child(Father, Mother):
    def __init__(self, a, b, c):
        # 私有变量，即使名字相同，继承了，也是两个变量
        Father.__init__(self, a)
        Mother.__init__(self, b, c)

# 对于子类可以访问的变量，公有变量和保护变量，多个父类同名，在子类中是同一个变量。
# 谁最后初始化，变量就等于初始化后类的值。

    def shwo_x(self):
        print(self.x)


c = Child(1, 2, 3)
c.show()
Mother.show(c)
c.shwo_x()