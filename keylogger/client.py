import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   # AF_INET で IPv4 AF_INET6 で IPv6 TCP で SOCK_STREAM
s.connect((socket.gethostname(), 1235))
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

msg = s.recv(1024)  # recv 一度に受け取るデータサイズを指定する
print(msg.decode("utf-8"))  # msg.decode("utf-8") utf-8 にでコードする

