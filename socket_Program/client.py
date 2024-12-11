import socket

s=  socket.socket()

s.connect(('localhost',7000))

print(s)