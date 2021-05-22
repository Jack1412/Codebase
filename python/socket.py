# 网络编程有一个重要的概念 socket（套接字），应用程序可以通过它发送或接收数据，套接字允许应用程序
# 将 I/O 插入到网络中，并与网络中的其他应用程序进行通信。

# socket工作流程：
# 1.建立连接：
#
#     服务器：socket--->address--->bind--->listen--->accept
#
#     客户端：socket--->connect
#
# 2.通信：收一发：recv(1024)<---send(byte)/sendall(byte)
#
# 3.关闭连接：close()

# *********************************服务端，server.py*********************************
# 导入socket模块
import socket
# 创建套接字 或使用server = socket.socket()
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 定义绑定的ip和端口，用元组定义
ip_port = ('127.0.0.1', 8888)
# 绑定监听:bind(address),在AF_INET下,以元组（ip,port）的形式表示地址
server.bind(ip_port)
# 设置最大连接数，默认为1
server.listen(5)
# 不断接受连接：one by one
while True:
    print("等待数据连接中……")
    # 接受客服端数据请求
    conn, address = server.accept()
    '''
    向客服端返回信息
    (注意：python3.x以上，网络数据的发送接收都是byte类型，
    发送接收String类型数据时需要对数据进行编码(发送：messages.enconde()；接收后转为String类型:messages.deconde())，pyhon2.x则直接发送数据无须编码)
    '''
    messages = "连接成功！"
    conn.send(messages.encode())
    # 计数信息条数
    count = 0
    # 一个连接中，不断的接受客户端发来的数据
    while True:
        data = conn.recv(1024)
        # 打印客户端发来的数据信息
        print(data.decode())
        # 判断是否退出当前连接,等在下一个连接
        if data == b'exit':
          break
        # 处理客户端数据（如：响应请求等）
        count = count + 1
        string = "第" + str(count) + "条信息：" + data.decode()
        conn.send(string.encode())
        # 主动关闭连接
    conn.close()



# *********************************客户端，client.py*********************************
import socket

#创建套接字
client = socket.socket()
#访问的服务器的ip和端口，用元组定义
ip_port = ("127.0.0.1", 8888)
#连接服务器主机
client.connect(ip_port)
#同一链接中，不断向服务器发生数据或请求
while True:
    #接收服务器发送或响应的数据
    data = client.recv(1024)
    #打印接收的数据；python3.x以上数据要编码(发送：data.enconde()；接收后转为String类型:data.deconde())
    print(data.decode())
    messages = input("请输入发生或请求的数据(exit退出)：")
    client.send(messages.encode())
    if messages == 'exit':
        break
    '''
    #接收服务器发送或响应的数据
    data = client.recv(1024)
    #打印接收的数据；python3.x以上数据要编码，发送enconde()；接收deconde()
    print(data.decode())
    '''
#关闭连接
client.close()


# 多线程通信
# TCP服务器与多个TCP客户端同时进行连续通信，只需要通过threading创建多线程任务handle_client就可以了
import socket
import threading
import random


def handle_client():
    # 接受客户端请求链接
    client, address = server.accept()
    print("[*] Accept connection from: %s:%d" % (address[0], address[1]))
    messages = "Hello World!"
    client.send(messages.encode())
    # 连续与当前连接的客户端通信
    while True:
        # 接受客户端数据
        request = (client.recv(1024)).decode()
        # 判断是否结束通信
        if request == 'exit':
            break
        print("[*] Received from %s:%d : %s" % (address[0], address[1], request))
        # 发送响应信息给客户端
        client.send((str(random.randint(1, 1000)) + "：" + "ACK!").encode())
    # 关闭当前连接
    client.close()


if __name__ == "__main__":
    # 创建套接字
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 定义绑定ip和端口
    ip = '127.0.0.1'
    port = 8888
    # 绑定监听
    server.bind((ip, port))
    # 设置最大连接数，默认为1
    server.listen(5)
    print("[*] Listening on %s:%d" % (ip, port))
    # 循环开启线程，接受多个客户端的链接通信
    while True:
        # 创建一个线程
        client_handler = threading.Thread(target=handle_client)
        # 开启线程
        client_handler.start()