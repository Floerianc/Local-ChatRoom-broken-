import socket
from threading import Thread

clients = {}

host = "192.168.178.27" # 192.168.178.27, 192.168.178.41
port = 27

# clients dict to store information about clients connection
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# set configuration so that many clients can request on one port.
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# bind the IP and port to the socket object.
sock.bind((host, port))

def handle_clients(conn):
    # get client's name from it's connection
    try:
        name = conn.recv(1024).decode()
    except Exception as ex:
        print(ex)


    # send the client a welcoming message
    welcome_message = f"Welcome {name}, good to see you!"
    conn.send(bytes(welcome_message, "utf8"))

    msg = name + " has recently joined us!"
    # send message to every connected client
    broadcast(bytes(msg, "utf8"))
    clients[conn] = name

    i = 0
    while True:
        try:
            msg = conn.recv(1024)
            broadcast(msg, name + ": ")
        
        except Exception as ex:
            i += 1
            if i < 3:
                print(ex)
                t.join()
            else:
                pass

def broadcast(msg, prefix=""):
    for client in clients:
        try:
            client.send(bytes(prefix, "utf8") + msg)
        except Exception as ex:
            print(ex)

def accept_client_connection():
    while True: # accepts clients request
        client_conn, client_address = sock.accept()
        print(f"{client_address} has connected to the Server.")
        client_conn.send(bytes("Welcome to the chat room, Please type your name to continue", "utf8"))

        # start the handle clients function in a thread.
        Thread(target=handle_clients, args=(client_conn,)).start()

if __name__ == "__main__":
    sock.listen(3)
    print("Listening to port:", port)
    t = Thread(target=accept_client_connection)
    t.start()
    t.join()