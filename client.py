import socket
file = open("/Users/oskarfranz/Desktop/Final redes/doc.txt", "r")
toSend = file.read()
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((socket.gethostname(), 80))
client.send(toSend.encode("utf-8"))
print("\n\nEnviando archivo: ", file.name)
encrypted = client.recv(1024)

with open('doc.txt', 'wb') as encrypted_file: 
    encrypted_file.write(encrypted)

print("Archivo encriptado: \n\n" + encrypted.decode("utf-8"))