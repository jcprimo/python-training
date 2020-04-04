# Updated: 04/04/20
# With this file you can create a simple server/client connection]
# This example runs a server on your local machine then run the client to establish
# the communication among client server
import socket

sock_ = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock_.connect(("127.0.0.1",9337))
msg = sock_.recv(1024) #How many bytes you want to receive
sock_.close()
print(msg.decode("ascii"))