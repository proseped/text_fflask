# 1.	创建四种车子分别是卡车，轿车，跑车，三轮车
# 公共的部分：
# 属性：
# 座位数，加速度，刹车距

# 卡车：
# 载重量
# 轿车：
# 四驱否（bool）
# 跑车：
# 四驱否（bool），敞篷否（bool）
# 三轮车：
# 踏板阻尼

# 方法：（print）
# 启动，加速，停车，减速，刹车
# 卡车:翻斗
# 跑车:敞篷
#   三轮车:脚刹
class Father:

    def __init__(self, t, a, s):
        self.__t = t
        self.__a = a
        self.__s = s

    def __repr__(self):
        return "座位数：{}加速度：{}刹车距：{}".format(self.__t, self.__a, self.__s)

    def table(self, t):
        self.__t = t

    def agret(self, a):
        self.__a = a

    def long(self, s):
        self.__s = s


# 卡车：
# 载重量
class A(Father):
    def weight(self,t,a,s, w):
        self.__w = w
        self.__t = t
        self.__a = a
        self.__s = s
    super().__init__(35,34,55,)

# 轿车：
# 四驱否（bool）
class B(Father):
    @staticmethod
    def is_four():
        i = int(input("是否为四驱："))

        bool(i)

# 跑车：
# 四驱否（bool），敞篷否（bool）
class C(Father, B):
    super()


# 三轮车：
# 踏板阻尼
class D(Father):
    @staticmethod
    def is_foot():
        i = int(input("是否阻尼："))
        if i == "是":
            i = 1
        if i == "否":
            i = 0
        bool(i)


# 方法：（print）
# 启动，加速，停车，减速，刹车
# 卡车:翻斗
# 跑车:敞篷
#   三轮车:脚刹
a = A(45,34,546)
print(a.__repr__())
b = B(43,5,4)
b.is_four()