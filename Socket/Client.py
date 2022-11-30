import socket
import platform
import os

print("Le client est connecté")

client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client_socket.connect(("localhost", 4000))

msg = ""

data = ""

while msg.lower() != "Kill" and msg != "Disconnect" and data != "Disconnect" and data != "Kill":
    msg = input("--> ")
    if msg == "Disconnect":
        print("Vous allez être déconnecté")
        rep = input("continuer (y/n)")
        if rep == "y":
            print("Déconnection")
            client_socket.send(msg.encode())
        else:
            pass
    else:
        client_socket.send(msg.encode())
    data = client_socket.recv(1024).decode()
    print(data)

client_socket.close()
