# 受け取るデータの大きさが一度に受け取るデータサイズよりも大きくても最後まで接続したままにできるように改善したもの
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   # AF_INET で IPv4 AF_INET6 で IPv6 TCP で SOCK_STREAM
s.connect((socket.gethostname(), 1235))
# s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

full_msg = b''
while True:
    msg = s.recv(8)  # recv 一度に受け取るデータサイズを指定する
    if len(msg) <= 0:
        break
    full_msg += msg # 文字をつなげていく
    print(full_msg.decode("utf-8"))  # full_msg.decode("utf-8") utf-8 にでコードする

