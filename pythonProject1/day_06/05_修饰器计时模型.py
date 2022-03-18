import datetime
import time


def print_anything(s: str, times: int):
    for i in range(times):
        print(s)
        time.sleep(0.1)


def count_time(function, *a, **b):  # *a,**b表示可以传入任何参数
    def do_count_time():
        nonlocal function, a, b
        time = datetime.datetime.now()
        ret = function(*a, **b)
        time2 = datetime.datetime.now()
        print("执行时间", (time2 - time).total_seconds())
        return ret

    return do_count_time()


print_anything("123", 4)
# count_time(print_anything("hello world",3))()
count_time(print_anything, "hello world", 3)


def add(a, b, c):
    return a + b + c


s = count_time(add, 1, 2, 3)
print(s)
