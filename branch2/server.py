import socket

def Main():
        # Hard coding the host ip and port
        host = '192.168.1.121' # Loopback Address
        port = 5000
        # Creating a socket
        s = socket.socket()
        # Binding the socket to a tuple of the Host and Port
        s.bind((host,port))
        # listen to 1 connection
        s.listen(1)
        # Accept the connection
        c, addr = s.accept()
        print("Connection From: " + str(addr))

        while True:
                # Recieving Data, setting the buffer to 1024 bytes
                data = c.recv(1024)
                if not data:
                        break
                print("From Connected user: " + str(data))
                data = str(data).upper()
                print("Sending: " + str(data))
                c.send(data)
        c.close()

if __name__ == "__main__":
        Main()

