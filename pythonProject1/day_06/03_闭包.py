# 闭包函数外面声明的变量，不能使用在函数里面，只能通过传参进来。
# 闭包函数里面的变量，不能在外面使用，有自己的作用域。
# if，for，while等流程控制语句没有自己的作用域。
# 闭包函数只能在声明所在的函数中调用。

def print_helo():
    print("hello")
    def print_world():
        print("world")
    print_world()
print_helo()