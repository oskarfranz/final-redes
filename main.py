from cryptography.fernet import Fernet

key = Fernet.generate_key() 

def cifrar(key):


    with open('filekey.key', 'wb')  as filekey: 
        filekey.write(key)
        
    with open('filekey.key', 'rb') as filekey: 
        key = filekey.read() 

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


cifrar(key)
descifrar(key)