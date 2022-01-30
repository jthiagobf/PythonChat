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

def send_individual_message(conexao):
    print(f"ENVIANDO mensagem para {conexao['addr']}")
    for i in range(conexao['last'], len(mensagens)):
        mensagem_de_envio = "msg=" + mensagens[1]
        conexao['conn'].send(mensagem_de_envio)
        conexao['last'] = i + 1
        time.sleep(0.2)




def send_all_message():
    global conexoes
    for conexao in conexoes:
        send_individual_message(conexao)



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
                map_connection = {
                    "conn":conn,
                    "nome":nome,
                    "addr":addr,
                    "last":0,

                }

                conexoes.append(map_connection)
                send_individual_message(map_connection)

            elif(msg.startswith("msg=")):
                 mensagem_separada = msg.split('=')
                 mensagem = mensagem_separada[1]
                 mensagem.append(mensagem)
                 send_all_message()



def start():
    print("INICIANDO socket")
    socket.listen()
    while(True):
        conn, addr = socket.accept()
        thread = threading.Thread(target=clients, args=())
        thread.start()



start()