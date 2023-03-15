import pygame, sys
from global_var import *
from camera import *
from entity import *

class Game():
    def __init__(self):
        self.screen = pygame.display.set_mode((1280,720))
        pygame.display.set_caption("Multiplayer Roguelike [v1.2]")
        self.clock = pygame.time.Clock()
        pygame.event.set_grab(False) # set to True if the game use the mouse

        # setup 
        self.camera_group = CameraGroup()
        self.player = Player((640,360), self.camera_group)


    def run(self):

        # game loop
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.type == pygame.MOUSEWHEEL:
                        self.camera_group.zoom_scale += event.y * 0.03

            self.screen.fill(COLOR[0])
	    
            self.camera_group.update()
            self.camera_group.custom_draw(self.player)
	    
            pygame.display.update()
            self.clock.tick()

