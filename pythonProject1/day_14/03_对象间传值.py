class Son:
    def __init__(self, name):
        self.__name = name
        self.__money = 0

    def show_money(self):
        print("%s:%d" % (self.__name, self.__money))

    def rise_money(self, num):
        self.__money += num


class Father:
    def __init__(self, name):
        self.__name = name
        self.__money = 1000000

    def show_money(self):
        print("%s:%d" % (self.__name, self.__money))

    def sent_money(self, son: Son):     # 郭麒麟为郭德纲的代理
        self.__money -= 100000          # 也称之为郭德纲【委托】郭麒麟的增长
        son.rise_money(100000)


f = Father("郭德纲")
s = Son("郭麒麟")
f.show_money()
s.show_money()

f.sent_money(s)
f.show_money()
s.show_money()