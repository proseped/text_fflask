import socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

client_socket.sendto("太阳当空照".encode("utf-8"), ("192.168.60.1", 8923))

# 接收回执
data, addr = client_socket.recvfrom(1024)
print(data.decode("utf-8"))