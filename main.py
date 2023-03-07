import pygame
from game import Game

def main():
    pygame.init()

    # socket_test()
    game = Game()
    game.run()
    
if __name__ == "__main__":
    main()