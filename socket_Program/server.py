import socket

from sqlalchemy.event import listen

s = socket.socket()
print(s,'socket created')

s.bind(('localhost',7000)) #to bind it with address and ip
s.listen(3)

while True:
    c,addr = s.accept()
    print("Connected to ",c,addr)

    c.send(bytes("WELCOME to scoket",'utf-8'))

    c.close()