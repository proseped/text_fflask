from request import Request
from request import RequestDelegate
import time


class DataManager(RequestDelegate):
    def __init__(self):
        self.__request = Request()

    def download_data(self):
        self.__request.request_data(self)

    def receive_data(self, data):   # 回调函数
        print("收到数据", data)
        print("解析数据！！")


datamanager = DataManager()
datamanager.download_data()

while True:
    time.sleep(0.8)
    print("主线程工作中...")
