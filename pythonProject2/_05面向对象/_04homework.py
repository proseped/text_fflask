# 作业：
# 1.设计一个圆的类，通过构造方法初始化半径。包含方法：
# 修改半径：
# 返回周长：
# 返回面积：
class cicle():
    r = 0.0

    def __init__(self, r):
        self.r = r

    def get_cicle(self):
        return 3.14 *self.r**2, 2*3.14*self.r

    def chang_r(self,r):
        self.r = r


ret = cicle(2)
print(ret.get_cicle())
ret.chang_r(4)
print(ret.get_cicle())
# 2.设计一个分数的类，包含属性：
# 分子
# 分母
# 包含方法：
# 修改分子和分母
# 按照 分子/分母 方式输出
# 约分
class point():
    sun, mon = 0.0,0.0

    def __init__(self,sun, mon):
        self.sun, self.mon = sun, mon

    def change(self,sun, mon):
        self.sun, self.mon = sun, mon

    def get_count(self):
        return self.sun/self.mon

    def reduce(self):
        _min = min(self.sun, self.mon)
        while True:
            if self.sun % _min == 0 and self.mon % _min == 0:
                break
            else:
                _min -= 1
        self.sun //= _min
        self.mon //= _min
p = point(6,4)
print(p.get_count())
# 3.设计一个账户信息的类
# 包含属性：
# 用户名
# 密码
# 昵称
# 注册时间：
# 最后访问时间：
# 包含方法：
# 访问（修改最后访问时间）
# 修改密码(要求传入旧密码和新密码，旧密码正确才能修改)
# 打印账户信息
# 4.设置矩形类，包含长和宽
# 方法：
# 返回面积
# 返回周长
