# クライアントソケット Version 2
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1235))
# s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

full_msg = b''
while True:
    msg = s.recv(1024)  # 一度に受け取るデータのサイズを指定する
    if len(msg) < 0:
        break;
    full_msg += msg # 受け取った文字列をつなげていく
    print(full_msg.decode("utf-8"))  # デコードして表示


