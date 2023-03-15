import pygame, sys
from pygame.locals import *
from map import *
from entity import *
from constants import *
from camera import *
#from character import *

class Game():
    def __init__(self):
        # fenêtre du jeu
        self.scr_size = (scr_width, scr_height)
        self.screen = pygame.display.set_mode(self.scr_size)
        pygame.display.set_caption("Multiplayer Roguelike [v1.1]")
        self.cp437 = pygame.font.Font(".\\font\PerfectDOSVGA437.ttf", 16) # font

        self.player = Player((TILE_SIZE*2,TILE_SIZE*2), camera_group)
        
        self.Map = Map()
        #self.Player = Player()

        self.camera_offset_x = self.Player.rect.x
        self.camera_offset_y = self.Player.rect.y

        # définir une liste pour stocker les collisions, voir Map
        # dessiner les groupe de calques Map ?

    def show_debug_info(self):
        # Titre
        debug_title = "Debug Info :"
        # FPS
        fps_str = str(int(self.clock.get_fps())) + " FPS"
        # Player coordinates
        player_coord_str = "x:" + str(int(self.Player.rect.x/TILE_SIZE)) +" y:" + str(int(self.Player.rect.y/TILE_SIZE))

        debug_info = debug_title+"\n"+fps_str+"\n"+player_coord_str
        debug_disp = self.cp437.render(debug_info, False, COLOR[3])
        self.screen.blit(debug_disp, (scr_width -TILE_SIZE*16, 0))

    def handle_input(self):
        """
        Method to get all input and execute stuff linked to those inputs
        """
        pressed = pygame.key.get_pressed()
        
        if pressed[pygame.K_UP]:
            self.Player.direction = "UP"
            #self.camera_offset_y -= self.Player.speed
        elif pressed[pygame.K_DOWN]:
            self.Player.direction = "DOWN"
            #self.camera_offset_y += self.Player.speed
        elif pressed[pygame.K_LEFT]:
            self.Player.direction = "LEFT"
            #self.camera_offset_x -= self.Player.speed
        elif pressed[pygame.K_RIGHT]:
            self.Player.direction = "RIGHT"
            #self.camera_offset_x += self.Player.speed

    def update(self):
        self.screen.fill((0,0,0)) # clear the screen

        # Update
        #self.handle_input()

        #print(list_sprite.sprites, list_wall.sprites)
        #list_sprite.empty() # prevent memory overflow
        #list_wall.empty()
        
        self.Map.load() # TODO : ask to load a new level if necessary
        
        camera_group.update()
        camera_group.custom_draw(self.player)
        
        # list_sprite.update()
        # self.Player.update()
        # Draw the game
        # list_sprite.draw(self.screen)
        # self.Player.draw(self.screen) # need to find a way to update and draw all entity at the same time

        # Draw on top of the game (for GUI)
        self.show_debug_info()
        pygame.display.flip()

    def run(self):
        self.clock = pygame.time.Clock()

        # game loop
        running = True
        while running:
            # closing the window without crashing the game
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
                if event.type == pygame.MOUSEWHEEL:
                    camera_group.zoom_scale += event.y * 0.03

            
            self.update()
            pygame.display.update()
            self.clock.tick(60) # limite the FPS à 60

        pygame.quit() # stop pygame
        sys.exit()  # stop script