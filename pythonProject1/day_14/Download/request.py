import threading
import time
import random


# 所有接收数据类的父类

class RequestDelegate:
    # 子类必须继承该类，重写下面方法
    def receive_data(self, data): pass


class Request(threading.Thread):
    def __init__(self):
        super().__init__()
        self.__delegate = None

    def request_data(self, delegate: RequestDelegate):
        self.start()
        self.__delegate = delegate

    def run(self):
        for i in range(random.randint(15, 30)):
            time.sleep(1)
            print("下载中")
        data = "我是要下载的数据"
        self.__delegate.receive_data(data)
