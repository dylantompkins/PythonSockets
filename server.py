import socket

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind(('localhost', 8888))
serversocket.listen(5)

clientsocket = None

while True:
    if (clientsocket == None):
        (clientsocket, address) = serversocket.accept()
    else:
        byte = clientsocket.recv(1)
        num = int.from_bytes(byte, "big", signed=True)
        spaces = 45 + num
        print(' ' * spaces + '|')

# TODO
# - threading for multiple clients
# - use a package for fancier graphing that terminal output