import threading
import socket

host = 'localhost' #todo socket possui um 'host' e uma 'porta'
port = 8888

clients = []

def main():

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

    try:
        server.bind((host, port))
        server.listen() #define a quantidade de conexões com o servidor | Ex: server.listen(5) = suporta 5 conexões
    except:
        return print('\nnão foi possível iniciar o servidor\n')

    while True:
        client, address = server.accept()
        clients.append(client)

        thread1 = threading.Thread(target=messages, args=[client])
        thread1.start()

def messages(client):
    while True:
        try:
            msg = client.recv(2048)
            bcast(msg, client)

        except:
            delClient(client)
            break
        

def bcast(msg, client):
    for clientNames in clients:
        if clientNames != client:
            try:
                clientNames.send(msg)
            except:
                delClient(clientNames)



def delClient(client):
    clients.remove(client)






main()