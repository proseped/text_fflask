import datetime
import time



def count_time(function):
    def do_count_time(*a, **b):
        nonlocal function
        time = datetime.datetime.now()
        ret = function(*a, *b)
        time1 = datetime.datetime.now()
        print("执行时间",(time1-time).total_seconds())
        return ret
    return do_count_time


@count_time
def print_anything(s: str, times: int):
    for i in range(times):
        print(s)
        time.sleep(0.1)

print_anything("1234",4)