import socket

# ブロードキャストするときは 255.255.255.255 ではなく空文字
# HOST = ''
PORT = 60001

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:    # UDP 通信
    host = socket.gethostname() # ホストに割り当てられている IP を取得する
    s.bind((socket.gethostbyname(host), PORT))

    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.listen(1)

    while True:
        try:
            client, addr = s.accept()
            # msg, addr = s.recvfrom(1024)
            # バッファサイズ 100
            data = client.recv(100)
            print(f'data: {data}, addr: {addr}')

            client.sendall("Hello World!".encode("utf-8"))
            # s.sendto('Hello World!'.encode('utf-8'), addr)

        except KeyboardInterrupt:
            print('Interrupted.')
            break

        except socket.error:
            print('Has error occurred.')
            pass

