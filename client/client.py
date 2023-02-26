import pygame, socket
from game import Game

def socket_test():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((socket.gethostname(), 1234))

    full_msg = ''
    while True:
        msg = s.recv(8)
        if len(msg) <= 0:
            break
        full_msg += msg.decode("utf-8")

    print(full_msg)

def main():
    pygame.init()

    # socket_test()
    game = Game()
    game.run()
    
if __name__ == "__main__":
    main()