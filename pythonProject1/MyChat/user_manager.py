class User:
    def __init__(self, username):
        self.__username = username

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, v):
        self.__username = v


class UserManager:
    def __init__(self):
        self.__user_list = []

    # 查找函数
    def __find_user(self, name):
        for i in self.__user_list:
            if i.username == name:
                return i
        return None

    # 一个用户登录上线
    def login_user(self, username):
        user = self.__find_user(username)
        if user:
            return False
        user = User(username)
        self.__user_list.append(user)
        return True



