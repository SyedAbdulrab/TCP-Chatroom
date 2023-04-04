import threading
import socket
import time

host = '127.0.0.1'  # local host
port = 55555

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

clients = []
nicknames = []


def broadcast(message):
    for client in clients:
        client.send(message)




def handle(client):
    while True:
        try:
            msg = message = client.recv(1024)

            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast(f"{nickname} left the chat".encode('ascii'))
            nicknames.remove(nickname)
            break


def receive():
    while True:
        client, address = server.accept() # accept clients all the time

        print(f"Connected with {str(address)}")
        # when someone connects to the server we will send the address to the
        # servers console so that the admin knows that someone just connected to the server

        client.send('NICK'.encode('ascii'))
        # the client will now receive the NICK message which will signal to the client to enter his nickname
        nickname = client.recv(1024)  # receiving the nickname from the client




        nicknames.append(nickname)  # appending the nickname to the nickname list
        clients.append(client)  # appending the client to the client list

        print(f"Nickname of the client is {nickname}\n")
        broadcast(f"{nickname} joined the chat".encode('ascii'))
        # here we broadcast to all the clients connected to the server that this client just joined the chat
        # client.send("Connected to the server")
        # the client will receive the message that the connection was successful

        # we will run one thread for each client as we will have to manage them at the same time
        thread = threading.Thread(target=handle,args=(client,))
        thread.start()


print('Server is listening...')

receive()

# if (message == 'private'):
#     client.send('enter the nickname of private msg receiver')
#     rcv_name = client.recv(1024)
#     client.send('enter your message')
#     prv_msg = client.recv(1024)
#     for client in clients:
#         client.send(rcv_name, prv_msg)
# else: