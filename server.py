from http import server
import socket
import threading
import time

SERVER_IP = "127.0.0.1"
PORT = 5050
ADDR = (SERVER_IP, PORT)
FORMATO = "utf-8"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

conexoes = []
mensagens = []

def send_individual_message(connection):
    pass

def send_all_message():
    pass

def clients(conn, addr):
    print(f'NOVA CONEXAO um novo usuário se conectou pelo endereço: {addr}')
    global conexoes
    nome = False

    while(True):
        msg = conn.recv(1024).decode(FORMATO)
        if(msg):
            if(msg.startswith('nome')):
                mensagem_separada = msg.split('=')
                nome = mensagem_separada[1]
                map_connexion = {
                    "conn":conn,
                    "nome":nome,
                    "addr":addr,
                    "last":last,

                }

                conexoes.append(map_connexion)

def start():
    print("INICIANDO socket")
    socket.listen()
    while(True):
        conn, addr = socket.accept()
        thread = threading.Thread(target=clients, args=())
        thread.start()



start()