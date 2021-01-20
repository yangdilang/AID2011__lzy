"""
基于多进程的网络并发模型
重点代码 ！！

创建tcp套接字
等待客户端连接
有客户端连接，则创建新的进程具体处理客户端请求
父进程继续等待处理其他客户端连接
如果客户端退出，则销毁对应的进程
"""
from socket import *
from multiprocessing import Process
import sys

# 地址变量
HOST = "0.0.0.0"
PORT = 8888
ADDR = (HOST, PORT)

# 服务入口函数
def main(func=None):
    # 创建tcp套接字
    tcp_socket = socket()
    tcp_socket.bind(ADDR)
    tcp_socket.listen(5)
    print("Listen the port %d"%PORT)

    # 循环连接客户端
    while True:
        try:
            connfd, addr = tcp_socket.accept()
            print("Connect from", addr)
        except KeyboardInterrupt:
            tcp_socket.close()
            sys.exit("服务结束")

        # 创建进程 处理客户端请求
        p = Process(target=func, args=(connfd,),daemon=True)
        p.start()

if __name__ == '__main__':
    # 处理客户端具体请求
    def handle(connfd):
        while True:
            data = connfd.recv(1024)
            if not data:
                break
            print(data.decode())
        connfd.close()

    main(handle)
