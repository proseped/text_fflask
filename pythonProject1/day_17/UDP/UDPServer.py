import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(("192.168.60.1", 8923))
while True:
    data , addr = server_socket.recvfrom(1024)
    data = data.decode("utf-8")
    print(data)
    server_socket.sendto("你发的【{}】我收到了".format(data).encode("utf-8"), addr)