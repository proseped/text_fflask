import socket


class MyChatClient:
    def __init__(self):
        self.__socket = self.init_socket()
        self.__server_addr = ("192.168.60.1", 8080)
        self.__username = "小科"

    @staticmethod
    def init_socket():
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        return s

    def start(self):
        self.login()

    def login(self):
        content = "<[LOGIN]>{}".format(self.__username)
        self.__socket.sendto(content.encode("utf-8"), self.__server_addr)

        # 接收回执
        data, addr = self.__socket.recvfrom(1024)
        data = data.decode("utf-8")
        if data == "<[LOGIN_SUCCESS]>":
            print("登录成功，您已上线！")
        else:
            print("登录失败！")


c = MyChatClient()
c.start()