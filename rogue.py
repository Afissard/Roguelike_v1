import pygame, sys
from constants import *
from camera import *

class Player(pygame.sprite.Sprite):
	def __init__(self,pos,group):
		super().__init__(group)
		self.image = pygame.image.load('./image/player.png').convert_alpha()
		self.rect = self.image.get_rect(center = pos)
		self.direction = pygame.math.Vector2()
		self.speed = 5

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

	def update(self):
		self.input()
		self.rect.center += self.direction * self.speed

class Rogue():
    def __init__(self):
        self.screen = pygame.display.set_mode((1280,720))
        pygame.display.set_caption("Multiplayer Roguelike [v1.2]")
        self.clock = pygame.time.Clock()
        pygame.event.set_grab(True) # set to True if the game use the mouse

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

def main():
    pygame.init()
    game = Rogue()
    game.run()
    
if __name__ == "__main__":
    main()