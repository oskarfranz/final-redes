import socket
file = open("/Users/oskarfranz/Desktop/Final\ redes/doc.txt", "r")
toSend = file.read()
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((socket.gethostname(), 80))
client.send(toSend.encode("utf-8"))
random = client.recv(128)
print("Archivo encriptado: \n\n" + random.decode("utf-8"))