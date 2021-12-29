# Python Object を受け取る

import socket
import pickle

# socket.socket() でソケットを作成する
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   # AF_INET で IPv4 AF_INET6 で IPv6 TCP で SOCK_STREAM
s.connect((socket.gethostname(), 1235)) # 指定したサーバに接続を試みる
# s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

full_msg = b''
while True:
    msg = s.recv(1024)  # recv 一度に受け取るデータサイズを指定する
    if len(msg) <= 0:
        break
    full_msg += msg # 文字をつなげていく
    # print(full_msg.decode("utf-8"))  # full_msg.decode("utf-8") utf-8 にでコードする
d = pickle.loads(full_msg)
print(d)

