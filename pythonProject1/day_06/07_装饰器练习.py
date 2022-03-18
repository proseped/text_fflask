# 装饰器练习
# 打印一个装饰器，在一个函数执行之前，打印这个函数将要执行，函数执行之后，打印这个函数。
# 计算打印完毕时间
import datetime
import time


def run_time(fanction):
    def do_run_time(*a, **b):
        nonlocal fanction
        print("函数将要执行")
        ret = fanction(*a, **b)
        print("函数执行完毕", datetime.datetime.now())
        return ret

    return do_run_time()


@run_time
def print_helloworld():
    print("helloworld!")


print_helloworld()
