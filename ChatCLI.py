import socket


def connect_to_server(server):
    print(f"Connecting to server running on {server}: 59002")
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.connect((server, 59002))

    while True:

        msg_recv = server_socket.recv(1024).decode("utf-8")
        if msg_recv.startswith("SUBMITNAME"):
            send_name(server_socket)
        elif msg_recv.startswith("NAMEACCEPTED"):
            print("Chatter - " + msg_recv[13::])
            send_message(server_socket)
        elif msg_recv.startswith("MESSAGE"):

            print(msg_recv[8::] + "\n")
            send_message(server_socket)


def send_name(server_socket):
    user_name = (input("Skriv dit navn\n") + "\n").encode("utf-8")
    server_socket.sendall(user_name)


def send_message(server_socket):
    msg = (input() + "\n").encode("utf-8")
    server_socket.sendall(msg)


if __name__ == '__main__':
    server_address = socket.get = input("Hej, hvilken server vil du tilslutte dig? (Tryk ENTER for localhost.)")
    if server_address == "":
        server_address = "localhost"
    connect_to_server(server_address)
