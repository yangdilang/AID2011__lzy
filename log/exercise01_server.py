"""
练习 01 ：
在客户端将一张图片上传到服务端，图片自选
上传到服务端后命名为 20210111.jpg

思路： 客户端   获取文件内容--》发送出去
      服务端   接收文件内容--》写入磁盘
"""
from  socket import *

# 接收内容，写入文件
def recv_file(connfd):
    file = open("20210111.jpg",'wb')
    # 边收边写
    while True:
        data = connfd.recv(1024)
        if not data or data == b"##":
            break
        file.write(data)
    file.close()
    connfd.send("传输完毕".encode())


def main():
    # 创建tcp套接字
    tcp_socket = socket()
    tcp_socket.bind(("0.0.0.0",8888))
    tcp_socket.listen(5)

    while True:
        connfd,addr = tcp_socket.accept()
        print("Connect from",addr)
        # 接收文件
        recv_file(connfd)
        connfd.close()

if __name__ == '__main__':
    main()