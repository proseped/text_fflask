import socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("192.168.60.1", 8923))
client_socket.send("hello world".encode("utf-8"))
data = client_socket.recv(1024)
print(data.decode("utf-8"))