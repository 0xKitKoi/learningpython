import os
from time import sleep

def Main():
    uin = int(input("Read or Write to a file? (1/2) -> "))
    if uin == 1:
        read()
    elif uin == 2:
        write()
    else:
        print("Invalid.")
        sleep(5)
        os.system('clear')
        Main()
def read():
    f = open("myfile.txt", "r")
    for line in f:
        print(line.strip('\n\r'))
    f.close()
def write():
    file = open("myfile.txt", 'w')
    for i in range(4):
        file.write(input("Enter a word. -> ") + '\n')
    file.close()

if __name__ == "__main__":
    Main()