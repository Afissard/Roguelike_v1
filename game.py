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
        self.cp437 = pygame.font.SysFont(".\\font\PerfectDOSVGA437.ttf", 24) # font
        
        self.Map = Map()
        self.Player = Player()

        # définir une liste pour stocker les collisions, voir Map
        # dessiner les groupe de calques Map ?

    def show_debug_info(self):
        # Titre
        debug_title = "Debug Info :"
        debug_disp = self.cp437.render(debug_title, False, (0,200,0))
        self.screen.blit(debug_disp, (scr_width -128, 0))
        # FPS
        fps_str = str(int(self.clock.get_fps())) + " fps"
        fps_disp = self.cp437.render(fps_str, False, (0,200,0))
        self.screen.blit(fps_disp, (scr_width -128, 20))
        # Player coordinates
        player_coord_str = "x:" + str(self.Player.rect.x/TILE_SIZE) +" y:" + str(self.Player.rect.y/TILE_SIZE)
        player_coord_disp = self.cp437.render(player_coord_str, False, (0,200,0))
        self.screen.blit(player_coord_disp, (scr_width -128, 35))

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
        self.screen.fill((0,0,0))
        self.Map.load() # TODO : only load the map when it's created, else draw previous map

        list_sprite.update()
        self.Player.update()
        
        list_sprite.draw(self.screen)
        self.Player.draw(self.screen) # need to find a way to update and draw all entity at the same time

        #print(list_sprite.sprites, list_wall.sprites)
        # list_sprite.empty() # prevent memory overflow
        # list_wall.empty()

        # Draw on top of the game
        self.show_debug_info()
        pygame.display.flip()

    def run(self):
        self.clock = pygame.time.Clock()

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
            self.clock.tick(60) # limite le FPS à 60

        # éteind tout
        # must disconect the client of the server
        pygame.quit() # arret pygame
        sys.exit()  # arret script