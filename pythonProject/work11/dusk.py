class Book ():
    def __init__(self, bname, isbn):
        self.bname = bname
        self.isbn = isbn

    def showInfo(self):
        print ( '此书' + self.bname, ',书号' + self.isbn )


class Car ():
    def __init__(self, brand, licence):
        self.brand = brand
        self.licence = licence

    def showInfo(self):
        print ( '此车' + self.brand, ',车牌' + self.licence )


class Person ():
    def __init__(self, idno):
        self.idno = idno

    def showInfo(self):
        print ( '此人身份证号' + self.idno )


staff = [ Book ( 'Python程序设计', '97875566' ), Car ( '别克', '鄂EV8858' ), Person ( '4205035558888' ) ];
for x in staff:
    x.showInfo ()