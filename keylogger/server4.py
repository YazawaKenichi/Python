import socket

PORT = 50000     # サーバ側の受付ポート番号
BUFFER_SIZE = 1024  # ソケットから読み取る際のバッファサイズ

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:    # ソケットの作成
    s.bind(('127.0.0.1', PORT)) # 
    s.listen()  # bind listen で通信待ちの状態にする
    while True:
        (connection, client) = s.accept()   # クライアントからの通信を受け付ける
        try:
            print('Client connected', client)
            data = connection.recv(BUFFER_SIZE)
            connection.send(data.upper())   # 大文字に変換して送信
        finally:
            connection.close()

