class Everyone:
    def recive_money(self):     # 继承实现了统一接口，实现了多态的作用
        return 0


class Father:
    def __init__(self, name):
        self.__name = name
        self.__money = 10000000

    def show_money(self):
        print("%s:%d" % (self.__name, self.__money))

    def sent_money(self, one: Everyone):     # 郭麒麟为郭德纲的代理
        ret = one.recive_money()
        self.__money -= ret                  # 也称之为郭德纲【委托】郭麒麟的增长


class Son(Everyone):
    def __init__(self, name):
        self.__name = name
        self.__money = 0

    def show_money(self):
        print("%s:%d" % (self.__name, self.__money))

    def recive_money(self):
        self.__money += 50000
        return 50000


class Stu(Everyone):
    def __init__(self, name):
        self.__name = name
        self.__money = 0

    def show_money(self):
        print("%s:%d" % (self.__name, self.__money))

    def recive_money(self):
        self.__money += 100000
        return 100000


f = Father("郭德纲")
s = Son("郭麒麟")
f.sent_money(s)
s.show_money()
f.show_money()

r = Stu("岳云鹏")
f.sent_money(r)
f.show_money()
r.show_money()
