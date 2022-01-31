from concurrent.futures import thread
import threading
import socket

HOST = 'localhost'
PORT = 8888

def main():

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client.connect((HOST, PORT))
    except:
        return print('\nFalha ao se conectar com o servidor\n')

    username = input('User: ')
    print('\nCONECTADO')

    thread_1 = threading.Thread(target=receive_message, args=[client])

    thread_2 = threading.Thread(target=send_message, args=[client, username])

    thread_1.start()
    thread_2.start()

def receive_message(client):
    while True:
        try:
            msg = client.recv(2048).decode('utf-8')
            print(msg+'\n')
        except:
            print('\nUsuario desconectado do servidor\n')
            print('\nPressione ENTER para coninuar\n')
            client.close()
            break


def send_message(client, username):
    while True:
        try:
            msg = input('\n')
            client.send(f'{username}: {msg}'.encode('utf-8'))
        except:
            return

main()