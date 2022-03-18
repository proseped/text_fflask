# 线程是一种工具类，是CPU同一时间完成多个任务的一种手段
# 程序默认拥有一个线程，我们称之为主线程，占用主线程执行的任务，称为同步任务，不占用主线程，
# 即开辟一个新线程子线程执行的任务，称为异步任务。
import threading
import time


# 自定义一个类，来继承官方类
class MyThreading(threading.Thread):
    # 将子线程执行的任务，写在run函数中
    def run(self):
        for i in range(10):
            print("hello world!")
            time.sleep(1)


thread = MyThreading()
thread.start()

for i in range(10):
    print("Good morning")
    time.sleep(0.8)
