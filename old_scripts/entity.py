import pygame
from constants import *

class Entity(pygame.sprite.Sprite):
    """
    Entity class for the player and other entity (enemy, teammate, etc)
    """
    def __init__(self, position:tuple=[TILE_SIZE*2, TILE_SIZE*2], group=camera_group):
        super().__init__(group) # TODO : add group to the arguments
        pygame.sprite.Sprite.__init__(self)
        self.position = position  # coordinate of the player [x,y]
        self.image = pygame.image.load(".\image\player.png").convert_alpha()
        self.rect = self.image.get_rect(center = self.position)
        # self.images = {
        #     "down" :  self.get_image(0, 0),
        #     "up" :    self.get_image(16, 0),
        #     "left" :  self.get_image(32, 0),
        #     "right" : self.get_image(48, 0)
        # }
        #list_sprite.add(self)

        # self.x = 1 # real position for the game
        # self.y = 1
        # self.rect.x = TILE_SIZE # virtual position for the camera (position draw on sreen)
        # self.rect.y = TILE_SIZE
        self.direction = pygame.math.Vector2()
        self.speed = 4

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        # TODO : add sprite animation
    
    def get_input(self):
        keys = pygame.key.get_pressed()
        # y axe
        if keys[pygame.K_UP]:
            self.direction.y = -1
        elif keys[pygame.K_DOWN]:
            self.direction.y = 1
        else:
            self.direction.y = 0
        # x axe
        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
        else:
            self.direction.x = 0

def update(self):
        print("test")
        self.get_input()
        self.rect.center += self.direction * self.speed

        # collistion
        self.previous_position = self.position
        list_collided_wall = pygame.sprite.spritecollide(self, list_wall, False)
        if len(list_collided_wall) > 0:
            self.rect.centerx = self.previous_position[0]
            self.rect.centery = self.previous_position[1]
            pass
        else :
            self.position = [self.rect.centerx, self.rect.centery]

        #print(self.rect.x, self.rect.y) 

class Player(Entity):
    """
    The Player class inherits from the Entity class
    """
    def __init__(self):
        Entity.__init__(self)
        print("player created")
        # there will be more soon...