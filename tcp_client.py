"""
TCP套接字编程
重点代码~~~~~!
"""
from socket import *

# 服务器地址
ADDR = ("127.0.0.1",55555)

# 使用默认值套接字
tcp_socket = socket()

# 发起连接
# tcp_socket.connect((""))
tcp_socket.connect(ADDR)

# 发送接收消息
while True:
    msg = input(">>")
    tcp_socket.send(msg.encode())
    if msg=="##":
        break
    data = tcp_socket.recv(1024)
    print("From server:",data.decode())
tcp_socket.close()
