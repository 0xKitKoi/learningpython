from cryptography.fernet import Fernet

print("Fernet Encryption Program.\n")
print("Encrption key as file: \n")
eK = str(input("--> "))
with open(eK, 'rb') as filekey:
        key = filekey.read()
fernet = Fernet(key)
    
def encFile(fileName):
    with open(fileName, 'rb') as file:
        original = file.read()
        encrypted = fernet.encrypt(original)

    with open(fileName, 'wb') as encrypted_file:
        encrypted_file.write(encrypted)

def decFile(fileName): 
    with open(fileName, 'rb') as enc_file:
        encrypted = enc_file.read()
        decrypted = fernet.decrypt(encrypted)

    with open(fileName, 'wb') as dec_file:
        dec_file.write(decrypted)

def Main():
    print("Encrypt or Decrypt?\n")
    print("Encrypt = 0 | Decrypt = 1 \n")
    uI = int(input("--> "))
    if (uI == 0):
        print("Filename: \n")
        fN = str(input("--> "))
        encFile(fN)
    elif (uI == 1):
        print("Filename: \n")
        fN = str(input("--> "))
        decFile(fN)

if __name__ == '__main__':
    Main()
