import socket
import os
import sys
import platform
import psutil

print("Le serveur est On")

server_socket = socket.socket()
server_socket.bind(("127.0.0.1", 4000))
server_socket.listen(1)

while True :
    conn, address = server_socket.accept()
    msg = ""
    data = ""

    while msg.lower() != "Kill" and msg != "Disconnect" and data != "Disconnect" and data != "Kill":
        data = conn.recv(1024).decode()
        print(data)
        if data=='Disconnect':
            message = f'Vous allez être déconnecté'
            conn.send(message.encode())
            conn.close()
            rep = input("continuer (y/n)")
            if rep == "y":
                print("Déconnection")
            break
        server_socket.close()
        if data == 'os':
            message = f"Le noyau est {os.name}, Votre système est {platform.system()}, et votre version de windows est : {platform.release()}"
            conn.send(message.encode())
        elif data == 'ram':
            message = f"RAM memory : {psutil.virtual_memory()}"
            conn.send(message.encode())
        elif data == 'cpu':
            message = f"Le CPU est {platform.processor()}"
            conn.send(message.encode())
        elif data == 'ip':
            message = f"L'adresse ip est {socket.gethostbyname(socket.gethostname())}"
            conn.send(message.encode())
        elif data == 'none':
            message = f'La commande ne fait rien'
            conn.send(message.encode())
        elif data =='vpython':
            message = f'Voici la version actuelle de python {sys.version}'
            conn.send(message.encode())
        elif data =='dir':
            path = "C://"
            dir_list = os.listdir(path)
            message = f'voici le répertoire {dir_list}'
            conn.send(message.encode())
        elif data =='mkdir':
            message =f'Vous pouvez creer un nouveau chemin {os.mkdir()}'
            conn.send(message.encode())
        else:
            msg='Votre commande existe pas'
            conn.send(msg.encode())
    conn.close()

