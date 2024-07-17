import socket
import threading

host = '127.0.0.1'
port = 8890
server = ('127.0.0.1', 8887)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host, port))
running = True

def stop():
    s.close()
    running = False

def getMessages():
    while True:
        data = s.recv(1024)
        data = data.decode('utf-8')
        print(" -- " + data)

def texting():
    message = input("-> ")
    while message != 'q':
        s.sendto(message.encode('utf-8'), server)
        message = input("-> ")
    stop()

def Main():
    t1 = threading.Thread(target=getMessages)
    t2 = threading.Thread(target=texting)
    t2.start()
    t1.run()
    


if __name__ == '__main__':
    while running:
        Main()
