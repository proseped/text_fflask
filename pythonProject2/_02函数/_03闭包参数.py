import datetime
import time


def print_anything(s: str, times: int):
    for i in range(times):
        print(s)
        time.sleep(0.1)


def count_time(function, *a, **b):
    def do_count_time():
        nonlocal function, a, b
        time = datetime.datetime.now()
        function(*a, *b)
        time1 = datetime.datetime.now()
        return (time1-time).total_seconds()
    return do_count_time


x = count_time(print_anything, "hello world", 3)
t =x()  # 注意此处的括号， 调用函数  count_time(参数)()
print(t)