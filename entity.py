import pygame
from global_var import *

class Entity(pygame.sprite.Sprite):
	def __init__(self, position, group):
		super().__init__(group)
		self.position = position # screen or game position ?
		self.image = pygame.image.load('./image/player.png').convert_alpha()
		# self.images = {
        #     "down" :  self.get_image(0, 0),
        #     "up" :    self.get_image(16, 0),
        #     "left" :  self.get_image(32, 0),
        #     "right" : self.get_image(48, 0)
        # }
		self.rect = self.image.get_rect(center = self.position)
		self.coordinate = [self.rect.centerx, self.rect.centery]
		self.direction = pygame.math.Vector2()
		self.speed = 4

	def input(self):
		keys = pygame.key.get_pressed()

		if keys[pygame.K_UP]:
			self.direction.y = -1
		elif keys[pygame.K_DOWN]:
			self.direction.y = 1
		else:
			self.direction.y = 0

		if keys[pygame.K_RIGHT]:
			self.direction.x = 1
		elif keys[pygame.K_LEFT]:
			self.direction.x = -1
		else:
			self.direction.x = 0
	
	def collision(self):
		self.previous_coordinate = self.coordinate
		list_collided_wall = pygame.sprite.spritecollide(self, list_wall, False)
		if len(list_collided_wall) > 0:
			self.rect.centerx = self.previous_coordinate[0]
			self.rect.centery = self.previous_coordinate[1]
		else :
			self.coordinate = [self.rect.centerx, self.rect.centery]

	def update(self):
		self.input()
		self.rect.center += self.direction * self.speed
		self.collision()

class Player(Entity):
    """
    The Player class inherits from the Entity class
    """
    def __init__(self, pos, group):
        Entity.__init__(self, pos, group)
        # there will be more soon...