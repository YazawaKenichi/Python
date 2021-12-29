import socket

# ブロードキャストするときは 255.255.255.255 ではなく空文字
HOST = ''
PORT = 60000

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:    # UDP 通信
    s.bind((HOST, PORT))
    while True:
        try:
            msg, addr = s.recvfrom(1024)
            s.sendto('Hello World!'.encode('utf-8'), addr)

        except KeyboardInterrupt:
            print('Interrupted.')
            break

        except socket.error:
            print('Has error occurred.')
            pass

