"""
练习：
使用udp完成网络单词查询
从客户端输入单词，发送给服务端，得到单词的解释，打印
出来
利用 dict 数据库下的 words表来完成
"""
from socket import *
import pymysql


# 数据处理类
class Dict:
    def __init__(self):
        self.kwargs = {
            "host": "localhost",
            "port": 3306,
            "user": "root",
            "password": "123456",
            "database": "dict",
            "charset": "utf8"
        }
        self.connect()

    # 完成数据库连接
    def connect(self):
        self.db = pymysql.connect(**self.kwargs)
        self.cur = self.db.cursor()

    # 关闭
    def close(self):
        self.cur.close()
        self.db.close()

    def get_mean(self, word):
        sql = "select mean from words where word=%s;"
        self.cur.execute(sql, [word])
        mean = self.cur.fetchone()  # （mean,） None
        if mean:
            return mean[0]
        else:
            return "Not Found"


# 逻辑处理 网络搭建
class QueryWord:
    def __init__(self, host="0.0.0.0", port=55556):
        self.host = host
        self.port = port
        self.dict = Dict()
        self.sock = self.create_socket()
        # self.times=times

    def create_socket(self):
        sock = socket(AF_INET, SOCK_STREAM)
        sock.bind((self.host, self.port))
        sock.listen(5)
        return sock

    def close(self):
        self.sock.close()

    # 查找单词方法
    # def query_word(self):
    #     while True:
    #         word, addr = self.sock.recvfrom(128)
    #         # 查询单词
    #         mean = self.dict.get_mean(word.decode())
    #
    #         self.sock.sendto(mean.encode(), addr)
    def query_word(self):
        while True:
            connfd, addr=self.sock.accept()
            word = connfd.recv(1024)
            mean = self.dict.get_mean(word.decode())
            print("收到:",word.decode())
            connfd.send(mean.encode())
            connfd.close()


# while True:
#     connfd,addr = tcp_socket.accept()
#
#     data = connfd.recv(1024)
#     print("收到:",data.decode())
#     connfd.send(b"Thanks")
#     connfd.close()


if __name__ == '__main__':
    query = QueryWord()
    query.query_word()
