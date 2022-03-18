import socket

# 服务端
# 配置套接字，首先设置传输方式TCP，然后绑定IP和端口号
# AF_INET为IPV4，AF_INET6为IPV6
# SOCK_STREAM为TCP协议，SOCK_DGRAM为UDP协议

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("192.168.60.1", 8923))


server_socket.listen(3) # 参数为最大并发数


while True:
    # 建立连接，返回客户端的IP和端口
    ip, address = server_socket.accept()
    # 接收不能超过4096，一般是二的倍数，不是二的倍数会出现中文乱码
    data = ip.recv(1024)
    print(data.decode("utf-8"))
    ip.send("good morning".encode("utf-8"))