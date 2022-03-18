import request
import re
# 下载并解析存储电影信息的类


class MovieInfoManager(request.RequestDelegate):
    def __init__(self):
        self.__request = request.Request(self)

    # 下载数据
    def download(self, url):
        self.__request.request(url)

    # 重写方法接收数据
    def receive_data(self, data):
        self.analyze_data(data)

    # 解析hrml文件
    def analyze_data(self,data):
        pattern = '"name":(.*)"director":'
        ret = re.search(pattern, data, re.S)
        pattern = '"(.*)",.*"url"'
        ret = re.search(pattern, ret.group(1), re.S)
        print(ret)


nin = MovieInfoManager()
nin.download("https://movie.douban.com/subject/1794171/")