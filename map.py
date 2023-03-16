"""
Pillow resources : https://stackoverflow.com/questions/138250/how-to-read-the-rgb-value-of-a-given-pixel-in-python

"""
import pygame
from PIL import Image
from global_var import *
from entity import *

class Map():
    def __init__(self):
        self.img_input = ".\image\default_map.png"
        self.need_load = True
    
    def generate(self):
        """
        method to procedurally create the dungeon map
        """
        pass

    def load(self, group):
        """
        method to load and convert the png map into data to display 
        the map (wall, object, player and enemies position, etc)
        """
        if self.need_load == True:
            self.map = Image.open(self.img_input)
            self.pixels = self.map.load()

            for x in range(self.map.size[0]):
                for y in range(self.map.size[1]):
                    for tile_id in range(len(COLOR)):
                        if self.pixels[x,y] == COLOR[tile_id]:
                            tile = Tile(x,y, tile_id +1, group) # TODO : offset x&y with the camera (center on player)
                            group.add(tile)
                        else : 
                            pass # TODO : draw the error tile
            
            self.need_load = False # to change when generating a new level

class Tile(pygame.sprite.Sprite):
    """
    Class made for loading a tile set and add tile 
    to the sprite group and collision groupe.

    TODO :
        - load a tile set and use it instead of the actual 1 tile = 1 image
        - work on tile merge with linking tile texture
        - add no-texture tile to display if there is an error
    """
    def __init__(self, x, y, tile_id, group):
        super().__init__(group)
        pygame.sprite.Sprite.__init__(self)
        self.id = tile_id
        self.tile_data = {
            # id : texture path,        collision
            1 : [".\image\wall.png",    True],
            2 : [".\image\ground.png",  False]
        }
        # load texture
        self.image = pygame.image.load(self.tile_data[self.id][0]).convert_alpha()
        self.rect = self.image.get_rect()
        # real position for the game
        self.x = x
        self.y = y
        # virtual position for the camera (position draw on screen)
        self.rect.x = TILE_SIZE * self.x
        self.rect.y = TILE_SIZE * self.y

        # add collision
        if self.tile_data[self.id][1] == True :
            list_wall.add(self)
    
    # TODO : add update method to add interaction for example a door open/close ...