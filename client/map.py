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
                # TODO : work on tile merge with linking tile texture
                if self.pixels[x,y] == BLACK: 
                    wall = Wall(x, y)
                    self.list_wall.add(wall)
                    self.list_sprite.add(wall)
                if self.pixels[x,y] == WHITE: 
                    ground = Ground(x, y)
                    self.list_sprite.add(ground)

# TODO : create a class for all tile
class Tiles(pygame.sprite.Sprite):
    """
    Class made for loading a tile set and add tile 
    to the sprite group and collision groupe.

    All the diffrent tile will be a child of the Tiles class, and may have
    there own parameter like collision, special interaction ???
    """
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(".\image\wall.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.y = TILE_SIZE * y
        self.rect.x = TILE_SIZE * x

class Ground(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(".\image\ground.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.y = TILE_SIZE * y
        self.rect.x = TILE_SIZE * x