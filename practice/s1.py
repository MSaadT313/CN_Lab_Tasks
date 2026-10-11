import socket 
s = socket.socket()
print("Socket created")

s.bind(('localhost', 9999))
s.listen(3)
print("Waiting for connections: ")

while True:
    c, address = s.accept()
    print("Connected with ",address)

    c.send(bytes("Connected to Saad Server",'utf-8'))

    c.close()
    

