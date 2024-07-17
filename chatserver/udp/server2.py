import socket
import os
#from _thread import *
import threading

ServerSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
host = '127.0.0.1'
port = 8887
ThreadCount = 0
ServerSocket.bind((host, port))
print("Waiting for connections...")
# ServerSocket.listen(1)
ServerSocket.

def threaded_client(connection, address):
    connection.send(str.encode("Welcome to the chat."))
    while True:
        data = connection.recv(2048) #2048 1024
        reply = str(address) + ' says: ' + data.decode('utf-8')
        if not data:
            break
        connection.sendall(str.encode(reply))
    connection.close()

while True:
    Client, address = ServerSocket.accept()
    print("Connected to: " + address[0] + ':' + str(address[1]))
    #start_new_thread(threaded_client, (Client, ))
    Thread.Thread(target=threaded_client, args=(Client, address[0]))
    ThreadCount += 1
    print("Thread Number: " + str(ThreadCount))
ServerSocket.close()

