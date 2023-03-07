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
    
    def generate(self):
        """
        method to procedurally create the dungeon map
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
                for tile_id in range(len(COLOR)):
                    if self.pixels[x,y] == COLOR[tile_id]:
                        tile = Tile(x,y, tile_id +1)
                        self.list_sprite.add(tile)

class Tile(pygame.sprite.Sprite):
    """
    Class made for loading a tile set and add tile 
    to the sprite group and collision groupe.

    TODO :
        - find a way to add collision detection (add to the list_wall group ?)
        - load a tile set and use it instead of the actual 1 tile = 1 image
        - work on tile merge with linking tile texture
        - add no-texture tile to display if there is an error
    """
    def __init__(self, x, y, tile_id):
        pygame.sprite.Sprite.__init__(self)
        self.id = tile_id
        self.tile_data = { 
            # id : texture path, collision
            1 : [".\image\wall.png", True],
            2 : [".\image\ground.png", False]
        }
        self.image = pygame.image.load(self.tile_data[self.id][0]).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = TILE_SIZE * x
        self.rect.y = TILE_SIZE * y
