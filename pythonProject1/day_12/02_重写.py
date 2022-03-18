# 可以通过super()函数，重写父类同名方法，完成一部分操作。
class Parent:
    def get(self, a, b):
        print("周长：{} ，面积：{}".format(4 * a, a * a))


class Child(Parent):

    def get(self, a, b):
        return "周长：{} ，面积：{}".format(b * a * 2, b * a)


s = Parent()
s.get(1, 5)
r = Child()
print(r.get(4, 2))
