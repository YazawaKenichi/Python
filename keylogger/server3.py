# Python Object を送信する

import socket
import pickle

data = {1: "Apple", 2: "Orange"}

# socket.socket() ソケットの作成
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   # AF_INET で IPv4 を指定する。(IPv6 の時は AF_INET6)
# 今回は TCP プロトコルを利用するので SOCK_STREAM とする
s.bind((socket.gethostname(), 1235))    # IPとポート番号を指定します  # bind ホスト名とポート番号を指定する
s.listen(5) # 引数にキューの数を指定する。ここで指定した数だけ並列的にリクエストを処理することができる。
# bint() listen() でソケットが通信待ちの状態になる

while True:
    clientsocket, address = s.accept()  # 接続の受信を行う
    print(f"Connection from {address} has been established!")   # アドレスを表示する
    msg = pickle.dumps(data)
    print(msg)

    clientsocket.send(msg) # データを送信する
    clientsocket.close()    # 接続を中断する

