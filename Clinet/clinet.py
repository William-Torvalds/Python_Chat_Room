import socket
from threading import Thread
from time import *

SERVER_IP = input("服务器IP地址>> ")
PORT = 6666


def recv_thread(conn):
    while True:
        data = conn.recv(81920)
        if not data:
            break
        else:
            print(("\n" + data.decode()))

# 1. 实例化一个 socket
cs = socket.socket()
# 2. 连接服务器, 会动态从操作系统得到一个端口
cs.connect((SERVER_IP, PORT))
# 3. 收发数据

t = Thread(target=recv_thread,
           args=(cs,),
           daemon=True)
t.start()



username = input("请输入用户名>>")
splash_screen_times = 0


while True:
    msg = input("请输入要发送的内容，发斜杠为指令，目前可使用的指令有/q(退出)>> ")

    if msg == "/q":
        break

    elif msg == "":
        if splash_screen_times == 3:
            print(">> 禁止刷屏")
            sleep(0.5)
            break
        print(">> 为防止刷屏，禁止输入空格")
        msg = ""
        splash_screen_times += 1

    else:
        msg = f"{username}说：{msg}"
        cs.sendall(msg.encode())
