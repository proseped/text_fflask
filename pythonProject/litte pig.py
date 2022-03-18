from distutils.core import setup
from turtle import *


def nose():  # 鼻子
    penup()
    goto(-100, 100)
    setheading(-30)
    color((255, 155, 192), "pink")  # 画笔色是浅粉，填充色是粉色
    pendown()
    begin_fill()
    # 绘制一个椭圆作为鼻子的轮廓
    segment = 0.4
    for i in range(120):
        if 0 <= i < 30 or 60 <= i < 90:
            segment = segment + 0.08
            left(3)
            forward(segment)
        else:
            segment = segment - 0.08
            left(3)
            forward(segment)
    end_fill()
    # 左鼻孔
    penup()
    setheading(90)
    forward(25)
    setheading(0)
    forward(10)
    color((255, 155, 192), (160, 82, 45))  # 画笔色是浅粉，填充色是黄土赭色
    pendown()
    begin_fill()
    circle(5)
    end_fill()
    # 右鼻孔
    penup()
    setheading(0)
    forward(20)
    pendown()
    begin_fill()
    circle(5)
    end_fill()


def head():  # 头
    penup()
    goto(-69, 167)
    pendown()
    color((255, 155, 192), "black")
    begin_fill()
    setheading(180)
    circle(300, -30)
    circle(100, -60)
    circle(80, -100)
    circle(150, -20)
    circle(60, -95)
    setheading(161)
    circle(-300, 15)

    # 勾画出右半个鼻子的轮廓，避免填充时覆盖掉
    penup()
    goto(-100, 100)
    pendown()
    setheading(-30)
    segment = 0.4
    for i in range(60):
        if 0 <= i < 30 or 60 <= i < 90:
            segment = segment + 0.08
            left(3)
            forward(segment)
        else:
            segment = segment - 0.08
            left(3)
            forward(segment)
    end_fill()


def ears():  # 耳朵
    color((255, 155, 192), "black")
    # 左耳朵
    penup()
    goto(0, 160)
    pendown()
    begin_fill()
    setheading(100)
    circle(-50, 50)
    circle(-10, 120)
    circle(-50, 54)
    end_fill()
    # 右耳朵
    penup()
    setheading(90)
    forward(-12)
    setheading(0)
    forward(30)
    pendown()
    begin_fill()
    setheading(100)
    circle(-50, 50)
    circle(-10, 120)
    circle(-50, 56)
    end_fill()


def eyes():  # 眼睛
    # 左眼框
    color((255, 155, 192), "white")
    penup()
    setheading(90)
    forward(-20)
    setheading(0)
    forward(-95)
    pendown()
    begin_fill()
    circle(15)
    end_fill()
    # 左眼珠
    color("black")
    penup()
    setheading(90)
    forward(12)
    setheading(0)
    forward(-3)
    pendown()
    begin_fill()
    circle(3)
    end_fill()
    # 右眼框
    color((255, 155, 192), "white")
    penup()
    setheading(90)
    forward(-25)
    setheading(0)
    forward(40)
    pendown()
    begin_fill()
    circle(15)
    end_fill()
    # 右眼珠
    color("black")
    penup()
    setheading(90)
    forward(12)
    setheading(0)
    forward(-3)
    pendown()
    begin_fill()
    circle(3)
    end_fill()


def cheek():  # 腮
    penup()
    goto(80, 10)
    setheading(0)
    color((255, 155, 192))
    pendown()
    begin_fill()
    circle(30)
    end_fill()


def mouth():  # 嘴
    penup()
    goto(-20, 30)
    color(239, 69, 19)
    pendown()
    setheading(-80)
    circle(35, 120)


def body():  # 身体
    color("red", (255, 99, 71))
    # 身体左边的曲线
    penup()
    goto(-32, -8)
    pendown()
    begin_fill()
    setheading(-130)
    circle(100, 10)
    circle(300, 30)
    # 身体底边
    setheading(0)
    forward(230)
    # 身体右边的曲线
    setheading(90)
    circle(300, 30)
    circle(100, 3)
    color((255, 155, 192), (255, 100, 100))
    # 把脸上的下巴颏画出来，避免填充时覆盖掉
    setheading(-135)
    circle(-80, 63)
    circle(-150, 24)
    end_fill()


def hands():  # 手
    color((255, 155, 192))
    # 左手的中间手指
    penup()
    goto(-56, -45)
    pendown()
    setheading(-160)
    circle(300, 15)
    # 通过一个弧形表示另外两根手指
    penup()
    setheading(90)
    forward(15)
    setheading(0)
    pendown()
    setheading(-10)
    circle(-20, 90)
    # 右手的中间手指
    penup()
    setheading(90)
    forward(30)
    setheading(0)
    forward(237)
    pendown()
    setheading(-20)
    circle(-300, 15)
    # 通过一个弧形表示另外两根手指
    penup()
    setheading(90)
    forward(20)
    setheading(0)
    pendown()
    setheading(-170)
    circle(20, 90)


def feet():  # 腿和脚
    # 左腿
    pensize(10)
    color((240, 128, 128))
    penup()
    goto(2, -177)
    pendown()
    setheading(-90)
    forward(40)
    setheading(-180)
    # 左脚
    color("black")
    pensize(15)
    forward(20)
    # 右腿
    pensize(10)
    color((240, 128, 128))
    penup()
    setheading(90)
    forward(40)
    setheading(0)
    forward(90)
    pendown()
    setheading(-90)
    forward(40)
    setheading(-180)
    # 右脚
    color("black")
    pensize(15)
    forward(20)


def tail():  # 尾巴
    pensize(4)
    color((255, 155, 192))
    penup()
    goto(148, -155)
    pendown()
    setheading(0)
    # 打卷的尾巴
    circle(70, 20)
    circle(10, 330)
    circle(70, 30)


def setting():  # 参数设置
    # 设置窗口大小
    setup(800, 500)
    # 设置画笔
    pensize(4)
    hideturtle()
    colormode(255)
    speed(20)


setting()  # 画布、画笔设置
nose()  # 鼻子
head()  # 头
ears()  # 耳朵
eyes()  # 眼睛
cheek()  # 腮
mouth()  # 嘴
body()  # 身体
hands()  # 手
feet()  # 脚
tail()  # 尾巴