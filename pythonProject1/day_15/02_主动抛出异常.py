class Fraction:
    def __init__(self, devised, devision):
        if devision == 0:
            raise ZeroDivisionError
        self.__devised, self.__devision = devised, devision

    def print(self):
        print("{}/{}".format(self.__devised, self.__devision))

    def to_float(self):
        return self.__devised / self.__devision

while True:
    try:
        devised, devision = int(input()), int(input())
        f = Fraction(devised, devision)
        break                                           # 当分母为零时，抛出异常，不执行异常下面代码，直接except
    except ZeroDivisionError:
        print("输入错误，请重试！")


print(f.to_float())
f.print()
