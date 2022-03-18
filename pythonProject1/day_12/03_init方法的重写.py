class Parent:
    def __init__(self, name, age):
        self.__name, self.__age = name, age

    def __repr__(self):
        return "姓名：{}\n年龄：{}\n".format(self.__name, self.__age)


class Child(Parent):
    def __init__(self, name, age, height, weight):
        super().__init__(name, age)
        self.__height, self.__weight = height, weight

    def __repr__(self):
        return super().__repr__() + "身高：{}\n体重：{}\n".format(self.__height, self.__weight)


child = Child("子类", 14, 144, 21)
print(child.__repr__())
