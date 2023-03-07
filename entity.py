import pygame
from constants import *

class entity(pygame.sprite.Sprite):
    """
    Entity class for the player and other entity (enemy, teammate, etc)
    """
    def __init__(self) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(".\image\player.png").convert_alpha()
        self.rect = self.image.get_rect()
        # self.images = {
        #     "down" :  self.get_image(0, 0),
        #     "up" :    self.get_image(16, 0),
        #     "left" :  self.get_image(32, 0),
        #     "right" : self.get_image(48, 0)
        # }
        self.rect.y = None
        self.rect.x = None
        self.direction = '-'
        self.speed = 1.5
    
    def update(self):
        current_x = self.rect.x
        current_y = self.rect.y
        if self.direction == 'G':
            self.rect.x -= TILE_SIZE
            self.direction = '-'
        elif self.direction == 'D':
            self.rect.x += TILE_SIZE
            self.direction = '-'
        elif self.direction == 'H':
            self.rect.y -= TILE_SIZE
            self.direction = '-'
        elif self.direction == 'B':
            self.rect.y += TILE_SIZE
            self.direction = '-'

        list_wall = pygame.sprite.spritecollide(self, list_wall, False)
        if len(list_wall) > 0:
            self.rect.x = current_x
            self.rect.y = current_y