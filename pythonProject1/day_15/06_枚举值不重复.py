from enum import IntEnum, unique


# IntEnum: 要求没个枚举值的值，都是int类
# unique: 枚举值不能重复

@unique
class IphoneType(IntEnum):
    IPHONE = 0
    IPHOEN3 = 1
    IPHOEN4 = 2
    IPHOEN5 = 3
    IPHOEN5S = 4
    IPHOEN6 = 5
    IPHONE7 = 6
    IPHONE8 = 7

    # 传入若干个版本，返回一个最新的
    @staticmethod
    def get_news(t, *args):
        m = t
        for i in args:
            if i.value > m.value:
                m = i
        return m

print(IphoneType.get_news(IphoneType.IPHONE7, IphoneType.IPHOEN5S, IphoneType.IPHOEN4))