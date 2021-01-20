from socket import *

# 服务器地址
ADDR = ("127.0.0.1",55556)
# while True:
#     msg = input(">>")
#     if not msg:
#         break
#     tcp_socket = socket()
#     tcp_socket.connect(ADDR)
#     tcp_socket.send(msg.encode())
#     data = tcp_socket.recv(1024)
#     print("From server:",data.decode())
#     tcp_socket.close()

class QueryWord:
    def __init__(self):
        self.sock = socket()#创建udp套接字

    def close(self):
        self.sock.close()

    # 网络传输
    def recv_mean(self,word):
        while 1:
            self.sock.connect(ADDR)
            self.sock.send(word.encode())
            mean = self.sock.recv(1024)
            return mean.decode()

    # 输入输出
    def query_word(self):
            word = input("Word:")
            mean = self.recv_mean(word)
            print("%s : %s"%(word,mean))


if __name__ == '__main__':
    while 1:
        query = QueryWord()
        query.query_word() # 查单词
        query.close()