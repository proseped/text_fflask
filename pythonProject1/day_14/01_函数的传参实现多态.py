import random


class Stu:
    def __init__(self, name, age, score, height):
        self.__name, self.__age, self.__score, self.__height = name, age, score, height

    @property   # 私有变量，要有属性调用
    def age(self):
        return self.__age

    @property
    def score(self):
        return self.__score

    @property
    def height(self):
        return self.__height

    def __repr__(self):
        return "【姓名：{}年龄：{}成绩：{} 身高：{}】".format(self.__name, self.__age, self.__score, self.__height)


ls = []
names = ["张三", "李四", "王五", "赵六"]
for name in names:
    ls.append(Stu(name, random.randint(10, 14), random.randint(0, 100), random.randint(100, 200)))

print(ls)


def sort(ls, function):
    # 根据年龄从小到大排序
    for i in range(0, len(ls) - 1):
        for j in range(0, len(ls) - 1 - i):
            if function(ls[j], ls[j + 1]):  # 调用older_than,使用older_than方法。stu1,stu2 = ls[j],ls[j+1]
                ls[j], ls[j + 1] = ls[j + 1], ls[j]


# 传入两个参数，左边大于右边
def older_than(stu1, stu2):
    return stu1.age > stu2.age


def younger_than(stu1, stu2):
    return stu1.age < stu2.age


def score_worse(stu1, stu2):
    return stu1.score < stu2.score


def shorter_than(stu1, stu2):
    return stu1.height < stu2.height


sort(ls, older_than)
print(ls)
sort(ls, younger_than)
print(ls)
sort(ls, score_worse)
print(ls)
sort(ls, shorter_than)
print(ls)