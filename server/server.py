import socket, threading, sys

def main():

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((socket.gethostname(), 1234))
    s.listen(5) # 5 clients maximum

    while True:
        # now our endpoint knows about the OTHER endpoint.
        clientsocket, address = s.accept()
        print(f"Connection from {address} has been established.")
        clientsocket.send(bytes("Hey there!!!","utf-8"))
        clientsocket.close()
        sys.exit(0) # must be executed only if the server recive the instruction from an admin to turn off

if __name__ == "__main__":
    main()