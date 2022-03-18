import socket
from user_manager import UserManager

server_addr = ("192.168.60.1", 8080)


class MyChatServer:
    def __init__(self):
        self.__socket = self.init_socket()  # 配置socket
        self.__user_manager = UserManager

    @staticmethod
    def init_socket():
        global server_addr
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.bind(server_addr)
        return s

    # 启动函数
    def start(self):
        self.run()

    # 监听客户端发来的请求
    def run(self):
        while True:
            data, addr = self.__socket.recvfrom(1024)
            # 根据客户端发来的数据不同，做不同的处理
            self.respond_request(data.decode("utf-8"), addr)

    def respond_request(self, data, addr):
        # 登录请求<[LOGIN]>|username
        ctl = data.split("|")[0]
        ctl_dict = {
            '<[LOGIN]>': MyChatServer.client_login
        }
        ctl_dict[ctl](self, data, addr)

    def client_login(self, data, addr):
        username = data[10:]
        ret = self.__user_manager.login_user(username)
        if ret:
            print("【{}】登录成功".format(username))
            content = "<[LOGIN_SUCCESS]>"
            self.__socket.sendto(content.encode("utf-8"), addr)
        else:
            print("【{}】登录失败".format(username))
            content = "<[LOGIN_FAILED]>"
            self.__socket.sendto(content.encode("utf-8"), addr)


chat_server = MyChatServer()
chat_server.start()







