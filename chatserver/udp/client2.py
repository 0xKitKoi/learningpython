import socket
from threading import Thread
import time

#def timer(name, delay, repeat):
#    print("Timer: " + name + " Started")
#    while repeat > 0:
#        time.sleep(delay)
#        print(name + ": " + str(time.ctime(time.time())))
#        repeat -= 1
#    print("Timer: " + name + " Completed")
#
#def treadStart():
#    t1 = Thread(target=timer, args=("Timer1", 1, 5))
#    t2 = Thread(target=timer, args=("Timer2", 2, 5))
#    t1.start()
#    t2.start()
#    print("Main completed")

def Main():
    host = '127.0.0.1'
    port = 8889
    server = ('127.0.0.1', 8887)
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((host, port))
    message = input("-> ")
    while message != 'q':
        s.sendto(message.encode('utf-8'), server)
        data, addr = s.recvfrom(1024)
        data = data.decode('utf-8')
        print("Recived from server: " + data)
        message = input("-> ")
    s.close()

if __name__ == '__main__':
    Main()
