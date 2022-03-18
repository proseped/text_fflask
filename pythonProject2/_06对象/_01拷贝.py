class Rect:
    def __init__(self, length, width):
        self.length, self.width = length, width

    def change(self, l, w):
        self.length, self.width = l, w

    def __repr__(self):
        return "({}:{})".format(self.length, self.width)

    def __copy__(self):
        return Rect(self.length, self.width)


# r1 = Rect(3, 4)
# r2 = r1.__copy__()
# print(r2)
# r2.change(5, 6)4
# print(r1, r2)

ls = [Rect(1, 2), Rect(3, 4), Rect(5, 6)]
ls2 = ls
ls2[0].change(-1, -1)
print(ls, ls2)

ls3 = ls.copy()
ls3[0].change(0, 0)
print(ls, ls3)

ls4 = [1, 2, 3, 4, [5, 6]]
ls5 = ls4.copy()
ls5[0] = -1                # ls4[0]是个值，复制了就和他没用关系了
ls5[4][0] = 0              # ls4[4][0]是个引用，复制了后是同一个对象的两个引用
print(ls4)
print(ls5)