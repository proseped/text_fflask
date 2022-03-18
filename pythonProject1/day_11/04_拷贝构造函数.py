class Rect:
    def __init__(self, length, width):
        self.__length, self.__width = length, width

    def set_length_width(self, l, w):
        self.__length, self.__width = l, w

    def __repr__(self):
        return "（{}:{}）".format(self.__length, self.__width)

    def copy(self):
        return Rect(self.__length, self.__width)


r1 = Rect(3, 4)
r2 = r1.copy()
print(r2)
r2.set_length_width(5,6)
print(r1,r2)