"""
Pillow ressources : https://stackoverflow.com/questions/138250/how-to-read-the-rgb-value-of-a-given-pixel-in-python

"""
import pygame
from PIL import Image
from constants import *

class Map:
    def __init__(self):
        self.img_input = ".\image\default_map.png"

        self.list_objet = pygame.sprite.Group()
        self.list_wall = pygame.sprite.Group()
        self.list_sprite = pygame.sprite.Group()
    
    def get_server_input(self):
        """
        method to get an png map input from the server
        """
        pass

    def load(self):
        """
        method to load and convert the png map into data to display 
        the map (wall, object, player and ennemis position, etc)
        """
        self.map = Image.open(self.img_input)
        self.pixels = self.map.load()

        for x in range(self.map.size[0]):
            for y in range(self.map.size[1]):
                #print (self.pixels[x,y])  # Get the RGBA Value of the a pixel of an image
                # TODO : declare constant for map_img_color
                if self.pixels[x,y] == BLACK: 
                    wall = Wall(x, y)
                    self.list_wall.add(wall)
                    self.list_sprite.add(wall)
                if self.pixels[x,y] == WHITE: 
                    ground = Ground(x, y)
                    self.list_sprite.add(ground)
                
        
        #pix[x,y] = value  # Set the RGBA Value of the image (tuple)
        #im.save('alive_parrot.png')  # Save the modified pixels as .png

    def draw(self):
        """
        draw the map on the pygame window
        
        (might move this method to the game class ...) 
        """
        pass

class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(".\image\wall.png").convert_alpha() # TODO : create wall.png
        self.rect = self.image.get_rect()
        self.rect.y = TILE_SIZE * y
        self.rect.x = TILE_SIZE * x

class Ground(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(".\image\ground.png").convert_alpha() # TODO : create ground.png
        self.rect = self.image.get_rect()
        self.rect.y = TILE_SIZE * y
        self.rect.x = TILE_SIZE * x