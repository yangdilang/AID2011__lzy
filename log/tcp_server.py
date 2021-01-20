"""
TCP服务端函数示例
重点代码~~~~~!
"""
from socket import *

# tcp创建套接字
tcp_socket = socket(AF_INET,SOCK_STREAM)

#绑定地址
tcp_socket.bind(("0.0.0.0",55555))

# 设置为监听套接字
tcp_socket.listen(6)

# 等待客户端连接
while True:
    print("Waiting for connect...")
    connfd,addr = tcp_socket.accept()
    print("Connect from",addr)

    # 收发消息
    while True:
        data = connfd.recv(1024)
        if data==b"##":
            break
        print("收到:",addr,data.decode())
        connfd.send(b"Thanks")

    # 关闭套接字

    connfd.close()
tcp_socket.close()
