# UrlItem 书签类
# 属性： 标题 网址 星级 访问次数
# 方法： 修改标题 网址 星级
# 返回： 标题 网址 星级

# UrlManager 储存书签
# 属性：通过一个列表，存储并修改大量书签
# 方法：添加书签 删除书签（通过标题，网址）
# 修改书签的标题（通过旧书签）
# 修改书签的网址
# 修改书签的星级
# 通过访问次数排序书签后输出
# 通过星级个数排序书签后输出

class URLItem:
    def __init__(self, title, url, stars):
        self.__title, self.__url, self.__stars, self.__visits = title, url, stars, 0

    def set_title(self, title):
        self.__title = title

    def set_url(self, url):
        self.__url = url

    def set_stars(self, stars):
        if stars < 1:
            self.__stars = 1
        elif stars > 5:
            self.__stars = 5
        else:
            self.__stars = stars

    def get_title(self):
        return self.__title

    def get_url(self):
        return self.__url

    def get_stars(self):
        return self.__stars

    def show(self):
        print("".center(30, "="))
        print("标题:{}\n网址:{}\n星级:{}\n访问次数:{}".format(self.__title, self.__url, self.__stars, self.__visits))
        print("".center(30, "="))


# UrLManager:储存并管理大量的书签


class URLManager:
    def __init__(self):
        self.__list = []  # 创建一个收藏夹的同时创建list

    # 在列表中查找这个标题的书签
    def __find_urlitem(self, title):
        for i in self.__list:
            if i.get_title() == title:
                return i
        return None

    # 添加书签
    def add_url(self, title: str, url: str, stars: int):
        # 先去找，列表里有没有这个书签
        item = self.__find_urlitem(title)
        if item:  # 返回一个对象，所有对象都是真，只有None是假
            print("标题为{}的书签已存在，添加失败".format(title))
            return

        item = URLItem(title, url, stars)  # 创建书签
        self.__list.append(item)  # 添加到列表
        print("书签{}已添加成功".format(title))

    # 删除书签（通过标题，网址）

    # 通过标题

    def remove_url(self, title):
        item = self.__find_urlitem(title)
        if not item:
            print("标签{}不存在，删除失败".format(title))
            return
        self.__list.remove(item)
        print("书签{}已删除".format(title))

    def remove_urlitem_url(self, url):
        is_exite = False
        for i in self.__list:
            if i.get_url() == url:
                self.__list.remove(i)
                print("书签{}已删除".format(i.get_url()))
                is_exite = True
            if is_exite:
                print("网址为{}的书签均已删除".format(url))
            else:
                print("网址为{}的书签不存在，删除失败".format(url))

    # 修改书签的标题（通过旧书签）

    def change_URLItem_title(self, title, new_url):
        item = self.__find_urlitem(title)
        if not item:
            print("标签{}不存在，修改失败".format(title))
        item.set_url(new_url)
        print("标题{}已修改为{}".format(title, new_url))

    # 修改书签的网址
    def change_url(self, title, new_url):
        item = self.__find_urlitem(title)
        if not item:
            print("标题为{}不存在，修改失败".format(title))
            return
        item.set_url(new_url)
        print("标题{}的网址已修改为{}".format(title, new_url))

        # 修改书签的星级

    def change_urlitem_stars(self, title, new_stars):
        item = self.__find_urlitem(title)
        if not item:
            print("标题为{}不存在，修改失败".format(title))
            return
        item.set_stars(new_stars)
        print("标题{}的星级已修改为{}".format(title, new_stars))

    # 将所有书签按照访问次数排序后输出
    def show_urlitem_visits(self):
        # 冒泡排序法
        for i in range(0, len(self.__list) - 1):
            for j in range(0, len(self.__list) - i - 1):
                if self.__list[j + 1].get_visit() > self.__list[j].get_visit():
                    self.__list[j], self.__list[j + 1] = self.__list[j + 1], self.__list[j]
        for i in self.__list:
            print(i)

    # 将所有书签按照星级排序后输出
    def show_urlitems_stars(self):
        # 选择排序法
        for i in range(0, len(self.__list) - 1):
            for j in range(i + 1, len(self.__list)):
                if self.__list[i].get_stars() < self.__list[j].get_stars():
                    self.__list[j], self.__list[i] = self.__list[i], self.__list[j]

        for i in self.__list:
            i.show()


u = URLManager()
u.add_url("哔哩哔哩", "www.bilibili.com", 5)
u.add_url("百度", "www.baidu.com", 3)
u.remove_url("百度")
u.remove_url("百度")
u.add_url("百度", "www.baidu.com", 3)
u.add_url("百度", "www.baidu.com", 4)
u.add_url("新浪", "www.sina.com", 3)
u.add_url("雅虎", "www.yahoo.com", 2)

u.change_urlitem_stars("雅虎", 4)
u.change_urlitem_stars("新浪", 3)

u.change_URLItem_title("雅虎", "Yahoo!!")

u.show_urlitems_stars()
