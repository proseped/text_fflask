# 写一个发报机，有一个函数，参数是发送的报文str，将报文发送给任意对象
class Everything:
    def recive_paper(self, date):
        pass


class Father:
    def __init__(self, name):
        self.__name = name

    def sent_paper(self, message, thing: Everything):
        thing.recive_paper(message)

    def show_thing(self):
        print(self.__name)


class Son(Everything):
    def __init__(self, name):
        self.__name = name

    def recive_paper(self, date):
        for i in range(3):
            print(date)

    def show_thing(self):
        print(self.__name)


f = Father("传送方")
s = Son("接收方")
f.sent_paper("haha", s)
f.show_thing()
s.show_thing()
