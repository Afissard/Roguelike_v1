import pygame
from constants import *

class Entity(pygame.sprite.Sprite):
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
        self.x = 1 # real position for the game
        self.y = 1
        self.rect.x = TILE_SIZE # virtual position for the camera (position draw on sreen)
        self.rect.y = TILE_SIZE
        self.direction = '-'
        self.speed = 4

        list_sprite.add(self)
    
    def draw(self, screen):
        screen.blit(self.image, self.rect)
        # TODO : add sprite animation
    
    def update(self):
        current_x = self.rect.x
        current_y = self.rect.y
        if self.direction == 'LEFT':
            self.rect.x -= self.speed
            self.direction = '-'
        elif self.direction == 'RIGHT':
            self.rect.x += self.speed
            self.direction = '-'
        elif self.direction == 'UP':
            self.rect.y -= self.speed
            self.direction = '-'
        elif self.direction == 'DOWN':
            self.rect.y += self.speed
            self.direction = '-'

        # collision system
        list_collided_wall = pygame.sprite.spritecollide(self, list_wall, False)
        if len(list_collided_wall) > 0:
            self.rect.x = current_x
            self.rect.y = current_y
        
        #print(self.rect.x, self.rect.y)

class Player(Entity):
    """
    The Player class inherits from the Entity class
    """
    def __init__(self) -> None:
        Entity.__init__(self)
        print("player created")
        # there will be more soon...