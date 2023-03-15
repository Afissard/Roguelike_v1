import pygame
from camera import *

# Tiles and Window setting
TILE_SIZE = 16
scr_width = TILE_SIZE * 64
scr_height = TILE_SIZE * 48

# COLOR (from Pico8 color palette):
COLOR = [
    (0,0,0),        # Black
    (255,241,232),  # White
    (255,0,77),     # Red
    (0,228,54)      # Light Green
]

# group of sprite and other
#camera_group = CameraGroup()
list_sprite = pygame.sprite.Group()
list_wall = pygame.sprite.Group()
#list_objet = pygame.sprite.Group()