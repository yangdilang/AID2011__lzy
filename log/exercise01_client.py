from socket import *
def send_file(tcp_socket,filename):
    file = open(filename,"rb")
    # 边读边发送
    while True:
        data = file.read(1024)
        if not data:
            break
        tcp_socket.send(data)
    file.close()
    # tcp_socket.send(b"##") # 告知服务端结束
    msg = tcp_socket.recv(1024)
    print("From server:", msg.decode())
def main(filename):
    tcp_socket = socket()
    tcp_socket.connect(("127.0.0.1",8888))
    # 发送文件
    send_file(tcp_socket,filename)
    tcp_socket.close()

if __name__ == '__main__':
    main("./zly.jfif")