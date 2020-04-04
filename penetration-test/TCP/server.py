# Updated: 04/04/20
# Basics of client/server TCP communication
import socket

host = "127.0.0.1"
port = 9337

sock_ = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
tupl=(host,port)
sock_.bind(tupl)
sock_.listen(1)

print("\nServer started...\n")

conn,addr = sock_.accept()

print("Connection established with: ",str(addr))

message = "\nThank you for connecting "+str(addr)
conn.send(message.encode("ascii"))
conn.close()