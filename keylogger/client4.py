import socket

PORT = 50000
BUFFER_SIZE = 1024

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(('127.0.0.1', PORT))  # サーバに接続
    data = input('Please input > ')
    s.send(data.encode())   # データの送信
    print(s.recv(BUFFER_SIZE).decode()) # 返信されてきたものを表示
    # ソケットに読み書きするデータはバイト（文字列）ではないため、送信時にエンコードし、受診時にデコードする必要がある

