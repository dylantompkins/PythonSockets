import socket
from math import sin
from time import sleep

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 8888))

x = 0

def mathFunc(x):
    return round(
        20*sin(x)
    )

while True:
    sock.send(
        mathFunc(x).to_bytes(1, "big", signed=True)
    )
    print('Sent: ' + str(mathFunc(x)))
    x += 0.1
    sleep(0.1)