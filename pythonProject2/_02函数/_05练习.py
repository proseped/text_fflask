import datetime


def run_time(function):
    def do_run_time(*a, **b):
        nonlocal function
        print("函数将要执行")
        ret = function(*a, **b)
        print("函数执行时间：", datetime.datetime.now())
        return ret
    return do_run_time


@run_time
def print_anything():
    print("hello world")

print_anything()