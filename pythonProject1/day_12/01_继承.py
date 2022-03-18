# 子类可以获得父类的字段和方法
# 子类可以拥有自己的字段和方法，称之为派生
class Parent:
    def __init__(self):
        self.a, self.b, self.__c = 0, 0, 0
    @property
    def c(self):
        return self.__c

    @c.setter
    def c(self, c):
        self.__c = c

    def print(self):
        print(self.a, self.b, self.c)

class Child(Parent):
    def print_helloworld(self):
        return "helloworld"


chr = Child()
chr.a = 41
chr.c = 45
print(chr.print_helloworld())
chr.print()