import pygame, sys
from pygame.locals import *
from map import Map
from constants import *

class Game:
    def __init__(self):
        # fenêtre du jeu
        self.scr_size = (scr_width, scr_height)
        self.screen = pygame.display.set_mode(self.scr_size)
        pygame.display.set_caption("Multiplayer Roguelike [v1]")

        # définir une liste pour stocker les collisions, voir Map
        # dessiner les groupe de calques Map ?
        
    def handle_input(self):
        pressed = pygame.key.get_pressed()

        if pressed[pygame.K_UP]:
            print("up")
        elif pressed[pygame.K_DOWN]:
            print("down")
        elif pressed[pygame.K_LEFT]:
            print("left")
        elif pressed[pygame.K_RIGHT]:
            print("right")

    def update(self):
        # vérification des collisions et autre
        self.map = Map()
        self.map.load()

    def run(self):
        clock = pygame.time.Clock()

        # boocle du jeu
        running = True
        while running:
            
            self.handle_input()
            self.update()
            pygame.display.flip()

            # event manager
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False # bloque l'entré dans la boucle de jeu
        
            pygame.display.update()
            clock.tick(60) # limite le FPS à 60

        # éteind tout
        pygame.quit() # arret pygame
        sys.exit()  # arret script