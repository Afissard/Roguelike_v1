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
        self.cp437 = pygame.font.Font("font\PerfectDOSVGA437.ttf", 16) # font
        
        self.Map = Map()
        self.Player = Player()

        # définir une liste pour stocker les collisions, voir Map
        # dessiner les groupe de calques Map ?

    def show_debug_info(self):
        # Titre
        debug_title = "Debug Info :"
        # FPS
        fps_str = str(int(self.clock.get_fps())) + " FPS"
        # Player coordinates
        player_coord_str = "x:" + str(self.Player.rect.x/TILE_SIZE) +" y:" + str(self.Player.rect.y/TILE_SIZE)

        debug_info = debug_title+"\n"+fps_str+"\n"+player_coord_str
        debug_disp = self.cp437.render(debug_info, False, COLOR[3])
        self.screen.blit(debug_disp, (scr_width -TILE_SIZE*8, 0))

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
        self.handle_input()

        self.screen.fill((0,0,0)) # clear the screen
        # Update
        #print(list_sprite.sprites, list_wall.sprites)
        #list_sprite.empty() # prevent memory overflow
        #list_wall.empty()
        self.Map.load() # TODO : ask to load a new level if necessary
        #list_sprite.update()
        self.Player.update()
        
        # Draw the game
        list_sprite.draw(self.screen)
        self.Player.draw(self.screen) # need to find a way to update and draw all entity at the same time

        # Draw on top of the game (for GUI)
        self.show_debug_info()
        pygame.display.flip()

    def run(self):
        self.clock = pygame.time.Clock()

        # boocle du jeu
        running = True
        while running:
            # closing the window without crashing the game
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False # bloque l'entré dans la boucle de jeu

            
            self.update()
            pygame.display.update()
            self.clock.tick(60) # limite le FPS à 60

        # éteind tout
        # must disconect the client of the server
        pygame.quit() # arret pygame
        sys.exit()  # arret script