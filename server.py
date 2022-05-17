import nacl.utils
import socket
from cryptography.fernet import Fernet

def cifrar(key, toEncode):


    with open('filekey.key', 'wb') as filekey: 
        filekey.write(key)
        
    with open('filekey.key', 'rb') as filekey: 
        key = filekey.read() 
    
    # with open('doc.txt', 'wb') as originalFile: 
    #     originalFile.write(toEncode.encode()) 

    fernet = Fernet(key) 

    with open('doc.txt', 'rb') as file: 
        original = file.read() 
        
        encrypted = fernet.encrypt(original) 
        return encrypted




server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((socket.gethostname(), 80))
server.listen(10)
# print(random)
key = Fernet.generate_key() 

while 1:
    client, address = server.accept()
    if(client):
        print("Conectado al cliente.")
        toEncode = client.recv(1024).decode("utf-8")
        print("Recieved file with content: ", toEncode)
        encrypted = cifrar(key, toEncode);
        print("Content is now encrypted")
        print("Sending encrypted file to client...")
        client.send(encrypted)
        print("Encrypted file successfully sent to the client!")

        # client.send(random.encode())
    else:
        print("Intentando conectar con el cliente...")





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