import nacl.utils
import socket
from cryptography.fernet import Fernet

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((socket.gethostname(), 80))
server.listen(10)
# print(random)

while 1:
    client, address = server.accept()
    if(client):
        print("Conectado al cliente.")
        toEncode = server.recv(128).decode("utf-8")
        cifrar(key, toEncode);
        server.send(toEncode.encode("utf-8"))
        # client.send(random.encode())
    else:
        print("Intentando conectar con el cliente...")


key = Fernet.generate_key() 

def cifrar(key, toEncode):


    with open('filekey.key', 'wb') as filekey: 
        filekey.write(key)
        
    with open('filekey.key', 'rb') as filekey: 
        key = filekey.read() 
    
    with open('doc.txt', 'wb') as originalFile: 
        originalFile.write(toEncode) 

    fernet = Fernet(key) 

    with open('doc.txt', 'rb') as file: 
        original = file.read() 
        
        encrypted = fernet.encrypt(original) 

    with open('doc.txt', 'wb') as encrypted_file: 
        encrypted_file.write(encrypted) 


def descifrar(key):  

    with open('filekey.key', 'wb') as filekey: 
        filekey.write(key)
    
    fernet = Fernet(key)
    
    with open('doc.txt', 'rb') as enc_file: 
        encrypted = enc_file.read() 
        print(encrypted, "\n")

    decrypted = fernet.decrypt(encrypted) 
    
    with open('doc.txt', 'wb') as dec_file: 
        print(decrypted)
        dec_file.write(decrypted) 


def firmar():
    print("firmar")