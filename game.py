import pygame, sys
from pygame.locals import *
from map import *
from entity import *
#from character import *
from constants import *

class Game():
    def __init__(self):
        # fenêtre du jeu
        self.scr_size = (scr_width, scr_height)
        self.screen = pygame.display.set_mode(self.scr_size)
        pygame.display.set_caption("Multiplayer Roguelike [v1]")

        
        self.Map = Map()
        self.Player = Player()

        # définir une liste pour stocker les collisions, voir Map
        # dessiner les groupe de calques Map ?
        
    def handle_input(self):
        """
        Method to get all input and execute stuff linked to those inputs
        """
        pressed = pygame.key.get_pressed()

        if pressed[pygame.K_UP]:
            self.Player.direction = "UP"
        elif pressed[pygame.K_DOWN]:
            self.Player.direction = "DOWN"
        elif pressed[pygame.K_LEFT]:
            self.Player.direction = "LEFT"
        elif pressed[pygame.K_RIGHT]:
            self.Player.direction = "RIGHT"

    def update(self):
        # vérification des collisions et autre
        self.Map.load()
        list_sprite.update()
        list_sprite.draw(self.screen)

        print(list_sprite.sprites, list_wall.sprites)
        list_sprite.empty() # prevent memory overflow
        list_wall.empty()
        #self.Player.draw(self.screen)

    def run(self):
        clock = pygame.time.Clock()

        # boocle du jeu
        running = True
        while running:
            
            self.handle_input()
            self.update()
            pygame.display.flip()

            # closing the window without crashing the game
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False # bloque l'entré dans la boucle de jeu

            
            pygame.display.update()
            clock.tick(60) # limite le FPS à 60

        # éteind tout
        # must disconect the client of the server
        pygame.quit() # arret pygame
        sys.exit()  # arret script