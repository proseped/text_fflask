import datetime
import time


def print_num():
    for i in range(1,101):
        time.sleep(0.1)
        print(i)


def count_time():
    def do_count_time(f):
        time = datetime.datetime.now()
        f()
        time2 = datetime.datetime.now()
        return (time2-time).total_seconds()
    return do_count_time   # 相当于返回给count time 然后赋值给x 打印出来

x = count_time()
print(x(print_num))

