# 1.歌词解析器，写一个歌词解析器，能解析网络下载的lrc文件，根据输入的秒数，返回对应的歌词。
# 比如“啦啦啦”对应的秒数是5秒，“呵呵呵”对应的秒数是8秒。要求输入5， 6， 7都是显示“啦啦啦”


# 2.编写地铁线路
# 站类：属性 站名
# 线类：属性 列表（管理一条线上的所有站）
# 	方法：添加站（插入添加）
# 地铁线路类:属性
# 	方法: 添加站(站名，线路名，线路上位置名)
# 		 打印一条线路上的所有站
# 		 判断两条线路是否能转乘(传两个线路号)
class Station:
    def __init__(self, name):
        self.__name = name

    @property
    def get_name(self):
        return self.__name

    @get_name.setter
    def get_name(self, name):
        self.__name = name


class Line:
    def __init__(self, name):
        self.__list = []
        self.__name = name

    @property
    def name(self):
        return self.__name

    # 添加站
    def add(self, index, name):
        self.__list.insert(index, Station(name))

    # 地铁线路类
    # 方法: 添加站(站名，线路名，线路上位置名)
    # 		 打印一条线路上的所有站
    # 		 判断两条线路是否能转乘(传两个线路号)

class Lines:
    def __init__(self):
        self.__list = []

    def add(self, station_name, line_name, index):
        for i in self.__list:
            if i.name == line_name:
                i.add(index, station_name)
                return













