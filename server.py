import socket

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind(('localhost', 8888))
serversocket.listen(5)

connection = None

class Connection:
    def __init__(self, socket):
        self.socket = socket

    def recv(self):
        byte = clientsocket.recv(1)
        self.num = int.from_bytes(byte, "big", signed=True)

    def display(self):
        spaces = 45 + self.num
        print(' ' * spaces + '|')

while True:
    if (connection == None):
        (clientsocket, address) = serversocket.accept()
        connection = Connection(clientsocket)
    else:
        connection.recv()
        connection.display()

# TODO
# - threading for multiple clients
# - use a package for fancier graphing that terminal output