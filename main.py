import pygame
import sys
import pygame.gfxdraw

# CLASSES

class Paddle:
	
	def __init__(self, x, y):
		self.pos = pygame.Vector2 (x, y)
		self.vel = pygame.Vector2 (0, 0)
		self.w = 25
		self.h = 75
		self.color = '#d83dff'
		self.rect = pygame.Rect(self.pos.x, self.pos.y, self.w, self.h)

	def draw (self, surface):
		pygame.draw.rect (surface, self.color, self.rect)

	def setVerticalVelocity (self, vy):
		self.vel.y = vy		

	def move (self, dt):
		self.pos += self.vel * dt
		self.bindRect()

	def bindRect (self):
		self.rect.x = self.pos.x
		self.rect.y = self.pos.y



class Ball:

	def __init__(self):
		self.rad = 15
		self.pos = pygame.Vector2 (500 // 2, 500 // 2)
		self.vel = pygame.Vector2 (0, 0)
		self.color = pygame.Color ('#FAEBD7')

	def draw (self, surface):
		pygame.gfxdraw.aacircle (surface, int(self.pos.x), int(self.pos.y), self.rad, self.color)
		pygame.gfxdraw.filled_circle(surface, int(self.pos.x), int(self.pos.y), self.rad, self.color)
		


# SETUP
window = pygame.display.set_mode((500,500))

clock = pygame.time.Clock()

paddle_R = Paddle (500 - 25, 250 - 75 // 2)
paddle_L = Paddle (0, 250 - 75 // 2)

ball = Ball ()

speed = 100


# RUN
while 1:

	clock.tick (60)

	for e in pygame.event.get():
		if e.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

	keys = pygame.key.get_pressed()

	# print ('keys', keys[pygame.K_UP], keys[pygame.K_DOWN])

	if keys [pygame.K_UP]:
		paddle_R.setVerticalVelocity (-speed)
	if keys [pygame.K_DOWN]:
		paddle_R.setVerticalVelocity (speed)

	if keys[pygame.K_UP] == 0 and keys[pygame.K_DOWN] == 0:
		paddle_R.setVerticalVelocity(0)
	

	if keys [pygame.K_w]:
		paddle_L.setVerticalVelocity (-speed)
	if keys [pygame.K_s]:
		paddle_L.setVerticalVelocity (speed)

	if keys[pygame.K_w] == 0 and keys[pygame.K_s] == 0:
		paddle_L.setVerticalVelocity(0)


	dt = clock.get_time() / 1000.0
	paddle_L.move (dt)
	paddle_R.move (dt)

	window.fill ('#381f0e')

	ball.draw (window)
	paddle_L.draw (window)
	paddle_R.draw (window)

	pygame.display.update()