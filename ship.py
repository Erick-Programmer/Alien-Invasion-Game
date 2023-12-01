import pygame

class Ship():
	def __init__(self, ai_settings, screen):
		"""inicializa a espaçonave e define sua posição inicial"""
		self.screen = screen
		self.ai_settings = ai_settings
		
		#carrega a imagem da espaçonave e obtém seu rect
		self.image = pygame.image.load('images/ship.bmp')
		self.rect = self.image.get_rect() #rect - imagem como retangulo.
		self.screen_rect = screen.get_rect() #armazenamos o retangulo(imagem).
		
		#inicia cada espaçonave na parte inferior central da tela.
		self.rect.centerx = self.screen_rect.centerx #x
		self.rect.bottom = self.screen_rect.bottom #y
		
		# Armazena um valor decimal para o centro da espaçonave
		self.center = float(self.rect.centerx)
		
		#flags de movimento.
		self.moving_right = False
		self.moving_left = False
		
	def blitme(self):
		"""desenha a espaçonave em sua posição atual"""
		self.screen.blit(self.image, self.rect)
	
	def update(self):
		"""Atualiza a posição da espaçonave de acordo com a flag de movimento."""
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.center += self.ai_settings.ship_speed_factor #1.5+
		if self.moving_left and self.rect.left > 0:
			self.center -= self.ai_settings.ship_speed_factor #1.5-
		
		# Atualiza o objeto rect de acordo com self.center
		self.rect.centerx = self.center

	def center_ship(self):
		"""Centraliza a espaçonave na tela."""
		self.center = self.screen_rect.centerx
 